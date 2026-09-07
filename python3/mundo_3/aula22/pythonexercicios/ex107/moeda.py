def half(v=0):
    s = v / 2
    return s

def double(v=0):
    s = v * 2
    return s

def rise(v=0, rate=0):
    s = v + (v * rate / 100)
    return s
def cutback(v=0, rate=0):
    s = v - (v * rate / 100)
    return s