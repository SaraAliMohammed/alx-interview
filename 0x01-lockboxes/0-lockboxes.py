#!/usr/bin/python3
''' Locked box challenge '''


def canUnlockAll(boxes):
    ''' Determines if all the boxes can be opened.

        Arguments:
        boxes (list): list of lists representing boxes and any keys inside.

        Returns: True if all boxes can be opened, else return False
    '''
    if type(boxes) is not list or len(boxes) < 1:
        return False
    for box in boxes:
        if type(box) is not list:
            return False
    keys = {0}
    size = len(boxes)
    visited = {0}
    keys = keys.union(boxes[0])
    while size > 0:
        for i in keys:
            if i in visited:
                continue
            keys = keys.union(boxes[i])
            visited.add(i)
        size -= 1
    return len(keys) == len(boxes)
