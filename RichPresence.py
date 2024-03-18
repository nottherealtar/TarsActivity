import tkinter as tk
from tkinter import messagebox 
from tkinter import messagebox, ttk
from tkinter import *
import validators
from pypresence import Presence
import json

# Function to validate the inputs
def validate_inputs():
    url1 = button1_url_entry.get()
    url2 = button2_url_entry.get()

    if not validators.url(url1) or not validators.url(url2):
        messagebox.showerror("Invalid URL", "Please enter a valid URL.")
        return False

    # Add more validation checks here as needed

    return True

# Function to update the rich presence
def update_presence():
    if not validate_inputs():
        return

    try:
        client_id = client_id_entry.get()
        details = details_entry.get() if details_entry.get() else None
        state = state_entry.get() if state_entry.get() else None
        large_image = large_image_entry.get() if large_image_entry.get() else None
        small_image = small_image_entry.get() if small_image_entry.get() else None
        button1_label = button1_label_entry.get() if button1_label_entry.get() else None
        button1_url = button1_url_entry.get() if button1_url_entry.get() else None
        button2_label = button2_label_entry.get() if button2_label_entry.get() else None
        button2_url = button2_url_entry.get() if button2_url_entry.get() else None
        start_timestamp = int(start_timestamp_entry.get()) if start_timestamp_entry.get() else None
        end_timestamp = int(end_timestamp_entry.get()) if end_timestamp_entry.get() else None
        party_size = int(party_size_entry.get()) if party_size_entry.get() else None
        party_max = int(party_max_entry.get()) if party_max_entry.get() else None

        RPC = Presence(client_id)  # Create a new Presence object
        RPC.connect()  # Connect to Discord

        # Update the rich presence with the user's input
        RPC.update(details=details, state=state, large_image=large_image, small_image=small_image,
                   buttons=[{"label": button1_label, "url": button1_url}, {"label": button2_label, "url": button2_url}],
                   start=start_timestamp, end=end_timestamp, party_size=[party_size, party_max])
    except Exception as e:
        messagebox.showerror("Error", str(e))
# Function to clear the rich presence
def clear_presence():
    try:
        client_id = client_id_entry.get()
        RPC = Presence(client_id)  # Create a new Presence object
        RPC.connect()  # Connect to Discord
        RPC.clear()  # Clear the rich presence
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to save the current inputs as a preset        
def save_preset():
    preset = {
        'client_id': client_id_entry.get(),
        'details': client_id_entry.get(),
        'state': client_id_entry.get(),
        'large_image_': client_id_entry.get(),
        'small_image': client_id_entry.get(),
        'button1_label': client_id_entry.get(),
        'button1_url': client_id_entry.get(),
        'button2_label': client_id_entry.get(),
        'button2_url': client_id_entry.get(),
        # ... repeat for all other inputs ...
    }
    with open('preset.json', 'w') as f:
        json.dump(preset, f)

# Function to load a preset
def load_preset():
    with open('preset.json', 'r') as f:
        preset = json.load(f)
    client_id_entry.insert(0, preset['client_id'])

# Function to login
def login():
    client_id = client_id_entry.get()
    global RPC
    RPC = Presence(client_id)  # Create a new Presence object
    RPC.connect()  # Connect to Discord

root = tk.Tk()
root.geometry("500x500")  # Set initial window size (width x height)
root.resizable(True, True)  # Make window resizable


# Use ttk for improved UI elements
client_id_label = ttk.Label(root, text="Client ID")
client_id_entry = ttk.Entry(root)
details_label = ttk.Label(root, text="Details")
details_entry = ttk.Entry(root)
state_label = ttk.Label(root, text="State")
state_entry = ttk.Entry(root)
large_image_label = ttk.Label(root, text="Large Image Key")
large_image_entry = ttk.Entry(root)
small_image_label = ttk.Label(root, text="Small Image Key")
small_image_entry = ttk.Entry(root)
button1_label_label = ttk.Label(root, text="Button 1 Label")
button1_label_entry = ttk.Entry(root)
button1_url_label = ttk.Label(root, text="Button 1 URL")
button1_url_entry = ttk.Entry(root)
button2_label_label = ttk.Label(root, text="Button 2 Label")
button2_label_entry = ttk.Entry(root)
button2_url_label = ttk.Label(root, text="Button 2 URL")
button2_url_entry = ttk.Entry(root)
start_timestamp_label = ttk.Label(root, text="Start Timestamp")
start_timestamp_entry = ttk.Entry(root)
end_timestamp_label = ttk.Label(root, text="End Timestamp")
end_timestamp_entry = ttk.Entry(root)
party_size_label = ttk.Label(root, text="Party Size")
party_size_entry = ttk.Entry(root)
party_max_label = ttk.Label(root, text="Party Max")
party_max_entry = ttk.Entry(root)
update_button = ttk.Button(root, text="Update Presence", command=update_presence)
clear_presence_button = ttk.Button(root, text="Clear Presence", command=clear_presence)
save_preset_button = ttk.Button(root, text="Save Preset", command=save_preset)
load_preset_button = ttk.Button(root, text="Load Preset", command=load_preset)
login_button = ttk.Button(root, text="Login", command=login)


# Pack the GUI elements into the window
client_id_label.pack()
client_id_entry.pack()
details_label.pack()
details_entry.pack()
state_label.pack()
state_entry.pack()
large_image_label.pack()
large_image_entry.pack()
small_image_label.pack()
small_image_entry.pack()
button1_label_label.pack()
button1_label_entry.pack()
button1_url_label.pack()
button1_url_entry.pack()
button2_label_label.pack()
button2_label_entry.pack()
button2_url_label.pack()
button2_url_entry.pack()
start_timestamp_label.pack()
start_timestamp_entry.pack()
end_timestamp_label.pack()
end_timestamp_entry.pack()
party_size_label.pack()
party_size_entry.pack()
party_max_label.pack()
party_max_entry.pack()
update_button.pack()
clear_presence_button.pack()
save_preset_button.pack()
load_preset_button.pack()
login_button.pack()

root.mainloop()