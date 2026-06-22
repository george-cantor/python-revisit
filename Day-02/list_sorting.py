"""
Given a list of numbers, for example:

[1, 2, 4, -5, 7, 9, 3, 2]

your task is to create another list that contains all the elements
arranged in ascending order (from smallest to largest).

For the above example, the resulting list should be:

[-5, 1, 2, 2, 3, 4, 7, 9]

Do not modify the original list; instead, create a new sorted list.
"""
L = [1, 2, 4, -5, 7, 9, 3, 2]
for j in range(len(L)):
    m = L[j]
    idx = j
    c = j
    for i in range(j,len(L)):
        if L[i]<m:
            m = L[i]
            idx = c
        c+=1
    temp = L[j]
    L[j] = m
    L[idx] = temp
print(L)
