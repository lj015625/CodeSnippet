# Given a 2-D matrix P of predicted values and actual values, write a function precision_recall to calculate precision and recall metrics.
# Return the ordered pair (precision, recall).
#                Predicted=TRUE	Predicted=FALSE
# Actual=TRUE	         121	      9
# Actual=FALSE	         17	         144
P = [[121, 9],
     [17, 144]]


def precision_recall(p):
    # TT/(TT+FP)
    precision = p[0][0] / (p[0][0] + p[1][0])
    # TT/(TT+FN)
    recall = p[0][0] / (p[0][0] + p[0][1])

    return precision, recall


print(precision_recall(P))
