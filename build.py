import pandas as pd
import numpy as np


def solution(data, indexs):
    out = pd.DataFrame(data, index = indexs)
    return out
