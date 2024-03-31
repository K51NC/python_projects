# Password Manager

## Description

### **How to use**

Fill in all fields with appropriate information. Select the `Generate` button to create a password. Select the `Save` button to store the password. When you select the `Generate` button, the password will be copied to the clipboard.

## Installation Instructions

* Install `pyperclip` module.
* Run the `main.py` file.

## Dev Log

### 3-28-2024

New concepts im using in this project:

* more `tkinter`
  * `columnspan`
  * clearing `Entry` fields
  * `messagebox`
* `pyperclip`

Additional notes:

`Tkinter` documentation is not the best. Again, I was able to do most of it on my own, but there are things that ended up wasting my time rather than teaching me new things. Regardless, I learning a lot with this one and I might head back over to the `018_POMODORO` project to add a popup window for the break time so I stop missing it.

### 3-30-2024

Returned to this project to officially learn about `json` file manipulation. Additionally, this section included some error handling and exception catching. I also added a search functionality to the password manager and moved my constants to a separate file. I did almost all of this part before watching anything in the section because I feel like we have already covered most of this in the previous sections.

Side note: If the JSON file is empty, it throws a `json.JSONDecodeError`. While the file should never be empty, this error can still occur if something weird happens, like a misplaced comma etc. I basically tell the user that they either lost all their passwords or they can figure out how to correct the error in the database on their own. I would like a way to handle this better in the future. One thing the course instructor mentioned was to only use exceptions when you can't handle the situation with an `if` statement. I went overboard with the exceptions in this project, but I wanted to learn how to use them. As an example, I could have used an `if/else` statement to check for the key instead of using an exception to catch the error.

### **Flow Chart**

### **Future Updates**

* better way to handle JSON file read errors (e.g. empty file)

### **To-Do List for Next Working Version**

### **Bugs**
