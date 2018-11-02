import requests
import json
import os

from time import time, sleep
from subprocess import check_output

API_KEY = os.getenv('DATADOG_TOKEN', '')
hid = os.getenv('HID', '')
url = "https://app.datadoghq.com/api/v1/series?api_key=%s" % API_KEY
debug = os.getenv('debug', '')


def get_params():
    res = check_output(["./ht2000", hid])
    _, _, temp, humidity, co2 = [x.strip() for x in res.split(',')]
    if debug:
        print(temp, humidity, co2)
    return [
        {"metric": "office.temp", "points": [[time(), float(temp)]], "host": "officeCheck"},
        {"metric": "office.humidity", "points": [[time(), float(humidity)]], "host": "officeCheck"},
        {"metric": "office.co2", "points": [[time(), float(co2)]], "host": "officeCheck"},
    ]


def log():
    while True:
        try:
            series = get_params()
            requests.post(url, data=json.dumps({"series": series}))
        except Exception as e:
            print(e)
        sleep(10)


if __name__ == '__main__':
    log()
