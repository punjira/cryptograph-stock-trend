import sys
import os
import json

from redisClient import redisInterface
from trendCalculator import processTrendOnSet

rd = redisInterface("localhost",6380)

def routine(hashkey):
    candles = rd.getCandles(hashkey)
    if candles != None:
        close = []
        date = []
        sortedDict = dict(sorted(candles.items()))
        for i in sortedDict:
            close.append(eval(sortedDict[i])[4])
            date.append(eval(sortedDict[i])[0])
        dir, strength = processTrendOnSet(close, date)
        if dir != None:
            print(hashkey, " has ",dir, strength)