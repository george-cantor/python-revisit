
# ============================================
# Variables and Data Types
# ============================================

x = 2
print(x)                     # 2
print(type(x))               # <class 'int'>

a, b = 4, 5.0
print(type(a))               # <class 'int'>
print(type(b))               # <class 'float'>

# Complex Numbers
com = 2 + 3j
print(type(com))             # <class 'complex'>

com1 = 2 + 0j
print(type(com1))            # <class 'complex'>

# Strings
st = "Hello"
print(type(st))              # <class 'str'>


# ============================================
# Arithmetic Operators
# ============================================

sum_result = x + a
print(sum_result)            # 6

division = x / a
print(division)              # 0.5

floor_division = x // a
print(floor_division)        # 0

modulus = x % a
print(modulus)               # 2

print(x + b)                 # 7.0

# String Concatenation
print("Hello" + "World")     # HelloWorld


# ============================================
# Boolean Values and Logical Operators
# ============================================

p = True
q = False
r = False

print(type(p))               # <class 'bool'>


# Logical AND
print(p and q)               # False
print(p and r)               # False
print(r and p)               # False
print(p and p)               # True
print(q and q)               # False


# Bitwise AND
print(p & q)                 # False


# Logical OR
print(p or q)                # True
print(p or r)                # True
print(p or p)                # True
print(q or q)                # False


# Bitwise OR
print(p | q)                 # True
print(r | p)                 # True


# Logical NOT
print(not p)                 # False


# ============================================
# Comparison Operators
# ============================================

print(2 < 3)                 # True
print(3 > 2)                 # True

print(2 == 2)                # True

print(2 != 2)                # False
print(2 != 3)                # True

print(type(2 > 3))           # <class 'bool'>

print(2 == 2.0)              # True
print(2 == (2 + 0j))         # True


# ============================================
# Precedence of Logical Operators
# not > and > or
# ============================================

print(False and False or True)     # True

print(False or True and False)     # False

