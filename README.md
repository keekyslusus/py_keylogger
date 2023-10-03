# Keylogger with Discord Integration

This is a simple Python keylogger script that logs keystrokes and sends periodic reports to a Discord webhook. The keylogger uses the `pynput` library to monitor keyboard input and the `requests` library to send messages to a Discord channel.

## Features

- Logs keystrokes and formats special keys for readability.
- Periodically sends logs to a specified Discord webhook.
- Notifies on specific keywords (e.g., "mail") detected in the logs.

## Prerequisites

- Python 3.x
- Install required dependencies: `pip install pynput`

## Configuration

1. Set the `DISCORD_WEBHOOK_URL` variable in the script to your Discord webhook URL.
2. Adjust the `SEND_REPORT_EVERY` variable to set the reporting interval.

## Usage

1. Run the script: `python keylogger.py`
2. The keylogger will start monitoring keystrokes in the background.
3. Periodically, it will send logs to the specified Discord channel.

**Note: Use this script responsibly and in compliance with legal and ethical standards. Unauthorized use of keyloggers is strictly prohibited.**

## Legal Disclaimer

This software is provided for educational purposes only. Unauthorized use of this script for malicious purposes is against the law.

## License

This project is licensed under the [MIT License](LICENSE).

