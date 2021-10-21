import numpy as np

def preProcessCandles():
    print("pre processing candles")


def calculateRScore(y_real, y_pref):
    sse = sum((y_real - y_pref)**2)
    tse = (len(y_real) - 1) * np.var(y_real, ddof=1)
    r2_score = 1 - (sse / tse)
    return r2_score

def calculateFit(x, y, order):
    fit = np.polyfit(x,y,order)
    return fit

def processTrendOnSet():
    x, y = preProcessCandles()
    r_score = 0
    order = 1
    fit_eq = 0
    fit = []
    while r_score<0.5 and order<4:
        fit = calculateFit(x,y,order)
        fit_eq = 0
        for index, cur in enumerate(fit):
            fit_eq = fit_eq + cur * np.power(x, fit.size-index-1)
        r_score = calculateRScore(y, fit_eq)
        order = order + 1

    if r_score>0.5:
        # set new data and publish update
    else:
        # remove old data, and publish trend removal
        print("")