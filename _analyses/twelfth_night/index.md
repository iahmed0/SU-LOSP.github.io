---
title: Twelfth Night
permalink: /analyses/twelfth_night/
read_play: http://shakespeare.mit.edu/twelfth_night/full.html
---


# Character interaction

The interaction between characters plays a central role in this play.
Information about the structure of the play and insight into its plot itself can
be extracted by computing when main characters meet each other on stage.

Using a [tagged version of the
play](http://shakespeare.mit.edu/twelfth_night/full.html) and
[characters.py](/tools/), we parsed events like `Enter`s and `Exit`s and
computed which characters were on stage at any given time. In this chart
characters appear as columns and time goes by vertically downwards:

<figure>
    <img alt="Character interactions" src="interactions.png" />
</figure>

With this information and a basic understanding of the play, we can see how the
interaction between characters highlights different characteristics of the play.

One example are the appearances of Sir Andrew Aguecheek and Sir Toby Belch. Sir
Andrew, with a single exception, always appears on stage with Sir Toby, and
often enters after or leaves before him. Sir Toby is more dominant as a
character in terms of driving the action forward, while Sir Andrew is more of a
counterpoint to Sir Toby.

It is noticeable too how Duke Orsino, decisive to the play's argument, doesn't
appear very often.

We can also see how the appearances of Viola and Toby, each on a different
subplot, interleave prior to Act 3, when both subplots meet.
