from itertools import *

def rle_encode(data):
    groups = (list(group) for _, group in groupby(data))
    # not finished because I need to restudy this parts