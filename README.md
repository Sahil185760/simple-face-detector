# Simple Face Detector

A Python command-line tool that detects faces in a still image using OpenCV's Haar cascade classifier. It displays the image with bounding boxes and reports the number of detected faces.

## Features

- Detect multiple faces in a single image.
- Display detections with green bounding boxes.
- Use OpenCV's bundled classifier without a separate model download.
- Process images locally without modifying the source file.

## Requirements

- Python 3.10–3.13
- A graphical desktop environment
- OpenCV, installed using the dependency file below

## Installation

Open a terminal in the project directory and create a virtual environment:

```sh
python -m venv .venv
```

Activate it on macOS or Linux:

```sh
source .venv/bin/activate
```

On Windows Command Prompt:

```bat
.venv\Scripts\activate
```

Install the dependency:

```sh
python -m pip install -r requirements.txt
```

On systems where Python is available as `python3`, use `python3` to create the virtual environment.

## Usage

```sh
python face_detector.py "path/to/photo.jpg"
```

Replace the path with an existing image. Quote paths containing spaces. Relative paths are resolved from the terminal's current directory.

Example terminal output:

```text
Faces detected: 3
```

The image opens in a separate window. Focus that window and press any key to close it. If no faces are detected, the count is zero and the image appears without bounding boxes.

Show command-line help:

```sh
python face_detector.py --help
```

## Detection approach

The program loads the image, converts it to grayscale, and applies OpenCV's bundled `haarcascade_frontalface_default.xml` classifier. Each detected region is drawn on the displayed image.

| Parameter | Value | Purpose |
| --- | --- | --- |
| `scaleFactor` | `1.1` | Controls the image scale reduction between detection passes. |
| `minNeighbors` | `5` | Filters candidate detections based on neighboring matches. |
| `minSize` | `(30, 30)` | Sets the minimum face size in pixels. |

## Project structure

```text
simple-face-detector/
├── face_detector.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Limitations

The classifier works best with clear, front-facing faces. Small, tilted, obscured, or poorly lit faces may be missed, and some objects may be incorrectly detected. The program locates faces; it does not identify people.

## Troubleshooting

- **Image cannot be read:** Check that the path exists and points to a supported, readable image.
- **Image window does not open:** Run on a graphical desktop. Remote terminals, headless servers, and hosted notebooks may not support the display window. Install `opencv-python`, not `opencv-python-headless`.
- **Classifier cannot be loaded:** Reinstall the dependency in the project's virtual environment.

## Project history

Originally developed on November 10, 2025. This repository contains a reconstruction created after the original source files were lost.

## Acknowledgments

This project was led by Sahil Harlalka as part of his school's Programming Club.
