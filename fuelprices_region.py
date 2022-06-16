# Load the required packges
import requests
from influxdb import InfluxDBClient

# Define the variables
client = InfluxDBClient(host='localhost', port=8086, database='fuelprices')

response = requests.get("https://creativecommons.tankerkoenig.de/json/prices.php?ids=4429a7d9-fb2d-4c29-8cfe-2ca90323f9f8&apikey=00000000-0000-0000-0000-000000000002")

if response:
  jsonResponse = response.json()
  json_body = [
    {
      "measurement": "Region",
      "tags": {
        "station_id": "insert_id_here",
        "station_name": "insert_name_here"
      },
      "fields": {
        "e5": jsonResponse["prices"]["insert_id_here"]["e5"],
        "diesel": jsonResponse["prices"]["insert_id_here"]["diesel"]
      }
    }
  ]
  print(json_body)
else:
  print('Request returned an error.')
  
client.write_points(json_body, time_precision='s')
