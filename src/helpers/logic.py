import sys
import os
import json
import numpy as np

from redisClient import redisInterface
from trendCalculator import processTrendOnSet

rd = redisInterface("history-redis-python-replica",6379)

def routine(hashkey):
    candles = rd.getCandles(hashkey)
    if candles != None:
        close = []
        date = []
        vols = []
        volWight = []
        sortedDict = dict(sorted(candles.items()))
        for i in sortedDict:
            close.append(eval(sortedDict[i])[4])
            date.append(eval(sortedDict[i])[0])
            vols.append(eval(sortedDict[i])[5])
            volWight.append((eval(sortedDict[i])[5])*(eval(sortedDict[i])[4]))
        dir, strength, started = processTrendOnSet(close, date)
        if dir != None and started != None:
            volume = np.sum(volWight[-started:])
            return {
                "key": hashkey,
                "status": 1,
                "location": date[-1],
                "details": {
                    "dir": dir,
                    "strength": strength,
                    "started": int(started),
                    "dollar_volume": int(volume)
                }
            }
        else:
            return {
                "key" : hashkey,
                "status": 0
            }