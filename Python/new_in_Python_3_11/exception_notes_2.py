import math

class MyOwnError(Exception):
    __notes__ = ['This is a custom error!']

try:
    math.sqrt(-1)
except:
    raise MyOwnError