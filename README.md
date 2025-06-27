
This is a Devlopers Widget for people who do machine learning or projects where you may use alot of swap or cpu use you need to moniter. This app will tell you vocally when you reach a certain amount of swap to shut down to save SSD. No need to check activity monitor. 

# Simple Mac inspired widge that tells you cpu/swap/load on the computer I use when developing sometimes.
Test on a M4 Mac 48gb ram I didnt make this for low end computers
Shouldnt use more then 2-4gb ram tho, id say less. 
**I have not tested on windows** or unit tested thoughly.  **I just use to montor swap safely while doing heavy tasks so I dont have to contantly run task mangage wake up deamons etc on mac**


# Memory Management Monitor (macOS)

A lightweight Python utility for tracking system memory, CPU, swap, load averages, and GPU VRAM usage on macOS. Logs diagnostics to the Desktop for easy performance review.


# Features

•  Logs system stats every 10 seconds

•  Captures:

•  Total, used, and available RAM

•  Swap memory usage

•  CPU usage percentage

 ***PYQT6 Transparent UI to show metrics***
 
•  Load averages (1, 5, and 15 minutes)

•  macOS GPU VRAM details using system_profiler

• Runs silently as .pyw (no terminal window)

•  Writes to ~/Desktop/memory_log.txt for diagnostics. 


# Dependencies

***Core functionality***

pip install PyQt6

pip install psutil

# For multimedia support (sounds)

pip install PyQt6-Qt6

For Future Updates: If you want charting capabilities:
pip install PyQt6-Charts

# Optional but useful for certain system integrations

pip install darkdetect

Or Refer tot the full requirements.txt

***Found inside the the extended system monitor version if needed.***


# Usage

***Run directly***

PYQT6 UI Displays CPU, GPU, 1,5,15 Load Averages.

To check text log: python check_memory.pyw

Or double-click the .pyw file on desktop.



# License

-This project is licensed under the BSD 3-Clause License.

-It includes components under compatible open source terms.

-Great libraries like psutil are used to gather system information.

-Thanks to the psutil authors for their work, I am NOT endorsed by them

-just giving them credit where credit is due.



# Architect of the UI design and Custom Features
•   Developed custom diagnostics tool, UI, and maintained by Justin Guida (@justinguida941)
 	--Utilizing ***psutil***
  
•   Tested on macOS 14 (M4 chip) 48 GB RAM.
 	-Not sure if this is windows compatable
  
•   ***Compatible with Python 3.10+***




# BSD 3-Clause License:
Created by Justin Gudida. May - 2025. Use it all your want. Never fully finished this just gotta change buttons locations/polish it up a bit.



# Roadmap

The additions will support:

- **QColorDialog**: For your UI editor's color selection

- **QIcon, QPainter, QPen, QPixmap**: For custom drawing like the traffic light buttons - Need to put in right place
 
- **json**: To save/load UI customization settings
  
- **Matplotlibs** for 2D graphing, and **3d Graphing using other libraries to visualize system usage.**
  
- **Tempature, Heatmaps, Network Traffic***

