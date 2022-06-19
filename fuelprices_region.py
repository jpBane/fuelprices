# Load the required packges
import requests
from influxdb import InfluxDBClient

# Define the variables
client = InfluxDBClient(host='localhost', port=8086, database='fuelprices')

response = requests.get("https://creativecommons.tankerkoenig.de/json/prices.php?ids=b43b5fcd-17ad-4143-9002-a98cc5b50cb8,bf6b5ee4-1eec-4e6a-bac2-fdaea055a4a9,00062259-1d51-4444-8888-acdc00000001,f9849d77-faed-4730-8755-d4db80e65d62,1f136233-03c3-475a-b796-5d30c21e6709,871828b4-37e5-419c-b7a5-cdbe1e1c0148,51d4b443-a095-1aa0-e100-80009459e03a,005056a9-779e-1eec-8fb1-9cf11c7c8e2d&apikey=00000000-0000-0000-0000-000000000002")

# Try to generate the output for the InfluxDB. Return a message if this is not possible. 
if response:
  jsonResponse = response.json()
  try:
    json_body_b43 = [
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
      }
    ]
  except:
    print("Shell Oberkirch ist geschlossen.")

  try:
    json_body_bf6 = [
      {
        "measurement": "Ortenau",
        "tags": {
          "station_id": "bf6b5ee4-1eec-4e6a-bac2-fdaea055a4a9",
          "station_name": "Classic Oberkirch"
        },
        "fields": {
          "e5": jsonResponse["prices"]["bf6b5ee4-1eec-4e6a-bac2-fdaea055a4a9"]["e5"],
          "diesel": jsonResponse["prices"]["bf6b5ee4-1eec-4e6a-bac2-fdaea055a4a9"]["diesel"]
        }
      }
    ]
  except:
    print("Classic Oberkirch ist geschlossen.")

  try:
    json_body_000 = [
      {
        "measurement": "Ortenau",
        "tags": {
          "station_id": "00062259-1d51-4444-8888-acdc00000001",
          "station_name": "Bft-Tankstelle Achern"
        },
        "fields": {
          "e5": jsonResponse["prices"]["00062259-1d51-4444-8888-acdc00000001"]["e5"],
          "diesel": jsonResponse["prices"]["00062259-1d51-4444-8888-acdc00000001"]["diesel"]
        }
      }
    ]
  except:
    print("Bft Achern ist geschlossen.")
    
  try:
    json_body_f98 = [
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
      }
    ]
  except:
    print("Marktkaufstation Offenburg ist geschlossen.")
    
  try:
    json_body_1f1 = [
      {
        "measurement": "Ortenau",
        "tags": {
          "station_id": "1f136233-03c3-475a-b796-5d30c21e6709",
          "station_name": "TotalEnergies Schutterwald"
        },
        "fields": {
          "e5": jsonResponse["prices"]["1f136233-03c3-475a-b796-5d30c21e6709"]["e5"],
          "diesel": jsonResponse["prices"]["1f136233-03c3-475a-b796-5d30c21e6709"]["diesel"]
        }
      }
    ]
  except:
    print("TotalEnergies Schutterwald ist geschlossen.")
    
  try:
    json_body_871 = [
      {
        "measurement": "Ortenau",
        "tags": {
          "station_id": "871828b4-37e5-419c-b7a5-cdbe1e1c0148",
          "station_name": "Tankhof Grün Willstätt"
        },
        "fields": {
          "e5": jsonResponse["prices"]["871828b4-37e5-419c-b7a5-cdbe1e1c0148"]["e5"],
          "diesel": jsonResponse["prices"]["871828b4-37e5-419c-b7a5-cdbe1e1c0148"]["diesel"]
        }
      }
    ]
  except:
    print("Tankhof Grün Willstätt ist geschlossen.")

  try:
    json_body_51d = [
      {
        "measurement": "Ortenau",
        "tags": {
          "station_id": "51d4b443-a095-1aa0-e100-80009459e03a",
          "station_name": "JET München Landsberger Str."
        },
        "fields": {
          "e5": jsonResponse["prices"]["51d4b443-a095-1aa0-e100-80009459e03a"]["e5"],
          "diesel": jsonResponse["prices"]["51d4b443-a095-1aa0-e100-80009459e03a"]["diesel"]
        }
      }
    ]
  except:
    print("JET München Landsberger Str. ist geschlossen.")
    
  try:
    json_body_005 = [
      {
        "measurement": "Ortenau",
        "tags": {
          "station_id": "005056a9-779e-1eec-8fb1-9cf11c7c8e2d",
          "station_name": "Freie Tankstelle Leverkusen Alkenrath"
        },
        "fields": {
          "e5": jsonResponse["prices"]["005056a9-779e-1eec-8fb1-9cf11c7c8e2d"]["e5"],
          "diesel": jsonResponse["prices"]["005056a9-779e-1eec-8fb1-9cf11c7c8e2d"]["diesel"]
        }
      }
    ]
  except:
    print("Freie Tankstelle Leverkusen Alkenrath ist geschlossen.")
    
# Return an error message if the request did not work
else:
  print('Request returned an error.')

# Write the prepared JSON data to the database. Return an error message in case the respective JSON object does not exist (station closed).
try:
  client.write_points(json_body_b43, time_precision='s')
except:
  print("Daten für Shell Oberkirch nicht übertragen.")

try:
  client.write_points(json_body_bf6, time_precision='s')
except:
  print("Daten für Classic Oberkirch nicht übertragen.")
  
try:
  client.write_points(json_body_000, time_precision='s')
except:
  print("Daten für Bft Achern nicht übertragen.")
  
try:
  client.write_points(json_body_f98, time_precision='s')
except:
  print("Daten für Marktkaufstation Offenburg nicht übertragen.")

try:
  client.write_points(json_body_1f1, time_precision='s')
except:
  print("Daten für TotalEnergies Schutterwald nicht übertragen.")
  
try:
  client.write_points(json_body_871, time_precision='s')
except:
  print("Daten für Tankhof Grün Willstätt nicht übertragen.")

try:
  client.write_points(json_body_51d, time_precision='s')
except:
  print("Daten für JET München Landsberger Str. nicht übertragen.")
  
try:
  client.write_points(json_body_005, time_precision='s')
except:
  print("Daten für Freie Tankstelle Leverkusen Alkenrath nicht übertragen.")
