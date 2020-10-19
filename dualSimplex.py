import numpy as np
M = 10
t5_2 = np.array([[1, 1, -1, 0, 0, 0, 0],
                 [0, -2, 1, 1, 0, 0, 2.1],
                 [0, 1, -2, 0, 1, 0, 2.2],
                 [0, 1, 1, 0, 0, 1, 5]], dtype = float)
test = np.array([[1, 3, 2, 0, 0, 0, 0],
              [0, 1, 3, 1, 0, 0, 9],
              [0, 1, 2, 0, 1, 0, 8],
              [0, 2, 1, 0, 0, 1, 8]], dtype = float)
test2 = np.array([[1, 2, 1, 0, 0, 0, 0],
              [0, -2, 1, 1, 0, 0, 2],
              [0, -1, 2, 0, 1, 0, 8],   
              [0, 1, -1, 0, 0, 1, 5]], dtype = float)
t6_2 = np.array([[1, -10 + 3 * M, -5 , -M, -M, 0, -M,  5 * M],
      [0, 1, 1, -1, 0, 0, 0, 4],
      [0, 1 ,0, 0, -1, 0, 0, 1],
      [0, 0, 1, 0, 0, 1, 0, 6],
      [0, 1, -1, 0, 0, 0, -1, 0.0000000001]], dtype = float)
t2 = np.array([[1, -10, -5, 0, 0, 0, 0, 0],
      [0, 1, 1, -1, 0, 0, 0, 4],
      [0, 1 ,0, 0, -1, 0, 0, 1],
      [0, 0, 1, 0, 0, 1, 0, 6],
      [0, 1, -1, 0, 0, 0, -1, 0]], dtype = float)
test3 = np.array([[1, -1, 3, 0, 0, 0, 0, 10000, 0],
              [0, 1, 1, -1, 0, 0, 0, 1, 5],
              [0, 1, 1, 0, 1, 0, 0, 0, 15],
              [0, 0, 1, 0, 0, 1, 0, 0, 2],
              [0, 1, 0, 0, 0, 0, 1, 0, 3]], dtype = float)
step1 = np.array([[1, 3, 0 , -1, -1, 0, -1,  5],
      [0, 1, 1, -1, 0, 0, 0, 4],
      [0, 1 ,0, 0, -1, 0, 0, 1],
      [0, 0, 1, 0, 0, 1, 0, 6],
      [0, 1, -1, 0, 0, 0, -1, 0.0000000001]], dtype = float)
dual = np.array([[1, -2, -2, -5, 0, 0, 0, 0],
                 [0, 2 , -1, -1, 1, 0, 0, -1],
                 [0, -1, 2, -1, 0, 1, 0, 1],
                 [0, -1, -1, -1, 0, 0, 1, 0.000000001] ], dtype = float)
t5_21 = np.array([[1, 0, 0, 0, -0.66666667, -0.33333333, 0, -3.13333333],
                 [0, 0, 0, 1, 1, 1, 0, 9.3],
                 [0, 1, 0, 0, 0.33333333, 0.66666667, 0, 4.06666667],
                 [0, 0, 1, 0, -0.33333333, 0.33333333, 0, 0.93333333],
                 [0, 0, 0, 0, -5, -10, 1, -1]], dtype = float)
t5_22 = np.array([[ 1.00000000,  0.00000000,  0.00000000,
         0.00000000,  0.00000000,  1.00000001,
        -0.133333334, -3.00000000],
       [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         1.00000000e+00,  0.00000000e+00, -1.00000000e+00,
         2.00000000e-01,  9.10000000e+00],
       [ 0.00000000e+00,  1.00000000e+00,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  1.00000001e-08,
         6.66666660e-02,  4.00000000e+00],
       [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  9.99999990e-01,
        -6.66666660e-02,  9.99999996e-01],
       [-0.00000000e+00, -0.00000000e+00, -0.00000000e+00,
        -0.00000000e+00,  1.00000000e+00,  2.00000000e+00,
        -2.00000000e-01,  2.00000000e-01]])
def dualsimplex(mat):
    varS = ["x1", "x2", "y1", "y2", "y3", "s1"]
    varC = ["y1", "x1", "x2","s1"]
    for k in range(1):
    #while not np.all(mat[0][1:len(mat[0]) - 2] >= 0):
        #string = np.argmin(mat[:,len(mat[0]) - 1][1:]) + 1
        #col = rowdual(mat[0][1:len(mat[0]) - 2], mat[string][1:len(mat[0]) - 2]) + 1
        string = 4
        col = 4
        print(string, col)
        temp = varC[string - 1]
        varC[string - 1] = varS[col - 1]
        mat[string] = mat[string] / mat[string][col]
        mat = np.array([mat[i]- mat[i][col]*mat[string] if i != string else mat[i] for i in range(len(mat))])
        print(mat)
    return mat, varC, varS
def row(col1, col2):
    col2=col2.copy()
    for i in range(len(col1)):
        if col1[i] * col2[i] <= 0:
            col2[i] = 10**5
        else:
            col2[i] = col2[i] / col1[i]
    return np.argmin(col2)
def rowdual(str1, str2):
    print(str1,str2)
    str1 = str1.copy()
    for i in range(len(str1)):
        if str1[i] * str2[i] >= 0:
            str1[i] = 10**5
        else:
            str1[i] = str1[i] / str2[i]
    return np.argmin(str1)
def simplex(mat, num):
    if num == 1:
        varS = ["x1", "x2", "y1", "y2", "y3"]
        varC = ["y1", "y2", "y3"]
    elif num == 2:
        varS = ["x1", "x2", "y1", "y2", "y3", "y4"]
        varC = ["r1", "r2", "y3", "r3"]
    print(mat)
    while not np.all(mat[0][1:len(mat[0]) - 2] <= 0):
        col = np.argmax(mat[0][1:len(mat[0]) - 2]) + 1
        string = row(mat[:,col][1:], mat[:,len(mat[0]) - 1][1:]) + 1
        temp = varC[string - 1]
        varC[string - 1] = varS[col - 1]
        mat[string] = mat[string] / mat[string][col]
        mat = np.array([mat[i]- mat[i][col]*mat[string] if i != string else mat[i] for i in range(len(mat))])
        print(mat)
    return varS, varC,
def evaluation(mat, string, col):
    mat[string] = mat[string] / mat[string][col]
    mat = np.array([mat[i]- mat[i][col]*mat[string] if i != string else mat[i] for i in range(len(mat))])
    return mat
#print(simplex(step1, 2))
#print(simplex(t5_2, 1))
print(dualsimplex(t5_21))
#print(dualsimplex(t5_22))
#print(dualsimplex(dual))
#print(evaluation(dual, 1, 1))

