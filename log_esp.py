import os
import json
import requests
from time import sleep, time

API_KEY = os.getenv('DATADOG_TOKEN', '')
IP_ADDR = os.getenv('ESP_IP_ADDR', '10.10.0.145')
url = "https://app.datadoghq.com/api/v1/series?api_key=%s" % API_KEY

def get_params():
   data = requests.get('http://%s/readjson' % IP_ADDR).json()
   co2 = data['sensors']['co2']
   events = []
   events.append(
      {"metric": "office.v2.co2", "points": [[time(), float(co2)]], "host": "officeCheck"}
   )
   return events


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
