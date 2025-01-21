import json
import tkinter as tk
from tkinter import messagebox

def submit():
    # Get user inputs from text fields
    tardys3.update({
        "transactionId": transaction_id_entry.get(),
        "publishedDate": published_date_entry.get(),
        "createdDate": created_date_entry.get(),
        "checksum": checksum_entry.get(),
        "event_id": event_id_entry.get(),
        "dpa_id": dpa_id_entry.get(),
        "dpa_name": dpa_name_entry.get(),
        "channels": channels_entry.get().split(","),
        "start_time": start_time_entry.get(),
        "end_time": end_time_entry.get(),
        "recurrence": recurrence_entry.get()
    })

    # Save updated JSON
    with open('tardys3.json', 'w') as f:
        json.dump(tardys3, f, indent=4)
    
    messagebox.showinfo("Success", "TARDyS3 reservation updated successfully!")

# Load existing TARDyS3 JSON
with open('tardys3.json') as f:
    tardys3 = json.load(f)

# Create Tkinter window
root = tk.Tk()
root.title("TARDyS3 Reservation Form")

# Define input fields
labels = ["Transaction ID", "Published Date", "Created Date", "Checksum", "Event ID",
          "DPA ID", "DPA Name", "Channels (comma-separated)", "Start Time", "End Time", "Recurrence"]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

(transaction_id_entry, published_date_entry, created_date_entry, checksum_entry,
 event_id_entry, dpa_id_entry, dpa_name_entry, channels_entry,
 start_time_entry, end_time_entry, recurrence_entry) = entries

# Submit button
tk.Button(root, text="Submit", command=submit).grid(row=len(labels), column=0, columnspan=2)

root.mainloop()
