import numpy as np


def dominationcheck(X, m):
    nrows = X.shape[0]
    ncols = X.shape[1]

    output = []
    if m == 'cols':
        for i in range(0, ncols-1):
            for j in range(i+1, ncols):
                index1 = (X[:, i] < X[:, j]).sum()
                index2 = (X[:, i] > X[:, j]).sum()

                if index1 == nrows:
                    output.append(i)
                if index2 == nrows:
                    output.append(j)

    elif m == 'rows':
        for i in range(0, nrows-1):
            for j in range(i+1, nrows):
                index1 = (X[i, :] < X[j, :]).sum()
                index2 = (X[i, :] > X[j, :]).sum()

                if index1 == ncols:
                    output.append(i)
                if index2 == ncols:
                    output.append(j)

    return output


def dominationdelete(A, B, moves=False):
    rows = dominationcheck(A, 'rows')
    cols = dominationcheck(B, 'cols')
    A = np.delete(A, rows, axis=0)
    A = np.delete(A, cols, axis=1)
    B = np.delete(B, rows, axis=0)
    B = np.delete(B, cols, axis=1)

    if moves:
        return A, B, rows, cols
    else:
        return A, B


def dominationfinal(A, B, moves=False):
    removedrows = []
    removedcols = []
    i = 0
    j = 0
    while (A.shape != dominationdelete(A, B, moves)[0].shape) and (B.shape != dominationdelete(A, B, moves)[1].shape) :
        result = dominationdelete(A, B, moves)
        A = result[0]
        B = result[1]

        if moves:
            if result[2]:
                removedrows += [x+i for x in result[2]]
                i+=1
            if result[3]:
                removedcols += [y+j for y in result[3]]
                j += 1

    return A, B, removedrows, removedcols
