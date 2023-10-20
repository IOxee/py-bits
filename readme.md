<img src="https://github.com/IOxee/py-bits/assets/48241519/00304b43-058c-47d6-8952-1218f91739c7" style="display: flex; justify-content: center;">

A collection of Python scripts for various utilities and tasks.

## Scripts

### 1. [set sessions](https://github.com/IOxee/py-bits/blob/main/set_sessons.py)
This script organizes media files in the current directory by season. It scans files in the current directory for episode numbers, determines the season for each episode, and then moves files into corresponding season directories.

**Dependencies**:
- `os`: For directory operations.
- `re`: For episode number extraction.

### 2. [mouse anti afk](https://github.com/IOxee/py-bits/blob/main/mouse_anti_afk.py)
This script makes the mouse cursor move in a circle pattern on the screen. It uses the 'clicknium' library to control the mouse and basic trigonometry to calculate the circular path.

**Parameters**:
- `w`: Defines the number of steps for a complete circle.
- `m`: A factor derived from `w` to scale the circle steps.
- `r`: Radius of the circle.

**Dependencies**:
- `time`: To introduce a delay between each step.
- `math`: For trigonometric calculations.
- `clicknium`: To control the mouse position.

### 3. [telegram download media](https://github.com/IOxee/py-bits/blob/main/telegram_download_media.py)
This script is used to download media from a Telegram channel. It requires the user to provide API credentials and the channel username. The script then downloads media files and organizes them based on episode numbers.

**Dependencies**:
- `telethon`: For interacting with Telegram API.
- `os`: For file and directory operations.
- `functools`: For higher-order functions and operations on callable objects.
- `asyncio`: For asynchronous I/O.

### 4. [check episodes](https://github.com/IOxee/py-bits/blob/main/check_episodes.py)
This script checks if all episodes of a TV show are present in a given directory. It prints out messages indicating which episodes are missing.

**Dependencies**:
- `os`: For directory operations.

---

## License

Copyright 2023 IOxee

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Disclaimer

The scripts and tools in this repository are provided "as is" without any guarantees or warranty. The author is not responsible for any damage or issues that may arise from using the scripts. Always backup your data and use at your own risk.

---

**Note**: Ensure you have the necessary dependencies installed and always follow the guidelines and instructions provided in the scripts.
