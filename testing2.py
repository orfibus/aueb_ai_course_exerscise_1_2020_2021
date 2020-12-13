#!/usr/bin/env python3
"""
exercise1 file including game start
"""
# Importing needed modules
import othello_testing2
import datetime
import time
import argparse

if __name__ == '__main__':
    """
    Initiating game play
    """
    for i in [True, False]:
        for j in range(0,25):
            cur_tim = time.time()
            game = othello_testing2.start_game(i, False, 2)
            game.play()
            end_time = time.time()
            x = ",{},{},{},{},{},test2\n".format(i, j+1, 2, datetime.datetime.now(), end_time - cur_tim )
            with open("test_results2.txt", "a") as f:
                f.write(x)
    for i in [True, False]:
        for j in range(0,25):
            cur_tim = time.time()
            game = othello_testing2.start_game(i, False, 3)
            game.play()
            end_time = time.time()
            x = ",{},{},{},{},{},test2\n".format(i, j+1, 3, datetime.datetime.now(), end_time - cur_tim )
            with open("test_results2.txt", "a") as f:
                f.write(x)

    for i in [True, False]:
        for j in range(0,25):
            cur_tim = time.time()
            game = othello_testing2.start_game(i, False, 4)
            game.play()
            end_time = time.time()
            x = ",{},{},{},{},{},test2\n".format(i, j+1, 4, datetime.datetime.now(), end_time - cur_tim )
            with open("test_results2.txt", "a") as f:
                f.write(x)

    for i in [True, False]:
        for j in range(0,25):
            cur_tim = time.time()
            game = othello_testing2.start_game(i, False, 5)
            game.play()
            end_time = time.time()
            x = ",{},{},{},{},{},test2\n".format(i, j+1, 5, datetime.datetime.now(), end_time - cur_tim )
            with open("test_results2.txt", "a") as f:
                f.write(x)
    for i in [True,False]:
        for j in range(0,10):
            cur_tim = time.time()
            game = othello_testing2.start_game(i, False, 6)
            game.play()
            end_time = time.time()
            x = ",{},{},{},{},{},test2\n".format(i, j+1, 6, datetime.datetime.now(), end_time - cur_tim )
            with open("test_results2.txt", "a") as f:
                f.write(x)
    # DEBUG MAIN (END)
