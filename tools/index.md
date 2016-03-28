---
title: Tools
permalink: /tools/
---

For further information and to download, please follow the links below.

## [characters.py](/tools/characters.py)

A little Python 3 script we created that fetches a Shakespeare play from
<http://shakespeare.mit.edu/> and outputs a CSV table with the times each
character appears. It takes into account when characters enter and exit the
stage and it can be used to determine when characters meet each other.

    $ python3 characters.py http://shakespeare.mit.edu/twelfth_night/full.html
    time,character
    0,CURIO
    0,DUKE ORSINO
    1,VALENTINE
    1,CURIO
    1,DUKE ORSINO
    3,VIOLA
    6,SIR ANDREW
    …

*[CSV table]: Comma Separated Values table or spreadsheet

## [Vocabalance](https://gitlab.sphalerite.org/linus/vocabalance/)

A tool that analyses the frequency with which each character uses a word,
generating a “significance index” based on:

 - How often the character uses the word
 - How often the character speaks overall
 - How often other characters use the word

We used this to perform in-depth analysis of characters on [Richard
II](/analyses/richard-ii).


## [AntConc](http://www.laurenceanthony.net/software/antconc/)

A freeware text analysis toolkit for concordancing and text analysis. Can be used to:

- Search for individual words in an individual play or corpus of plays
- Make concordance plots
- View n-grams

## [WordHoard](http://wordhoard.northwestern.edu/)

An application for the close reading and scholarly analysis of texts, largely
used on this project for determining the log-likelihoods of specific words and
generating word clouds to display this information in a user-friendly manner.

## [Ubiqu+ity](http://vep.cs.wisc.edu/ubiq/)

Generates statistics and identifies linguistic patterns and groups.

