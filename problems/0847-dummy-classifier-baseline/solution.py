import numpy as np
from collections import Counter
from collections import defaultdict

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    cnt = Counter(y_train)
    cnt = [list(x) for x in cnt.items()]
    cnt.sort(key=lambda x: x[1], reverse=True)
    #print (cnt)
    if(strategy == "most_frequent"):
        o = []
        for i in range (n_test):
            o.append(cnt[0][0])
        return o
    if(strategy == "constant"):
        o = []
        for i in range (n_test):
            o.append(constant)
        return o
    if(strategy == "uniform"):
        o = []
        for i in range (n_test):
            o.append(cnt[i%len(cnt)][0])
        return o
    have =0
    float_part = [x.copy() for x in cnt]
    for i in range (len(cnt)):
        cnt[i][1]= cnt[i][1]*n_test/len(y_train)
        float_part[i][1] = (cnt[i][1]-int(cnt[i][1]))
        cnt[i][1] = int(cnt[i][1])
        have += cnt[i][1]
    if(have<n_test):
      have = n_test - have
    else:
        have=0  
    #print(have,n_test)
    float_part.sort(key=lambda x:x[1],reverse = True)
    o = []
    for i in range(min(have,len(float_part))):
        o.append(float_part[i][0])
    for i in range (len(cnt)):
        a = cnt[i][0]
        b = cnt[i][1]
        for j in range (b):
            o.append(a)
    o.sort()
    return o