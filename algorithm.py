def sma(array=[], n=5):
    if n < 1:
        return []

    size = len(array)
    avg = [0] * size
    sum = 0
    for i in range(0, size):
        sum = sum + array[i]
        if i < n:
            avg[i] = sum / n
        else:
            avg[i] = (avg[i-1] * n - array[i - n] + array[i]) / n

    return avg


def ema(array=[],n=5):
    if n < 1:
        return []

    size = len(array)
    avg = [0] * size

    a = 2/(n+1)

    for i in range(0,size):
        if i == 0:
            avg[i] = array[i]
        else:
            avg[i] = a * (array[i] - avg[i-1]) + avg[i-1]

    return avg


def macd(array=[], low=12, high=26, middle=9):
    size = len(array)
    low_ema = ema(array, low)
    high_ema = ema(array, high)

    diff = [0] * size

    for i in range(0, size):
        diff[i] = low_ema[i] - high_ema[i]

    dea = ema(diff, middle)

    cd = [0] * size

    for i in range(0,size):
        cd[i] = (diff[i] - dea[i]) * 2

    return diff, dea, cd



