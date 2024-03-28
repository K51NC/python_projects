# Pomodoro

## Description

### **How to use**

Hit `Start` to start the timer. Hit `Reset` to reset the timer. After 25 minutes, a window will pop up to remind you to take a 5 minute break. After 4 pomodoros, take a 20 minute break.

## Installation Instructions

None. Just run the `main.py` file.

## Dev Log

### 3-27-2024

New concepts im using in this project:

* timer functionality (`after()` and `after_cancel()` methods)
* dynamic typing

Additional notes:

First decent assignment with `tkinter`. This will be the first app that I believe I will be able to use in my daily life. This will also motivate me to improve and tailor the app to my liking. I am excited to see how it turns out and what ideas I will eventually come up with to improve it in the future.

Update after section:

Not going to lie, that was easy yet difficult. `Tkinter` documentation is not the best so I had to rely on a lot on the 100 Days of Code course to guide me on this one. I was still able to do quite a bit of it on my own, but little things like the `after()` method and `after_cancel()` method were something I had no clue about and both were necessary to complete this project. Regardless, I learned a LOT about `Tkinter`.

### 3-28-2024

Added a few ideas for the future in the README (below). Changed the timer to stop after one cycle of pomodoros (4 cycles of 25 minutes). You now have to manually start the next set of pomodoros. This is just a personal preference so I can start using the app until I add more features later.

Added a popup to notify you of your break time. I kept missing it so I added a popup to remind me to take a break.

Added a water icon to remind myself to drink. This feature reminds me to drink water after every "X" number of minutes (hardcoded in the program for now). Click the water icon to reset the timer. Also have it clearing my background `powershell` screen with the `cls` command to show how long is left on the water timer. This is just a personal thing and you can remove it if you want.

### **Flow Chart**

### **Future Updates**

* add timer adjustments for longer or shorter work periods
* make window pop-up alert and/or sounds optional
* add pause button
* Task integration
  * Manual entry to local or online database
  * Separate Google calendar tasks
  * Other to-do list apps
* Adjustable pomodoro lengths
* Task length and priority
  * Optionally set automatic daily pomodoros
* Easy to use menu to swap out tasks
* create an app for mobile devices

### **To-Do List for Next Working Version**

### **Bugs**
