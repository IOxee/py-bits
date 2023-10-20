import os

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


def check_episodes(directory):
    """
    Check if all episodes of a TV show are present in a given directory.

    Args:
        directory (str): The path to the directory containing the TV show episodes.

    Returns:
        None: This function does not return anything. It prints out messages indicating which episodes are missing.
    """

    for season, (start, end) in season_ranges.items():
        season_path = os.path.join(directory, season)
        if not os.path.exists(season_path):
            print(f"Folder {season} does not exist.")
            continue

        for episode in range(start, end + 1):
            patterns = {
                f"Case Closed - {str(episode).zfill(3)}",
                f"Case_Close_{str(episode).zfill(3)}",
            }
            found = False
            for file in os.listdir(season_path):
                if any(pattern in file for pattern in patterns):
                    found = True
                    break
            
            if not found:
                print(f"Episode {episode} is missing from {season}.")

if __name__ == "__main__":
    # Automatically detects the mother folder based on the location of the script
    main_directory = os.path.dirname(os.path.abspath(__file__))
    check_episodes(main_directory)
