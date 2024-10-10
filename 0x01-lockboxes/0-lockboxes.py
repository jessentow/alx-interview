#!/usr/bin/python3
"""This will define a function that determines if a box
    containing a list of lists and can be opened using
    keys stored in the lists
"""


def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""
    location = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or location == 0:
            unlocked[location] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != location:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        location += 1
    return False
