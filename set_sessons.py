import os
import re

season_ranges = {
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

def get_season(episode_num):
    """
    Returns the season number for a given episode number.

    Args:
        episode_num (int): The episode number.

    Returns:
        int: The season number, or None if the episode number is not within any season range.
    """
    for season, (start, end) in season_ranges.items():
        if start <= episode_num <= end:
            return season
    return None

    
"""
Organizes media files in the current directory by season.

- Scans files in the current directory for episode numbers.
- Determines the season for each episode.
- Moves files into corresponding season directories.

Requires:
- os: For directory operations.
- re: For episode number extraction.
"""
current_directory = os.getcwd()
files = os.listdir(current_directory)

for file in files:
    match = re.search(r'(\d+)', file)
    if match:
        episode_num = int(match.group(1))
        season = get_season(episode_num)
        
        if season:
            season_directory = os.path.join(current_directory, season)
            
            if not os.path.exists(season_directory):
                os.makedirs(season_directory)
            
            os.rename(os.path.join(current_directory, file), os.path.join(season_directory, file))

print("Files moved correctly!")