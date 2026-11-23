import numpy as np

def f_score(y_true, y_pred, beta):
    """
    Calculate F-Score for a binary classification task.

    :param y_true: Numpy array of true labels
    :param y_pred: Numpy array of predicted labels
    :param beta: Weight of recall relative to precision (beta > 1 favours recall)
    :return: F-Score rounded to three decimal places
    """
    pass
    #cal some thing
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range (len(y_pred)):
        if(y_pred[i]==1 and y_true[i]==1):
            tp+=1
        if(y_pred[i]==0 and y_true[i]==1):
            fn+=1
        if(y_pred[i]==0 and y_true[i]==0):
            tn+=1
        if(y_pred[i]==1 and y_true[i]==0):
            fp+=1
    p=0
    r=0
    p = tp/(tp+fp)
    r = tp/(tp+fn)
    return round((1+beta**2)*p*r/(p*beta**2+r),3)
