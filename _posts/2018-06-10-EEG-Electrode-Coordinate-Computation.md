---
layout: post
title: "EEG Electrode Coordinate Computation"
date: 2018-06-10
comments: true
categories: Software EEG Neuroscience
---

TL;DR: Check out the [github repository](https://github.com/sappelhoff/eeg_positions)

When recording electroencephalography (EEG) data, electrodes are usually placed according to an international standard. The 10-20, and by extension the 10-10 and 10-05 systems are established sets of rules for this case (see e.g., this [paper](https://www.biosemi.com/publications/pdf/Oostenveld2001b.pdf) for a review).

Even when the actual electrode positions have not been empirically measured during the recording, an approximation of these positions is important for for plotting topographies or visualizing locations of sensors with the help of analysis software.

Standard positions are available in many places such as from [Robert Oostenveld's blog](http://robertoostenveld.nl/electrode/) (who is, by the way,  the main author of that review paper I linked above), or directly from electrode cap manufacturers such as Easycap.

Recently, I wanted to compute there positions myself by pretending the head of a human
was similar to a geometrical sphere and then applying the rules as described in the
blog and paper above. Here, electrode positions on the horizontal and vertical
circumferences on the sphere are quite easily computed by:

1. Counting the number of electrodes along the circumference
2. Dividing the overall angle that is being spanned by that number of
electrodes
3. Using a range of spherical coordinates with the step size obtained in 2. and keeping either the polar or the azimuthal angle constant, depending on whether the horizontal or vertical circumferences are plotted.

More challenging are electrodes, that do not directly lie on the "main circumferences",
because here we would have to very both: the polar angle *and* the azimuthal angle.

It took me a few attempts to get at the correct result and the
intermediate results sometimes looked quite OK (but still false), such as this one,
where I calculated each new electrode position based on midpoints between known electrode positions:

![figure1 of an attempt]({{ site.url }}/assets/2018-06-10/1st_attempt.png)

But at other times, the method I used was completely off. The following picture
shows the electrode positions when each electrode is placed at a fraction
on a Great Arc (arc along a [Great Circle](https://en.wikipedia.org/wiki/Great_circle))

![figure2 of an attempt]({{ site.url }}/assets/2018-06-10/2nd_attempt.png)

Finally, I figured out that the electrodes are placed at fractions along an arc
formed along a "small circle" that is obtained by intersecting the sphere modeling
the human head together with a plane that is formed by three electrodes with known
coordinates.

![figure3 of an attempt]({{ site.url }}/assets/2018-06-10/final_attempt.png)

Two honorable mentions in this regard are an answer on
[StackExchange Mathematics](https://math.stackexchange.com/q/2805204)
and Ed Williams, with whom I had a very helpful exchange. If you work on a similar
problem, you should see his comprehensive
[collection of algorithms and functions](http://edwilliams.org/avform.htm)
to compute positions on a sphere.

All further code and documentation can be found in a [github repository](https://github.com/sappelhoff/eeg_positions).
