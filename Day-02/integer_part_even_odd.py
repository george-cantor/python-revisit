"""
User will enter a floating-point number, for example 238.915.

Your task is to extract the integer portion before the decimal point
(in this case, 238) and determine whether that integer portion is
an even number or an odd number.
"""
x = float(input("Enter the number::"))
y = int(x)
print(y)
if y%2 == 0:
    print("Integer portion is even.")
else:
    print("Integer portion is odd")