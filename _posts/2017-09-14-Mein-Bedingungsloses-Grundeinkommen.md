---
layout: post
title: "Mein Bedingungsloses Grundeinkommen"
date: 2017-09-14
comments: true
categories: German Basic-Income Probability
---

Schonmal von Mein-Grundeinkommen gehört? Interesse, ein Grundeinkommen zu gewinnen? Dann ist das hier vielleicht interessant - ein Grundeinkommen mal ausprobieren anstatt nur darüber zu diskutieren. :-)

[Mein-Grundeinkommen](https://www.mein-grundeinkommen.de) ist eine Organisation, die (wer hätte es gedacht) [bedingungslose Grundeinkommen](https://de.wikipedia.org/wiki/Bedingungsloses_Grundeinkommen) verlost. Zur Zeit gibt es eine besondere Tandem-Aktion, bei der man zwischen 0 und 100 Partner sammeln kann. Bei einem Gewinn der Lotterie wird unter den Partnern des Gewinners ein weiteres Grundeinkommen verlost. Man hat also zwei Gewinnchancen, sobald man mehr als 0 Partner hat. Das ganze kann man auch schön aufmalen und die Wahrscheinlichkeiten ausrechnen:


N = Anzahl Teilnehmer

M = Anzahl Partner

K = Anzahl Partner der Partner

```
      ---> Gewonnen
     /
    / 1/N            ---> Gewonnen
   /                /
  /                / 1/K
 /   M/N          /
* ---------------*
 \                \
  \                \ (K-1)/K
   \                \
    \ (N-(M+1))/N    ---> Verloren
     \
      ---> Verloren
```

Die beim [Baumdiagramm](https://de.wikipedia.org/wiki/Baumdiagramm) aufgezeichneten Wahrscheinlichkeiten ergeben sich direkt aus den Regeln von der Organisation Mein-Grundeinkommen:

- Man hat eine geringe Chance, direkt zu gewinnen (1/N) ...
- ... und eine hohe Chance überhaupt nicht zu gewinnen (N-(M+1))/N)
- Spannend ist der Fall, wenn einer der eigenen Partner gewinnt (M/N) ...
- ... denn dann hat man nochmals eine Chance unter den Partnern des Partners ausgewählt zu werden (1/K) ...
- ... oder eben nicht ((K-1)/K).

Aus diesem Baumdiagramm können wir jetzt die Gewinnchancen errechnen, indem wir den [Multiplikationssatz](https://de.wikipedia.org/wiki/Bedingte_Wahrscheinlichkeit#Multiplikationssatz) verwenden: P(A und B) = P(A gegeben B) * P(B)

Danach kann man die "Gewonnen" und "Verloren" Äste addieren und wenn man dann auch noch auf eine Gesamtwahrscheinlichkeit von 1 kommt, ist die Sache fast geritzt. Fast? Ja - denn wir müssen noch einberechnen, dass mehr als nur EIN Grundeinkommen verlost wird. Wir müssen also die Wahrscheinlichkeit, dass mindestens ein Mal gewonnen wird berechnen. Dazu rechnen wir einfach 1 - die Wahrscheinlichkeit, dass nie gewonnen wird. Also 1 - p(verlust)^nGrundeinkommen. Wobei nGrundeinkommen die Anzahl an zu verlosenden Grundeinkommen ist.

Jetzt müssen wir uns nur noch auf ein paar Zahlen festlegen: N, M, K, und nGrundeinkommen.

Wir (über)schätzen grob, dass 1 Million Teilnehmer bei der nächsten Verlosung mitmachen (N), man selbst 100 Partner hat (M), und dass diese 100 Partner im Schnitt selbst je 50 Partner haben (K). Außerdem gehen wir davon aus, dass 12 Grundeinkommen verlost werden (nGrundeinkommen).


Ich habe das ganze mal in Python programmiert (siehe [hier](https://github.com/sappelhoff/meinbge)) und präsentiere hiermit ein paar interessante Plots (basierend auf unseren geschätzten N, M, K, und nGrundeinkommen).

-----

![pretty figure]({{ site.url }}/assets/gewinn_partner.jpg)

... Damit man es besser vergleichen kann habe ich auch noch die Wahrscheinlichkeiten eingefügt, wenn man 6 oder 7 mal in Folge mit einem Würfel eine Sechs würfeln möchte.

-----

![pretty figure]({{ site.url }}/assets/gewinn_contour.jpg)

... Die y-Achse ist hier für bessere Lesbarkeit des Plots im logarithmus angegeben (von 1 bis 100).

-----

Lange Rede kurzer Sinn. Es ist gut, viele Partner zu haben ... und noch besser ist es, wenn diese Partner nur dich als Partner haben. :-)

Achja ... und je nachdem wie sinnvoll die Schätzung von N, M, K, und nGrundeinkommen war stehen die Chancen sogar relativ günstig, ein Grundeinkommen zu gewinnen.

Viel Glück!
