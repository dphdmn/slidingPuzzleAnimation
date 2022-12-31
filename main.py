import os
import numpy
import math
import subprocess
import shutil
import time
from cairosvg import svg2png
import sys

# dependecy problem solution:
# pip install pipwin
# pipwin install cairocffi

# if lower, may cause bugs if exe running very slow
WAITING_TIME_PER_FRAME = 0.05

PUZZLE_SIZE = 4  # OK ITS BAD, IT CHANGES WHEN PUZZLE IS CREATED, SO IT CAN WORK WITH 1 PUZZLE AT THE TIME AND I'M LAZY TO MAKE CLASS


# 0..15 to 0..3
def getXY(lin):
    N = PUZZLE_SIZE
    y = int(math.floor(lin / N))
    x = lin % N
    return x, y


# return empty puzzle (matrix from 1 to 16 (0))
def create_puz(N):
    global PUZZLE_SIZE
    PUZZLE_SIZE = N
    arr = numpy.arange(1, PUZZLE_SIZE * PUZZLE_SIZE + 1)
    arr[PUZZLE_SIZE * PUZZLE_SIZE - 1] = 0
    blank = PUZZLE_SIZE * PUZZLE_SIZE - 1
    return arr.reshape(PUZZLE_SIZE, PUZZLE_SIZE), blank


# scramble matrix with string like slidysim
def scramble_puz(puzzle, scramble):
    blank = PUZZLE_SIZE * PUZZLE_SIZE - 1
    arr = tuple([int(a) for x in scramble.split("/") for a in x.split()])
    for idd, el in enumerate(arr):
        if el == 0:
            blank = idd
        x, y = getXY(idd)
        puzzle[y, x] = el
    return puzzle, blank


# do move, not check if possible, blank 0 id of empty, move - RULD
def move(puzzle, blank, move):
    xb, yb = getXY(blank)
    N = PUZZLE_SIZE
    if move == "R":
        puzzle[yb, xb] = puzzle[yb, xb - 1]
        puzzle[yb, xb - 1] = 0
        blank -= 1
    if move == "L":
        puzzle[yb, xb] = puzzle[yb, xb + 1]
        puzzle[yb, xb + 1] = 0
        blank += 1
    if move == "D":
        puzzle[yb, xb] = puzzle[yb - 1, xb]
        puzzle[yb - 1, xb] = 0
        blank -= N
    if move == "U":
        puzzle[yb, xb] = puzzle[yb + 1, xb]
        puzzle[yb + 1, xb] = 0
        blank += N
    return puzzle, blank


# do moves sequence, like RULD... string, Null if whatever is wrong
def doMoves(puzzle, blank, moves):
    try:
        for i in moves:
            puzzle, blank = move(puzzle, blank, i)
        return puzzle, blank
    except:
        return None, None


# returns true if puzzle is solved
def checkSolved(puzzle):
    s, _ = create_puz()
    return numpy.array_equal(puzzle, s)


# get slidysim style scramble from array
def toScramble(puzzle):
    scr = ""
    for i in puzzle:
        for j in i:
            scr += str(j) + " "
        scr = scr[:-1] + "/"
    return scr[:-1]


# runs exe file that saves out image called out.svg
def createImage(scramble):
    subprocess.run(["image_gen.exe", "--state", scramble])


def badsolutionfix(solution):
    nmax = PUZZLE_SIZE - 1
    moves = ["R", "U", "L", "D"]
    for move in moves:
        i = nmax
        while i > 1:
            solution = solution.replace(move + str(i), move * i)
            i = i - 1
    return solution


def generateImages(scramble, moves, tps):
    lens = [0, 0, 0, 17, 37, 64, 97, 136, 181, 232, 289]
    mypuz, blank = create_puz(lens.index(len(scramble)))
    mypuz, blank = scramble_puz(mypuz, scramble)
    try:
        shutil.rmtree("images")
    except FileNotFoundError as e:
        print("Old image folder was not found, new will be created. Yes i don't know why this message is needed")
    os.mkdir("images")
    createImage(toScramble(mypuz))
    frameid = 0
    time.sleep(WAITING_TIME_PER_FRAME)
    shutil.copy("out.svg", f"images/img{frameid:05d}.svg")
    moves = badsolutionfix(moves)
    for move in moves:
        frameid += 1
        mypuz, blank = doMoves(mypuz, blank, move)
        createImage(toScramble(mypuz))
        time.sleep(WAITING_TIME_PER_FRAME)
        shutil.copy("out.svg", f"images/img{frameid:05d}.svg")
        with open(f"images/img{frameid:05d}.svg", 'r') as mysvg:
            svg2png(scale=3, bytestring=mysvg.read(), write_to=f"images/img{frameid:05d}.png")
    subprocess.run(["ffmpeg", "-y", "-i", "images/img%05d.png", "-filter_complex",
                    f"[0]scale=hd1080,setsar=1,boxblur=20:20[b];[0]scale=-1:1080[v];[b][v]overlay=(W-w)/2",
                    "output25.mp4"])
    shutil.rmtree("images")
    os.remove("out.svg")
    speedVar = 25 / int(tps)
    subprocess.run(["ffmpeg", "-y", "-i", "output25.mp4", "-filter:v", f"setpts=PTS*{speedVar}", f"output{tps}.mp4"])
    os.remove("output25.mp4")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        generateImages(sys.argv[1], sys.argv[2], 20)
    if len(sys.argv) == 4:
        generateImages(sys.argv[1], sys.argv[2], sys.argv[3])
