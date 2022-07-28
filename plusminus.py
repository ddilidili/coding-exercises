"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.
"""
import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos, neg, zer = 0, 0, 0
    for item in arr:
        if item > 0: pos += 1
        if item < 0: neg += 1
        if item == 0: zer += 1

    for term in [pos, neg, zer]: print("{:.6f}".format(term/len(arr)))

plusMinus([-4, 3, -9, 0, 4, 1])
