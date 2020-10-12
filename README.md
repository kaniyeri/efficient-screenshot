# efficient-screenshot
## Press Ctrl to take screenshots (automatically saved a new folder with a timestamp)
Press Esc to exit.

Requires python libraries keyboard and mss. Run setup.py for automatic install.

Run basic.py and switch to the desired window. Everytime Ctrl is pressed a screenshot will be taken and saved to a folder with the timestamp being the name.
Folder name scheme - [(current date)--(current time)]

Note - The time used is the one at launch of the script, all screenshots taken during a single script launch is saved to ONE folder. This is by design, restart the script to create a new folder for easy categorization.
