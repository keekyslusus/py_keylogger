# keylogger with discord Integration

this is a simple python keylogger script that logs keystrokes and sends periodic reports to a discord webhook. the keylogger uses the `pynput` library to monitor keyboard input and the `requests` library to send messages to a discord channel.

## features

- logs keystrokes and formats special keys for readability.
- periodically sends logs to a specified discord webhook.
- notifies on specific keywords (e.g., "mail") detected in the logs.

## prerequisites

- python 3.x
- install required dependencies: `pip install pynput`

## configuration

1. set the `DISCORD_WEBHOOK_URL` variable in the script to your Discord webhook URL.
2. adjust the `SEND_REPORT_EVERY` variable to set the reporting interval.

## usage

1. run the script: `python keylogger.py`
2. the keylogger will start monitoring keystrokes in the background.
3. periodically, it will send logs to the specified Discord channel.
4. pyinstaller: `pyinstaller --noconsole --icon=icon.ico --onefile py_keylogger.py` (optional)

**note: use this script responsibly and in compliance with legal and ethical standards. unauthorized use of keyloggers is strictly prohibited.**

## legal disclaimer

this software is provided for educational purposes only. unauthorized use of this script for malicious purposes is against the law.

## license

licensed under the [MIT License](LICENSE).

**inspired by the work of [Aydin Yunus](https://github.com/aydinnyunus), specifically the [Keylogger](https://github.com/aydinnyunus/Keylogger) project.**

