import math
import os
import strutils

var
    corner, group, sqRoot : int

var inputValue = parseInt(paramStr(1))

proc nearestCorner(inp: int, sqr: int, cor: int, grp: int): int =
    var turnaround, cSqr : int

    turnaround = int((sqr / 2))

    if grp mod 2 == 0:
        cSqr = sqr + 1
    else:
        cSqr = sqr

    if inp >= grp - turnaround:
        return sqr - (grp - inp)
    elif inp >= cor:
        return cSqr - (inp - (cor))
    elif inp >= cor - turnaround:
        return cSqr - (cor - inp)
    else:
        return sqr - (inp - (cor - sqr))

if inputValue == 1:
    echo 0
elif inputValue < 5:
    echo 1
else:
    sqRoot = int(sqrt(float(inputValue)))

    if sqRoot * sqRoot == inputValue:
        echo sqRoot - 1
    else:
        # in these cases, sqRoot is the floor of the true square root, therefore
        # we need work with the "even" side of the alogrithm if sqRoot is odd
        # and vice versa
        group = (sqRoot + 1) * (sqRoot + 1)
        corner = group - sqRoot
        if sqRoot mod 2 == 0:
            if inputValue == corner:
                echo sqRoot
            else:
                echo nearestCorner(inputValue, sqRoot, corner, group)
        else:
            if inputValue == corner:
                echo sqRoot + 1
            else:
                echo nearestCorner(inputValue, sqRoot, corner, group)
