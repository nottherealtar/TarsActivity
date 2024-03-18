# Discord Rich Presence GUI
This is a simple GUI application for setting a custom Discord Rich Presence status. It's built with Python and uses the pypresence library to interact with Discord, and tkinter for the GUI.

## Features
Set a custom Discord Rich Presence status with various options (details, state, images, buttons, timestamps, party size)
Validate URLs for buttons
Save and load presets
Login with a specific client ID

### Usage
Run the script: python RichPresence.py
Enter your client ID and other details for your rich presence status
Click "Update Presence" to set your status
You can also save your current inputs as a preset by clicking "Save Preset", and load them back later with "Load Preset"
To clear your status, click "Clear Presence"

#### Requirements
_Python 3_
- `pypresence` library (`pip install pypresence`)

- `validators library` (`pip install validators`)

- `tkinter library` (`comes pre-installed with Python`)

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
