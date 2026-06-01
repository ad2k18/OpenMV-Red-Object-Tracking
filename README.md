# OpenMV-Red-Object-Tracking
Real-time red object detection and tracking using OpenMV and Python.
# OpenMV Red Object Tracking

## Project Summary

Real-time computer vision system for object detection and tracking using OpenMV camera and Python.

## Overview

This project implements a real-time computer vision system using an OpenMV camera and Python.

The system detects red objects within the camera frame, calculates their position, and outputs bounding box and center coordinates. The project was developed as part of the Cyber Physical Systems module at Technische Universität Berlin.

## Features

- Real-time object detection
- Color-based segmentation
- Bounding box visualization
- Center coordinate calculation
- Real-time coordinate output
- Embedded computer vision processing

## Technologies

- Python
- OpenMV
- Computer Vision
- Embedded Systems
- Image Processing

## System Demo

The system runs in real-time on an OpenMV camera and detects red objects within the camera frame.

Detected objects are highlighted with bounding boxes and their center coordinates are printed in real-time output.

## Expected Behavior

- The camera detects red-colored objects in the scene
- A bounding box is drawn around detected objects
- The center coordinates are continuously printed
- The system operates in real-time with stable FPS

## How It Works

The OpenMV camera continuously captures frames and detects red-colored objects using a predefined LAB color threshold.

For each detected object, the system:

1. Detects the object in the image
2. Draws a bounding box around it
3. Computes the center coordinates
4. Outputs position data (X, Y, width, height, center)

This output can be used for robotic systems or further processing (e.g. ROS integration).


## Example Output
BOX: 120 80 45 50 CENTER: 142 105


## Learning Outcomes

Through this project, I gained practical experience in:

- Real-time computer vision
- Object detection techniques
- Embedded systems programming
- Sensor-based image processing
- Robotics-oriented data output
- Integration of vision systems into cyber-physical systems

## Author

Arsam Dilmaghani  
Bachelor of Science in Computer Science  
Technische Universität Berlin


