import json
#import tkinter as tk

# Open the tardys3 reservation format
with open('tardys3.json') as f:
    tardys3 = json.load(f)

# Input tardys3 parameters
transaction_id = input("Enter transaction ID: ")
published_date = input("Enter published date (YYYY-MM-DD HH:MM:SS): ")
created_date = input("Enter created date (YYYY-MM-DD HH:MM:SS): ")
checksum = input("Enter checksum: ")
event_id = input("Enter event ID: ")
dpa_id = input("Enter DPA ID: ")
dpa_name = input("Enter DPA name: ")
channels = input("Enter channels (comma-separated): ")
start_time = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
end_time = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")
recurrence = input("Enter recurrence (optional): ")

# Convert comma-separated channels into a list
channels = channels.split(",")

# Update the dictionary with user inputs
tardys3.update({
    "transactionId": transaction_id,
    "publishedDate": published_date,
    "createdDate": created_date,
    "checksum": checksum,
    "event_id": event_id,
    "dpa_id": dpa_id,
    "dpa_name": dpa_name,
    "channels": channels,
    "start_time": start_time,
    "end_time": end_time,
    "recurrence": recurrence
})

print(json.dumps(tardys3, indent=4))