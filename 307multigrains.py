#!/usr/bin/env python3

import sys
from store import *


def matrix_square(n,p):
    deb = [5, 6, 7, 8]
    squash = [
        [1, 0, 1, 0, 2, 1, 0, 0, 0, n[0]],
        [1, 2, 0, 1, 0, 0, 1, 0, 0, n[1]],
        [2, 1, 0, 1, 0, 0, 0, 1, 0, n[2]],
        [0, 0, 3, 1, 2, 0, 0, 0, 1, n[3]],
        [p[0], p[1], p[2], p[3], p[4], 0, 0, 0, 0, 0]
    ]
    for x in range(4):
        a = 0
        extra = 0
        for j in range(5):
            if squash[4][j] >= a:
                a = squash[4][j]
                extra = j
        if a <= 0:
            solve = [0] * 6
            for i in range(4):
                if deb[i] < 5:
                    solve[deb[i]] = squash[i][9]
            solve[5] = squash[4][9]
            return solve
        a = 1e+16
        b = 0
        min = 0
        for k in range(4):
            if squash[k][extra] != 0:
                b = squash[k][9] / squash[k][extra]
                if b < a:
                    a = b
                    min = k
        a = squash[min][extra]
        for k in range(10):
            squash[min][k] = squash[min][k] / a
        for k in range(5):
            if k != min:
                if squash[k][extra] != 0:
                    a = squash[k][extra]
                    for j in range(10):
                        squash[k][j] = squash[k][j] - squash[min][j] * a
        deb[min] = extra
    solve = [0] * 6
    for i in range(4):
        if deb[i] < 5:
            solve[deb[i]] = squash[i][9]
    solve[5] = squash[4][9]
    return solve


def Usage():
        print ("USAGE:\n\t./307multigrains n1 n2 n3 n4 po pw pc pb ps\n")
        print ("DESCRIPTION:\n\tn1\tnumber of tons of fertilizer F1")
        print ("\tn2\tnumber of tons of fertilizer F2\n\tn3\tnumber of tons of fertilizer F3")
        print ("\tn4\tnumber of tons of fertilizer F4\n\tpo\tprice of one unit of oat")
        print ("\tpw\tprice of one unit of wheat\n\tpc\tprice of one unit of corn")
        print ("\tpb\tprice of one unit of barley\n\tps\tprice of one unit of soy\n")
        exit(0)

def numerize(ent) -> bool:
    try:
        int(ent)
    except ValueError:
        return False
    else:
        return True

def main(args):
    if len(sys.argv) == 0:
        exit(84)
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        Usage()
    if len(sys.argv) != 10:
        exit(84)
    for args in sys.argv[1:]:
            if numerize(args) is False:
                print("Only integers are allowed.")
                exit(84)
            if int(args) < 0:
                print("Arguments should be positive values.")
                exit(84)
    n = []
    p =[]

    try:
        for i in range(1,5):
            n.append(int(sys.argv[i]))
        for j in range(5,10):
            p.append(int(sys.argv[j]))
    except ValueError:
        print ("Invalid parameter")
        exit(84)
    print("Resources: %d F1, %d F2, %d F3, %d F4\n" %(n[0], n[1], n[2], n[3]))
    solve = matrix_square(n,p)
    fruit("Oat",p[0], solve[0])
    fruit("Wheat",p[1], solve[1])
    fruit("Corn",p[2], solve[2])
    fruit("Barley",p[3], solve[3])
    fruit("Soy",p[4], solve[4])
    final(-solve[5])
    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])