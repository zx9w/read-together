---
name: Suggest Paper
about: Optional structure for making a paper suggestion
title: PAPER NAME [TZ]
labels: paper
assignees: ''

---

# Introduction

Paper name, link and small overview of the domain and requisite knowledge (disjoint with abstract).
When are you available?
What is your rough aptitude or understanding?

## Abstract

Paste here

## Idea

What is the idea behind reading this paper?
How do you want to approach the paper?
What is the scope of the study of this paper? are we reading adjacent papers?
More concretely; what is the goal of this study group? what kind of artifacts would you like to produce? (e.g. annotated paper, latex notes, simple implementations, etc.) TODO: parameterize this space.

# Politics

Here you can express your preference on how to organize, relevant subjects include:

- Asynchronous persistent channel :: Decide on a way to communicate persistently in order to bootstrap synchronous sessions and facilitate organization. Make sure that there is a total order (Foreground = Availability > Consistency = Fallback), common options: irc, email, this github forum..
- Synchronous ephemeral channels :: Tools used to coordinate during meeting, common options: mumble, drawpile, jitsi, codiMD, etc.
- Prerequisites for participation :: Homework? Background? Test? Staking / collateral? This is your option for supply demand, this will probably never be an issue :)
- Postcondition (for merging) :: If you want a witness (me) to observe that you reach a goal then you can specify completion/failure conditions.
