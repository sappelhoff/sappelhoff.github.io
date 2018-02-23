---
layout: post
title: "Triggers with Psychopy on Brainvision Recorder"
date: 2017-11-23
comments: true
categories: mixed
---

## Problem
You want to set up your BrainProducts EEG System (BrainAmp) to receive triggers via the parallel port on **Windows**.

For that, you want to use Python.

(If you want to use Matlab, see [here](http://apps.usd.edu/coglab/psyc770/IO64.html))

## General Information

Parallel ports are hardware ports that are also called LPT ports.

LPT = ["**L**ine **P**rint **T**erminal", "**L**ocal **P**rint **T**erminal", or "**L**ine **P**rin**T**er"](https://en.wikipedia.org/wiki/Parallel_port#Access)

Common port addresses for [Windows](https://en.wikipedia.org/wiki/Parallel_port#Port_addresses):
```
LPT1 = 0x0378 or 0x03BC
LPT2 = 0x0278 or 0x0378
LPT3 = 0x0278
```

For completeness, these would be common addresses for Linux:
```
LPT1 = /dev/parport0
LPT2 = /dev/parport1
LPT3 = /dev/parport2
```


## Possible Solution 1
We will use Python ([psychopy](http://psychopy.org)) to send triggers.

### Requirements

- BrainProducts' BrainAmp set up and connected to the parallel port of your computer
- BrainVision Recorder running on monitor mode
- [*Inpout32*](http://www.highrez.co.uk/downloads/inpout32/) (for Windows)
- [Python 2.7.14](https://www.python.org/downloads/) (or newer)

### Instructions (Windows)
Open a Windows shell.

Prepare a virtual environment:

    python -m pip install virtualenv
    python -m virtualenv C:\psychopy_env

To activate or deactivate the virtual environment:

    C:\psychopy_env\Scripts\activate
    C:\psychopy_env\Scripts\dectivate

We use psychopy. So activate your virtual environment and run:


    python -m pip install pypiwin32 numpy scipy matplotlib pandas pyopengl
    python -m pip install pyglet pillow moviepy lxml openpyxl configobj psychopy


Once everything has been installed, you can try out the most common parallel port addresses. Copy the following code into a file and run it. At this point, you should have your BrainVision Recorder running in monitor mode. Stare at the screen to check whether markers are coming up:

``` python

from psychopy import parallel as p
import time


p_port1 = p.ParallelPort(address=0x03BC)
p_port2 = p.ParallelPort(address=0x0378)
p_port3 = p.ParallelPort(address=0x0278)
p_port4 = p.ParallelPort(address=0x3010) # this worked for me once ...


p_ports = [p_port1, p_port2, p_port3, p_port4]
for i, p_port in enumerate(p_ports):
    p_port.setData(0)
    time.sleep(1)
    p_port.setData(i+1)

```

If a marker shows up, note down the corresponding parallel port address.

If you were unlucky and you did not see any markers, see below:


## Possible Solution 2
In case non of the above addresses work, you might have to use a different parallel port address.

Check out the [Parallel-Port-Tester](https://www.downtowndougbrown.com/2013/06/parallel-port-tester/), which might yield some hints for the address.
