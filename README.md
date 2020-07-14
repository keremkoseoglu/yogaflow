# YogaFlow

This is a random yoga flow generator, written in Python.

![Screenshot](screenshot.png)

## Installation

### OS independent

* Install Python First. The program won't work unless you install Python.  [Click here](https://www.python.org/downloads/mac-osx/) to install Python. [The official Python docs](https://docs.python.org/3/using/mac.html) are good enough to help you through the installation.

* Create a folder (presumably called yogaflow), and download all of the files in this repository there

* Open a terminal window, go to the yogaflow folder and type the following commands:

```
python3 -m venv venv
```

## Usage

### Windows

Simply run main.py. You can run main.py from the command line by typing:

```
cd yogaflow
venv\Scripts\activate.bat
python3 main.py
```

Obviously, you should change the folder name yogaflow with your own installation path. Feel free to create a .bat file including this command for easy startup.

### Mac / Linux

Simply run main.py. You can run main.py from the command line by typing:

```
cd yogaflow
. venv/bin/activate
python3 main.py
```

Obviously, you should change the folder name yogaflow with your own installation path. Feel free to create a .sh file including this command for easy startup.

## Customization

You can customize content by editing the simple & intuitive JSON files under /data.