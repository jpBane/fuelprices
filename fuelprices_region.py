# Load the required packges
import requests
from influxdb import InfluxDBClient

# Define the variables
client = InfluxDBClient(host='localhost', port=8086, database='fuelprices')

response = requests.get("https://creativecommons.tankerkoenig.de/json/prices.php?ids=b43b5fcd-17ad-4143-9002-a98cc5b50cb8,bf6b5ee4-1eec-4e6a-bac2-fdaea055a4a9,00062259-1d51-4444-8888-acdc00000001,f9849d77-faed-4730-8755-d4db80e65d62,871828b4-37e5-419c-b7a5-cdbe1e1c0148&apikey=00000000-0000-0000-0000-000000000002")

if response:
  jsonResponse = response.json()
  json_body = [
    {
      "measurement": "Ortenau",
      "tags": {
        "station_id": "00062259-1d51-4444-8888-acdc00000001",
        "station_name": "Bft-Tankstelle Schnurr Achern"
      },
      "fields": {
        "e5": jsonResponse["prices"]["00062259-1d51-4444-8888-acdc00000001"]["e5"],
        "diesel": jsonResponse["prices"]["00062259-1d51-4444-8888-acdc00000001"]["diesel"]
      }
    },
    {
      "measurement": "Ortenau",
      "tags": {
        "station_id": "b43b5fcd-17ad-4143-9002-a98cc5b50cb8",
        "station_name": "Shell Oberkirch"
      },
      "fields": {
        "e5": jsonResponse["prices"]["b43b5fcd-17ad-4143-9002-a98cc5b50cb8"]["e5"],
        "diesel": jsonResponse["prices"]["b43b5fcd-17ad-4143-9002-a98cc5b50cb8"]["diesel"]
      }
    },
    {
      "measurement": "Ortenau",
      "tags": {
        "station_id": "f9849d77-faed-4730-8755-d4db80e65d62",
        "station_name": "Marktkaufstation Offenburg"
      },
      "fields": {
        "e5": jsonResponse["prices"]["f9849d77-faed-4730-8755-d4db80e65d62"]["e5"],
        "diesel": jsonResponse["prices"]["f9849d77-faed-4730-8755-d4db80e65d62"]["diesel"]
      }
    },
    {
      "measurement": "Ortenau",
      "tags": {
        "station_id": "871828b4-37e5-419c-b7a5-cdbe1e1c0148",
        "station_name": "Tankhof Grün - Willstätt"
      },
      "fields": {
        "e5": jsonResponse["prices"]["871828b4-37e5-419c-b7a5-cdbe1e1c0148"]["e5"],
        "diesel": jsonResponse["prices"]["871828b4-37e5-419c-b7a5-cdbe1e1c0148"]["diesel"]
      }
    }
  ]
  print(json_body)
else:
  print('Request returned an error.')
  
client.write_points(json_body, time_precision='s')
