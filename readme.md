# Overview

It is good to study in groups; getting asked questions, asking questions and in general testing understanding is conducive to learning. However, it is hard to organize reading groups, especially when the topic is very specific.

The goal of this repository is to organize such groups and then as a side-effect of meeting we can collaboratively document our process, making it easier for others to get started.


# Getting started

The basic idea is to use github issues for suggesting papers to read (as well as organizing meeting dates and meta-comments such as improving this document or the structure of our collaboration etc.) 

The actual meetings manifest themselves as pull requests; first, the concrete decisions made in the issue are collected into a readme (and the canonical version of the paper is added as well). Then, once the meeting takes place, any artefacts from the meeting can be collected into the PR.

Normally the issue can be closed once the pull request has been opened since it means that the readme is almost ready (and the focus is always anchored to a readme).



## How to host a meeting

Basic idea:

- Create an issue for the paper you want to read, once interest develops some decisions will be made.
  - When to meet.
  - Precondition(s) for participation (if any).
  - Goal(s) (if any).
  - Communication channels for bootstrapping meetings and general async communication (IRC, email, scuttlebutt, activitypub, matrix).
  - Tools to communicate during meeting:  drawpile, mumble and codimd are good tools (annotate pdfs, while talking and writing notes with latex - all synchronous).
  - Staking or some other way to signal commitment can also be agreed on but should not be needed in most cases.
- Then create a pull request for the meeting, the pull request should have a folder with:
  - The paper
  - Ideally a shell.nix with all communication software preconfigured
  - A readme that explains the format of the meeting, technical howto (joining etc.), lists participants or requirements for participation and in general serves as the authoritative document for decisions made in the issue that spawned the pull request.
- When the meeting is finished you can add the annotated paper and any notes or images that were produced over the meeting to the pull request.

If you already have a group or are just going to be reading the paper no matter what then you can skip straight to making a pull request with your decisions (among which must be information for joining).

For recurring meetings a format like this can be used:
```
Paper                    -- name of paper
├── paper.pdf            -- The paper
├── shell.nix            -- The necessary software to participate
├── readme.md            -- The decisions mentioned above
├── group-meeting1       -- A directory containing a readme with e.g. goals and then meeting artefacts
└── group-meeting2       -- group is some arbitrary id, allows many groups to discuss the same paper concurrently
```

Of course you are free to deviate from this structure but please document your process and treat the readme like a constitution (respecting "higher" readmes). This makes it easier for others to benefit from your ideas.

### Merging Pull Requests

I had a cheeky idea to merge when goals are met (in line with the scientific method, predefine conditions for failure so that the experiment can be unbiased). The group would come up with the goals themselves and merging is the "job well done" ceremony. If you don't have any goals for the meeting then merging can be done at any time.

## How to participate

Just make an issue or join a group that meets publicly.

Some groups may use email or something similar to keep joining details private - while leaving the artefacts and organization public (by committing them to this repo). This is totally fine since it's important to keep everyone on the same page and momentum may be lost when bringing in new people.

However don't let this discourage you from opening an issue, maybe those same people will be willing to participate in other new groups.

### Adding a Profile

Make a pull request adding a folder to `profiles/`
```
Profile                  -- your pseudonym / real name
├── readme.md            -- an introduction with relevant details to reading CS papers.
└── wishlist1.md         -- a list of papers you'd like to read or topics you want to study.
```
You can also put the wishlists in the readme but it can be easier to manage when you have different files for different topics.

Feel free to sign your readme and include a public key in your profile folder.


# Inspiration

Communities

- https://paperswelove.org/

If you are looking for a place to start then here are some places that aggregate papers about haskell and type theory:

- ##dependent on freenode, their repo: https://github.com/dpndnt/library
- https://github.com/cohomolo-gy/haskell-resources
- https://mitchellwrosen.github.io/haskell-papers/
- https://github.com/beerendlauwers/haskell-papers-ereader
- https://wiki.haskell.org/Research_papers
- distributed systems: https://heather.miller.am/teaching/cs7680/

