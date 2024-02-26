import numpy
from scipy.linalg import solve

# the first matrix
# brandon's section
A = numpy.array([[3 ,1,-1],
                 [1, 4, 1],
                 [2, 1, 2]])

b = numpy.array([2, 12, 10])
#solving the matrix and storing in solution_1
solution_1 = solve(A, b)

#the second matrix
C = numpy.array([[1,-10, 2, 4],
      [3, 1, 4, 12],
      [9, 2, 3, 4],
      [-1, 2, 7, 3]])

d = numpy.array([2, 12, 21, 37])

solution_2 = solve(C, d)
# Ethan's section
print("The solution to the first equation:")
for value in solution_1:
    print(f"[{value:.1f}]")
print(f"The solution to the second equation:")
for value in solution_2:
    print(f"[{value:.3f}]")



