import numpy as np

def preProcessCandles(close, date):
    x = np.arange(len(close))
    y = np.array(close)
    return x , y


def calculateRScore(y_real, y_pref):
    sse = sum((y_real - y_pref)**2)
    tse = (len(y_real) - 1) * np.var(y_real, ddof=1)
    r2_score = 1 - (sse / tse)
    return r2_score

def calculateFit(x, y, order):
    fit = np.polyfit(x,y,order)
    return fit

def processTrendOnSet(close, date):
    print("processing data")
    x, y = preProcessCandles(close, date)
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
        direction = ""
        isStrong = False
        first_order_derivative = 0
        for ii, cc in enumerate(fit):
            if fit.size-ii-2 >= 0:
                first_order_derivative = first_order_derivative + (fit.size-ii-1) * cc * np.power(x, fit.size-ii-2)
        if np.sign(first_order_derivative)[-1] > 0:
            direction = "positive"
        else:
            direction = "negative"
        signs = np.sign(first_order_derivative)
        if direction=="positive" and np.all(signs==1):
            isStrong = True
        elif direction=="negative" and np.all(signs==-1):
            isString = True
        return direction, isStrong
    else:
        return None, None