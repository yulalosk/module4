from fake_math import divide as fake_divide
from true_math import divide as true_divide
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)

def divide(first,second):
    if second == 0:
       return 'ошибка'
    else:
         return first / second

from math import inf
def divide(first,second):
    if second == 0:
       return inf
    else:
        return first / second