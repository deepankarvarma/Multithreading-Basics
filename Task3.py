import os
import sys
import time
import random as r
import threading
import tkinter as tk

# Define a task function
def task(lb, ub, refreshTime, displayLabel):
    while True:
        num = r.randint(lb, ub)
        displayLabel.config(text=str(num))
        time.sleep(refreshTime)

# Create the window
window = tk.Tk()
window.title("Dashboard")

# Create the display labels
displayLabels = []
for i in range(6):
    label = tk.Label(window, text="", font=("Helvetica", 36))
    label.grid(row=i, column=0)
    displayLabels.append(label)

# Define the display locations and starting values
displayLocations = ["Location 1", "Location 2", "Location 3", "Location 4", "Location 5", "Location 6"]
startingValues = [(10, 20, 10), (-10, 10, 20), (-100, 0, 8), (0, 20, 12), (-40, 40, 16), (100, 200, 14)]

# Create the threads
threads = []
for i in range(6):
    lb, ub, refreshTime = startingValues[i]
    label = displayLabels[i]
    thread = threading.Thread(target=task, args=(lb, ub, refreshTime, label))
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Start the main loop
window.mainloop()
