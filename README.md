
# Push-Up Counter

Our goal was to design and build a Python program that can analyze and count the number of push-ups taken and display it in a monitor.The program reads out the total number of push-ups taken and creates a leader-board which stores the top 5 push up scores. 

We used Python libraries like OpenCv and Mediapipe for this project. The OpenCv library was used to capture images frame by frame from the webcam and the Mediapipe libray  to find the position of the different landmarks on the human body.  To develop the interactive user interface we used Tkinter library from Python.

The program tracks the movement of the shoulders relative to the elbow and increments the count every time they reach the same level.

Our application is expected to make fitness more enjoyable by making it competitive.


## Important

Don't Use Space or press return key while Entering Name of People only use Enter button given

Needed fix on that :) 

## Run in Linux

After Installation

Start Leaderboard by

```bash
  ./board.sh
```
In another terminal,
Start the pushup-counter by

```bash
  ./push.sh
```
#### Alternate Method

set permission of files "board.sh" and "push.sh" as "Allow executing file as a program"

right click board.sh and click "Run as a program"

right click push.sh and click "Run as a program"

## Run in Other OS

run lead.py

run pcounter.py
## Installation
Clone the project

```bash
  git clone https://github.com/inamurahman/pushup-counter.git
```

Go to the project directory

```bash
  cd pushup-counter
```

#### Install requirements

Tkinter

opencv

mediapipe

pillow (PIL)


## Features

- Live previews
- Fullscreen mode
- Cross platform
- Live Highscores (upto 5)

## Photos

![IMG-20221205-WA0006](https://user-images.githubusercontent.com/96386836/206923517-8da82d05-eb5e-423d-9a6d-da1a8655f1f1.jpg)

![IMG-20221205-WA0010](https://user-images.githubusercontent.com/96386836/206923472-cd6ffce1-abd0-45c1-9cc0-cbc4c235a670.jpg)



