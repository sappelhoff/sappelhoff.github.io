---
layout: post
title: "PyPrep Preprocessing Pipeline for EEG"
date: 2018-05-01
comments: true
categories: Software EEG Neuroscience
---

PyPrep is my attempt at translating the
["PREP"](https://www.frontiersin.org/articles/10.3389/fninf.2015.00016/full)
(**PRE**processing **P**ipeline) for EEG
data into Python. The original implementation is only
[available in Matlab](https://github.com/VisLab/EEG-Clean-Tools)
and intended for cleaning raw EEG data as a first standardized step before
working with it.

Out of all functionalities that PREP offers, I particularly liked the
["findNoisyChannels"](https://github.com/VisLab/EEG-Clean-Tools/blob/d5289035ad26e773c58fe359c60d9221c4d006d1/PrepPipeline/utilities/findNoisyChannels.m)
function. With it, the EEG data are subjected to several robust tests to tease out
channels that contain noise:

1. Contains n/a values or is flat over an extended period?
2. Abnormal deviations of amplitude i.e., too much or too little?
3. Low correlation with other channels?
4. Not well predicted by other channels? (yes, this is different from 3. see the code)

As mentioned before, with PyPrep there is now a Python implementation of this
function, which works closely with
[MNE-Python](https://www.martinos.org/mne/stable/index.html),
the arguably most popular software package for EEG analysis in Python.


As of May 2018, the "findNoisyChannels" function is the only part of the PREP
that I implemented in Python (contributions welcome!) however, there is one more
thing:

The original PREP does not implement a robust screening of noisy epochs; so I
implemented another function borrowed from
 [FASTER](https://www.sciencedirect.com/science/article/pii/S0165027010003894?via%3Dihub),
 which is yet another preprocessing pipeline for EEG data (they really like their acronyms).

In conclusion, PyPrep currently offers two convenient functions for automatically
cleaning your EEG data in a conservative and robust way.

The code is available on [github](https://github.com/sappelhoff/pyprep) and
[pypi](https://pypi.org/project/pyprep/).
