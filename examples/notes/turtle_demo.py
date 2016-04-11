from turtle import *

# Small vocabulary:  forward, right, clearscreen
# Teach vocubulary in pairs:
#   forward/backward  left/right  penup/pendown
#   width/color
# Teach by asking to make predictions.
# Avoid syntax errors.  Use the arrow keys.
# Use the word "YOU" to describe what happened.
# Use the word "USUALLY" for default arguments.
# Barrier 1: Computers aren't programmable
# Barrier 2: Computers create problems rather than solve them
# Barrier 3: Switching from forced learning to volunteer learning
# Question reversing, hinting, and pointing
#     to create high probabity of q&a success

def el(big=100):
    forward(big)
    right(90)

def square(big=100):
    el(big)
    el(big)
    el(big)
    el(big)

def star(wide=10, outside='blue', inside='green',
         times=18, shape=square, big=100, turn=20):
    clearscreen()
    begin_fill()
    width(wide)
    color(outside, inside)
    for i in range(times):
        shape(big)
        right(turn)
    end_fill()

def spiral(wide=10, outside='blue', inside='green',
         times=18, shape=square, big=10, turn=20):
    clearscreen()
    begin_fill()
    width(wide)
    color(outside, inside)
    for i in range(times):
        shape(big * i)
        right(turn)
    end_fill()


