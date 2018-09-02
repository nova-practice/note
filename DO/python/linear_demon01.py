# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat

A = np.mat([1,1])
print('A:\n', A)
print('A.T:\n', A.T)

B = mat([[1,2], [2,3]])
print('B:\n', B)

# A 1*2 B 2*2
print('A.B:', dot(A, B))
