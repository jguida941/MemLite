You’re absolutely right — per the BSD 3-Clause License:

“Neither the name of the psutil authors nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.”

To comply fully, here’s your revised README.md with that line removed:



Memory Management Monitor (macOS)

A lightweight Python utility for tracking system memory, CPU, swap, load averages, and GPU VRAM usage on macOS. Logs diagnostics to the Desktop for easy performance review.



Features
	•	Logs system stats every 10 seconds
	•	Captures:
	•	Total, used, and available RAM
	•	Swap memory usage
	•	CPU usage percentage
	•	Load averages (1, 5, and 15 minutes)
	•	macOS GPU VRAM details using system_profiler
	•	Runs silently as .pyw (no terminal window)
	•	Writes to ~/Desktop/memory_log.txt



Dependencies

Only psutil is required beyond the standard library.

Install with:

pip install psutil

Or refer to the full requirements.txt from the extended system monitor version if needed.



Usage

Run directly:

python check_memory.pyw

Or double-click the .pyw file on supported systems.



License

This project is licensed under the BSD 3-Clause License.
It includes components under compatible open source terms.
Great libraries like psutil are used to gather system information.
Thanks to the psutil authors for their work.



Maintainer
	•	Developed and maintained by Justin Guida (@justinguida941)
	•	Tested on macOS 14 (M4 chip) 48 GB RAM
	•	Compatible with Python 3.10+



Roadmap
	•	Optional menu bar interface
	•	Idle-state auto-pausing
	•	GUI control panel
	•	Configurable log rotation
