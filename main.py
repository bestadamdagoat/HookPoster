from configparser import ConfigParser
import time
import requests

def sendwebhook(webhook):
    data = {
        "embeds": [{
        "title": title,
        "description": description,
        "url": url,
        "author": {
        "name": name,
        "url": author_url,
        "icon_url": icon_url,
        },
        "image": {
        "url": image_url
        }
        }]
    }
    result = requests.post(webhook, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        time.sleep(2)
        print("Quitting")
        quit(time.sleep(2))

config_object = ConfigParser(interpolation=None)
config_object.read("config.ini")
try:
    config = config_object["CONFIG"]
except KeyError:
    writeconfig = open("config.ini", "w")
    writeconfig.write("[CONFIG]\ntest_webhook = https://www.testwebhook.com/\nname = Unconfigured HookPoster\nauthor_url = https://github.com/bestadamdagoat/HookPoster\nicon_url = https://avatars.githubusercontent.com/u/66372881?v=4")
    print("Config file missing. Don't worry though, I made one for you with the default options. Make sure to change the webhook to your own webhook.")
    time.sleep(2)
    print("Quitting")
    quit(time.sleep(2))

test_webhook = str(config["test_webhook"])
name = config["name"]
author_url = config["author_url"]
icon_url = config["icon_url"]
againbreak = False

title = input("Title? ")
description = input("Description? ")
url = input("Title URL? ")
image_url = input("Image URL? ")

print("Do you want to send a test webhook? (Y/N)")
while True:
    if againbreak == True:
        break
    continuewithprogram = input()
    if continuewithprogram.lower() not in ('y', 'n'):
        continue
    if continuewithprogram.lower() == "y":
        sendwebhook(test_webhook)
        print("Looks good? (Y/N)")
        while True:
            continuewithprogramagain = input()
            if continuewithprogramagain.lower() not in ('y', 'n'):
                continue
            if continuewithprogramagain.lower() == "y":
                againbreak = True
                break
            else:
                quit(print("Quitting"))
    else:
        continue

try:
    webhooklist = open('webhooklist.txt')
except FileNotFoundError:
    errorprocess("No webhooks specified. Make sure you created a webhooklist.txt file.")

while True:
    currentwebhook = webhooklist.readline()
    if not currentwebhook:
        quit(print("End of Webhooks"))
    currentwebhook = currentwebhook.replace('\n', '')
    sendwebhook(currentwebhook)
    print("Sent A Webhook")