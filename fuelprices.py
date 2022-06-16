# Load the required packages
import requests
from influxdb import InfluxDBClient

# Define the variables
client = InfluxDBClient(host='localhost', port=8086, database='database_name')

response = requests.get('https://creativecommons.tankerkoenig.de/json/list.php?lat=51&lng=9.8&rad=1&sort=dist&type=all&apikey=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')

if response:
  jsonResponse = response.json()
  json_body = [
    {
      "measurement": "Ortenau",
      "tags": {
        "station_id": jsonResponse["stations"][0]["id"],
        "station_name": jsonResponse["stations"][0]["name"]
      },
      "fields": {
        "e5": jsonResponse["stations"][0]["e5"]
      }
    }
  ]
  print(json_body)
else:
  print('Request returned an error.')
  
# client.write_points(json_body, time_precision='s')
