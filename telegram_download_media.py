from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.sessions import StringSession
import os
from functools import partial
import asyncio


# https://my.telegram.org/auth?to=apps
api_id = ''
api_hash = ''
phone = '' # your phone number or bot token
channel_username = '' # channel username without @ for example t.me/@channel_username or just channel_username
file_prefix = 'file_prefix'

season_ranges = {
    # Folder Name : (Start Episode, End Episode)
    'Season 1': (1, 28),
    'Season 2': (29, 54),
    'Season 3': (55, 82),
    'Season 4': (83, 106),
    'Season 5': (107, 134),
    'Season 6': (135, 162),
    'Season 7': (163, 193),
    'Season 8': (194, 219),
    'Season 9': (220, 254),
    'Season 10': (255, 285),
    'Season 11': (286, 315),
    'Season 12': (316, 353),
    'Season 13': (354, 389),
    'Season 14': (390, 426),
    'Season 15': (427, 465),
    'Season 16': (466, 490),
    'Season 17': (491, 523),
    'Season 18': (524, 565),
    'Season 19': (566, 605),
    'Season 20': (606, 645),
    'Season 21': (646, 680),
    'Season 22': (681, 723),
    'Season 23': (724, 762),
    'Season 24': (763, 803),
    'Season 25': (804, 886),
    'Season 26': (887, 926),
    'Season 27': (927, 964),
}

excluded_keywords = {
    "Movie",
    "Special",
}


def get_season_folder(episode_number):
    """Obtain the name of the season folder based on the episode number."""
    for season, (start, end) in season_ranges.items():
        if start <= episode_number <= end:
            return season
    return None

progress_status = {}

def create_progress_bar(percentage, bar_length=50):
    """Returns a visual representation of a progress bar with the percentage at the end."""
    filled_blocks = int(percentage / 100 * bar_length)
    empty_blocks = bar_length - filled_blocks
    return "|" + "█" * filled_blocks + "-" * empty_blocks + f"| {percentage:.2f}%"

def update_console():
    """Update the console with the progress of all files."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clean the console
    for filename, progress in progress_status.items():
        progress_bar = create_progress_bar(progress)
        print(f"[{filename}] {progress_bar}")

def progress_callback(downloaded_bytes, total_bytes, filename):
    progress_percentage = (downloaded_bytes / total_bytes) * 100
    progress_status[filename] = progress_percentage
    update_console()

## WORKING IN PROGRESS - NOT WORKING YET
def update_metadata(filename, episode_str, title):
    """Update the MP4 file metadata with the title provided."""
    #translated_title = translator.translate(title, src='es', dest='en').text
    full_title = f"{episode_str} - {title}"
    
    with open(filename, 'rb+') as f:
        mp4['moov']['trak'][0]['tkhd']['track_name'] = full_title
        f.seek(0)
        f.write(mp4.serialize())


semaphore = asyncio.Semaphore(3)  # To limit 3 concurrent downloads

async def download_episode(client, message):
    async with semaphore:  # Limits 3 concurrent downloads
        if not message.text:
            return

        if any(keyword in message.text for keyword in excluded_keywords):
            return

        text_parts = message.text.split(" ", 1)
        if len(text_parts) == 2:
            episode_str, title = text_parts
            try:
                episode_number = int(episode_str)
            except ValueError:
                return

            season_folder = get_season_folder(episode_number)
            if season_folder:
                if not os.path.exists(season_folder):
                    os.mkdir(season_folder)

                filename = f"{file_prefix}_{episode_str}_{title.replace(' ', '_')}.mp4"
                path_to_save = os.path.join(season_folder, filename)
                if os.path.exists(path_to_save):
                    return

                await client.download_media(message, path_to_save, progress_callback=partial(progress_callback, filename=filename))
                #update_metadata(path_to_save, episode_str, title)
                del progress_status[filename]


async def main():
    async with TelegramClient(phone, api_id, api_hash) as client:
        # Get channel information
        channel = await client.get_entity(channel_username)
        channel_details = InputPeerChannel(channel.id, channel.access_hash)

        # Get messages and plan downloads
        tasks = []
        async for message in client.iter_messages(channel_details):
            tasks.append(download_episode(client, message))
        
        # Wait for all downloads to be completed
        await asyncio.gather(*tasks)

print("Starting discharges ...")
asyncio.run(main())
print("All downloads have been completed.")
