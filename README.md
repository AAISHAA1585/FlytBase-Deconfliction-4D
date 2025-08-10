FlytBase Drone Deconfliction System
A strategic deconfliction system that validates a drone's planned mission for spatio-temporal conflicts in shared airspace. This project was developed as part of the FlytBase internship assignment, focusing on robust and scalable flight path analysis.

---

Key Features


1]4D Spatio-Temporal Deconfliction: The system precisely checks for conflicts in 3D space (x, y, z) over time, a core requirement of the project's extra credit.

2]Modular Architecture: The codebase is logically organized into dedicated modules for data handling, path generation, conflict detection, and visualization, making it scalable and easy to maintain.

3]Dynamic 4D Visualization: A high-quality animated GIF is generated to visually represent the drone missions. This includes showing drones as moving points, dynamically drawing their flight paths, and clearly marking any conflict zones with a prominent red sphere and a red cross.

4]Robust Input Handling: Mission data for all drones is read from simple, human-readable JSON files, with built-in validation to handle potential errors in the input data.



## 2. Folder structure

flytbase_deconfliction/
│
├── run_deconflict.py # Main script
├── requirements.txt # Libraries needed
├── README.md # This file
│
├── deconflict/ # Code files
│ ├── io.py # Reads JSON input
│ ├── trajectory.py # Calculates positions
│ ├── detector.py # Checks conflicts
│ ├── visualizer.py # Draws and animates drones
│ ├── utils.py # (Optional) helper functions
│
├── scenarios/ # Input data
│ ├── primary.json
│ ├── others.json
│
├── demo/ # Output animations
│ ├── conflict_animation.gif
│
└── docs/ # Extra documents
├── reflection.pdf


Setup Instructions
To get this project up and running on your local machine, follow these simple steps.

Prerequisites
Python 3.x: Ensure you have a compatible version of Python installed.

Git: Required to clone the repository.

1. Install dependencies
Navigate to the project's root directory in your terminal and install the required Python libraries.

pip install -r requirements.txt

2. Run the simulation
Execute the main script from the same directory.

python run_deconflict.py

 "Animation Output":

 ### Animation Output

A dynamic 4D visualization of the drone missions and detected conflicts.

<p align="center">
  <img src="demo/conflict_animation.gif" alt="4D Deconfliction Simulation">
</p>

"Console Report":

### Console Report

The terminal output provides a detailed report of any detected conflicts, including the time and location.

<p align="center">
  <img src="docs/console_output_screenshot.png" alt="Conflict Report in Terminal" width="80%">
</p>