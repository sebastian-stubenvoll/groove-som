import pandas as pd
import numpy as np
import math

class SongData:

    def __init__(self, m, path='./raw_data/'):
        self.id = m['id']
        self.title = m['title']
        self.filename = m['filename']
        self.performer = m['performer']
        self.length = m['length']
        self.segments = m['segments']
        self.data = pd.read_csv(f'{path}{self.filename}')


    def filter(self, features=None):
        if features != None:
            self.data = self.data[features]

    def aggregate(self, stepsize=1, method='mean'):
        lastRow = self.data.shape[0]-1
        slices = dict()
        if self.segments != None:
            for seg in self.segments:
                b, e = seg
                slices[b] = e
            slice_str = ''
            for k,v in slices.items():
                if not isinstance(k, int) or not isinstance(v, int):
                    raise ValueError(f'An error occurred processing the segments field on {self.title} - ID: {self.id}')
                k = k * lastRow / self.length
                v = v * lastRow / self.length
                slice_str += '{}:{}:{}, '.format(math.floor(k), math.floor(v), stepsize)
            slice_str = slice_str[:-2]
            self.data = eval(f'self.data.iloc[np.r_[{slice_str}]]')
        if method == 'mean':
            self.data = self.data.mean().to_numpy()
        elif method == 'std':
            self.data = self.data.std().to_numpy()
        else:
            raise NotImplementedError('The aggregation method you are attempting to use, has not been implemented. \n\
Please use either \'std\' or \'mean\'.')





