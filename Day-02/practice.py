
# ============================================
# Some Useful Built-in Functions
# ============================================

# 1. round()

print(round(4.556))          # 5
print(round(4.345))          # 4
print(round(4.556789, 3))    # 4.557
print(round(4.556389, 3))    # 4.556


# ============================================
# 2. divmod(x, y)
# ============================================

print(divmod(22, 10))        # (2, 2)
print(divmod(34, 9))         # (3, 7)


# ============================================
# 3. isinstance()
# ============================================

print(isinstance(3, int))                    # True
print(isinstance(2.4, int))                  # False
print(isinstance(2.4, float))                # True
print(isinstance(2.4, (int, float)))         # True
print(isinstance(2 + 3j, (int, float, str))) # False
print(isinstance(2 + 3j, complex))           # True


# ============================================
# 4. pow()
# ============================================

print(pow(2, 4))             # 16

print(pow)                   # <built-in function pow>

print(pow(2, 4, 7))          # 2


# ============================================
# 5. input()
# ============================================

x = input("Enter a number: ")
print(x)                     # Depends on user input
print(type(x))               # <class 'str'>

y = int(x)
print(type(y))               # <class 'int'>


# ============================================
# 6. help()
# ============================================

print(help(pow))             # Displays documentation


# ============================================
# Control Flow : if-elif-else
# ============================================

a = int(input("a: "))
b = int(input("b: "))

if a > b:
    print("a is bigger")

elif a == b:
    print("Both are equal")

else:
    print("b is bigger than a")


# ============================================
# Nested if
# ============================================

x = int(input("Enter a number: "))

if x > 10:

    print("Number is above 10")

    if x > 20:
        print("and also above 20!")

    else:
        print("but not above 20.")

else:
    print("below 10")


# ============================================
# while Loop
# ============================================

n = int(input("n: "))

i = 1

while i < n:
    print(i**2)
    print("This is iteration number:", i)
    i += 1

print("Loop done")


# ============================================
# break Statement
# ============================================

i = 1

while True:

    if i % 9 == 0:
        print("Inside if")
        break

    else:
        print("Inside else")
        i += 1

print("Done")


# ============================================
# continue Statement
# ============================================

i = 1

while True:

    if i % 9 != 0:
        print("Inside if")
        i += 1
        continue

    print("something")
    print("Something else")
    break

print("Done")


# ============================================
# for Loop
# ============================================

L = []

for i in range(0, 10, 2):

    print(i + 1)     # 1 3 5 7 9

    L.append(i**2)

print(L)             # [0, 4, 16, 36, 64]


# ============================================
# else in for Loop
# ============================================

S = {"apple", 4.9, "cherry"}

for x in S:
    print(x)         # Order may vary

else:
    print("Loop terminates successfully")

print("Outside the loop")


# ============================================
# Exploring Dictionary
# ============================================

D = {
    "A": 10,
    "B": -19,
    "C": "abc"
}

for key in D:

    print(key, D[key])

# A 10
# B -19
# C abc