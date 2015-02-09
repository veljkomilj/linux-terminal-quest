#!/usr/bin/env python
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# Author: Caroline Clark <caroline@kano.me>
# A chapter of the story

import os
import sys

dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if __name__ == '__main__' and __package__ is None:
    if dir_path != '/usr':
        sys.path.insert(1, dir_path)

from linux_story.Step import Step

# Change this import statement, need to decide how to group the terminals
# together
from linux_story.challenges.challenge_11.terminals import TerminalMv
from linux_story.challenges.challenge_15.steps import Step1 as NextStep
from linux_story.challenges.challenge_13.steps import Step3 as LoseDogStep
from linux_story.file_data import HIDDEN_DIR


class StepTemplateMv(Step):
    challenge_number = 12

    def __init__(self):
        Step.__init__(self, TerminalMv)


# Thanks you for saving the little girl
class Step1(StepTemplateMv):
    story = [
        "{{wb:Edith:}} Thank you for saving her!",
        "{{wb:Eleanor:}} Doggy!",
        "{{wb:Edith:}} Can you save her dog too?  I'm worried something will "
        "happen to it if it stays outside"
    ]
    start_dir = ".hidden-shelter"
    end_dir = ".hidden-shelter"
    command = "mv ../dog ."
    hints = [
        "{{rn:Use the command}} {{yb:mv ../dog .}}"
    ]
    dog_file = os.path.join(HIDDEN_DIR, 'town/.hidden-shelter/dog')

    def block_command(self, line):
        line = line.strip()
        if ("mv" in line or "cd" in line) and line not in self.command:
            return True

    def next(self):
        if os.path.exists(self.dog_file):
            Step2()
        else:
            LoseDogStep()


# Save both the dog and the little girl
class Step2(StepTemplateMv):
    story = [
        "{{wb:Little girl:}} Yay, Doggie!",
        "{{wb:Dog:}} Ruff.",
        "{{wb:Edith:}} Oh thank goodness you got them both back.",
        "I was wrong about you. You're clearly a good person.\n",
        "{{gb:Awesome!  You're a hero!}}",
        "Talk to everyone and see if there's anything else you can do to "
        "help further"
    ]
    start_dir = ".hidden-shelter"
    end_dir = ".hidden-shelter"
    command = "cat Edward"
    hints = [
        "{{r:Edward looks like he has something he wants to say. "
        "Talk to Edward with}} {{yb:cat}}"
    ]

    def next(self):
        NextStep()
