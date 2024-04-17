#!/usr/bin/python3
"""Script contains the method canUnlockAll"""


def canUnlockAll(boxes):
    """ Method returns True if all boxes can be opened,
    else returns False
    """

    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True
