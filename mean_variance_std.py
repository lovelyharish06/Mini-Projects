import numpy as np
def calculate(l):
    try:
        if len(l)<9:
            raise ValueError("List must contain nine numbers")
        ar=l.reshape(3,3)
        d={
            'mean':[np.mean(ar,axis=0).tolist(),np.mean(ar,axis=1).tolist(),np.mean(l).tolist()],
            'variance':[np.var(ar,axis=1).tolist(),np.var(ar,axis=1).tolist(),np.var(l).tolist()],
            'standard deviation':[np.std(ar,axis=0).tolist(),np.std(ar,axis=1).tolist(),np.std(l).tolist()],
            'max':[np.max(ar,axis=0).tolist(),np.max(ar,axis=1).tolist(),np.max(ar).tolist()],
            'min':[np.min(ar,axis=0).tolist(),np.min(ar,axis=1).tolist(),np.min(ar).tolist()],
            'sum':[np.sum(ar,axis=0).tolist(),np.sum(ar,axis=1).tolist(),np.sum(ar).tolist()]
            }
        return d
    except ValueError as e:
        print(e)
l=np.array([0,1,2,3,4,5,6,7])
calculate(l)