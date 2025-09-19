
# Simple Mac inspired widge that tells you cpu/swap/load on the computer I use when developing sometimes.
Test on a M4 Mac 48gb ram I didnt make this for low end computers
Shouldnt use more then 2-4gb ram tho, id say less. 


This is a Devlopers Widget for people who do machine learning or projects where you may use alot of swap or cpu use you need to moniter. This app will tell you vocally when you reach a certain amount of swap to shut down to save SSD. No need to check activity monitor. 

**I have not tested on windows** or unit tested thoughly.  **I just use to montor swap safely while doing heavy tasks so I dont have to contantly run task mangager which uses alot of data/cpu and wakes up deamons etc on MAC*


# Memory Management Monitor (macOS)

A lightweight Python utility for tracking system memory, CPU, swap, load averages, and GPU VRAM usage on macOS. Logs diagnostics to the Desktop for easy performance review!


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





# Architect of the UI design and Custom Features
•   Developed custom diagnostics tool, UI, and maintained by Justin Guida (@justinguida941)
 	--Utilizing ***psutil***
  
•   Tested on macOS 14 (M4 chip) 48 GB RAM.
 	-Not sure if this is windows compatable
  
•   ***Compatible with Python 3.10+***




# License

**Evaluation only — all rights reserved.**

You may **clone and run locally** for personal or hiring evaluation.  
You may **not** redistribute, sublicense, or use this work commercially without my written permission.

See the [LICENSE](LICENSE) file for the exact terms.

**Qt note:** This app uses **PyQt6 (GPLv3)**. Do **not** redistribute the app unless you comply with GPLv3 or have a Qt commercial license.


# Roadmap

The additions will support:

- **QColorDialog**: For your UI editor's color selection

- **QIcon, QPainter, QPen, QPixmap**: For custom drawing like the traffic light buttons - Need to put in right place
 
- **json**: To save/load UI customization settings
  
- **Matplotlibs** for 2D graphing, and **3d Graphing using other libraries to visualize system usage.**
  
- **Tempature, Heatmaps, Network Traffic***

