# Some Useful Functions

## Functions

**Functions** are reusable blocks of code that execute a specific task when they are called.

## Built-in Functions

Built-in functions are predefined functions provided by Python that can be used directly.

---

# Examples of Some Common Built-in Functions

### `round()`

Rounds a number to a specified number of decimal places or to the nearest integer.

```python
round(number, ndigits)
```

---

### `divmod(x, y)`

Returns a tuple containing the quotient and remainder.

```python
divmod(dividend, divisor)
```

---

### `isinstance()`

Returns `True` if the object is an instance of the specified class. Multiple classes can also be checked at once.

```python
isinstance(object, classinfo)
```

---

### `pow(x, y, z)`

Computes (x^y) and then returns the remainder when divided by `z`.

```python
pow(x, y, z)    # equivalent to (x**y) % z
```

---

### `input()`

Takes input from the user.

```python
a = input("Enter something: ")
```

---

### `help()`

Displays the internal documentation of a function, module, or object.

```python
help()
```

---

# Control Flow

## if-elif-else Statement

```python
if condition_1:
    # runs if condition_1 is True
elif condition_2:
    # runs if condition_1 is False and condition_2 is True
else:
    # runs if all previous conditions are False
```

### Example

```python
a = int(input("a: "))
b = int(input("b: "))

if a > b:
    print("a is bigger")
elif a == b:
    print("Both are equal")
else:
    print("b is bigger than a")
```

---

# Nested if

```python
if condition_outer:

    if condition_inner:
        statements_1

    else:
        statements_2

else:
    statements_3
```

Nested `if` statements are used when one condition depends on another condition.

---

# Loops (while)

A `while` loop repeatedly executes a block of code as long as the specified condition remains `True`.

```python
while condition:
    # block of code
```

---

# pass Statement

The `pass` statement does nothing. It acts as a placeholder for future code.

```python
while True:
    pass
```

---

# break and continue

## break

The `break` statement immediately terminates the loop and transfers control to the statement following the loop.

## continue

The `continue` statement skips the remaining statements in the current iteration and proceeds to the next iteration.

---

# Lists

A list is an ordered, mutable collection of elements.

Example:

```python
L = [1, 2, 3, 4]
```

### Accessing Elements

```python
L[i]       # Returns the i-th element
```

### Adding Elements

```python
L.append(x)    # Adds x to the end of the list
```

---

# for Loop

A `for` loop is used to iterate over a sequence such as a list, tuple, string, dictionary, or any other iterable object.

```python
for variable in sequence:
    # block of code
```

Example:

```python
for i in [1, 2, 3]:
    print(i)
```

---

# else in a for Loop

The `else` block executes only if the loop completes normally, i.e., without encountering a `break` statement.

```python
for item in iterable:

    if condition:
        break

else:
    # Executes only if break was never executed
```

### Example

```python
for i in range(5):

    if i == 10:
        break

else:
    print("Loop completed successfully")
```

---

# Day 2 Topics Covered ✅

* Functions
* Built-in Functions
* Control Flow
* if-elif-else Statements
* Nested if Statements
* while Loops
* pass Statement
* break and continue
* Lists
* for Loops
* else in for Loops

---

**Status:** ✅ Day 2 Completed

