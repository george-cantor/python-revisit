# Python Notes 🐍

## Algorithm

Step-by-step solution to a problem.

## Flowchart

Graphical representation of an algorithm.

## Pseudocode

Human-readable description of an algorithm.

### Example of Pseudocode Using Sorting

#### Searching Minimum of List and Its Index

```text
searchMinList(L, n)
    minValue = L[1]
    index = 1
    counter = 2

    while (counter <= n)
        v = L[counter]

        if (v <= minValue)
            minValue = v
            index = counter
        else
            pass
        endIF

        counter = counter + 1
    endWhile

    return minValue, index
end searchMinList
```

#### Selection Sort

```text
sortList(L, n)
    L2 = []
    counter = 1

    while (counter <= n)
        minValue, index = searchMinList(L, n)
        insert minValue into L2
        delete L[index]
        n = n - 1
    endWhile

    return L2
end sortList
```

---

## Why Choose Python?

* Beginner-friendly
* Versatile and flexible
* One of the largest and most mature package ecosystems
* Most popular language in the Machine Learning world

---

## IDE (Integrated Development Environment)

An application used for writing, testing, and debugging code.

### Examples of IDEs

* Jupyter Notebook
* PyCharm
* Spyder
* Canopy
* Vim
* Atom
* VS Code

---

## Variables and Operators

### Variables

A variable is a name that stores data which can be used later in the program.

---

# Data Types

## Numeric Types

* **Integer (`int`)**: Holds whole numbers. Example: `42`
* **Float (`float`)**: Holds real numbers. Example: `3.14`
* **Complex (`complex`)**: Holds complex numbers. Example: `4 + 9j`

## Text Type

* **String (`str`)**: Sequence of characters enclosed in single, double, or triple quotes.

Example:

```python
"Hello"
```

## Sequence Types

* **List**: Mutable ordered collection of items.

Example:

```python
[1, 2, 3]
```

* **Tuple**: Immutable ordered collection.

Example:

```python
(1, 2, 3)
```

## Mapping Type

* **Dictionary (`dict`)**: Stores key-value pairs.

Example:

```python
{"id": 1}
```

## Set Types

* **Set**: Unordered, mutable collection of unique elements.

Example:

```python
{1, 2, 3}
```

* **Frozenset**: Immutable version of a set.

## Boolean and None Types

* **Boolean (`bool`)**: Represents logical states, either `True` or `False`.
* **None (`NoneType`)**: Represents the absence of a value.

---

## Examples

```python
x = 2      # int
y = 3.14   # float
z = "Hello" # str
```

---

## Checking Type of Variables

```python
print(type(variable))
```

Example:

```python
print(type(x))
```

---

## Multiple Assignment

```python
a, b = 4, 5.0
```

---

## Deleting Variables

```python
del x
```

---

# Operators

* **Addition (`+`)**
* **Subtraction (`-`)** : Subtracts the right operand from the left.
* **Multiplication (`*`)**
* **Division (`/`)** : Always returns a floating-point number.
* **Floor Division (`//`)** : Returns the quotient after division.

Example:

```python
7 // 2
# Output: 3
```

* **Modulus (`%`)** : Returns the remainder after division.
* **Exponentiation (`**`)** : Raises the first number to the power of the second.

---

# Concatenation

Applicable to strings.

```python
"string1" + "string2"
```

Output:

```python
"string1string2"
```

---

## Naming Conventions of Variables

* Allowed characters: `A-Z`, `a-z`, `0-9`, and underscore (`_`)
* Variable names cannot start with a digit
* No spaces or hyphens are allowed
* Reserved keywords cannot be used as variable names
* Python is case-sensitive

Examples:

```python
student_name = "Alex"
marks1 = 95
```

---

## Logical Operators

These operators always return Boolean values.

* **and** : Returns `True` only if both operands are `True`.
* **or** : Returns `True` if at least one operand is `True`.
* **not** : Reverses the Boolean value.

Examples:

```python
True and False
# False

True or False
# True

not True
# False
```

---

## Comparison Operators

These operators always return Boolean values.

* `==` : Equal to
* `!=` : Not equal to
* `<` : Less than
* `>` : Greater than
* `<=` : Less than or equal to
* `>=` : Greater than or equal to

Example:

```python
5 == 5
# True

7 > 10
# False
```

---

## Precedence of Logical Operators

```text
not > and > or
```

* `not` has the highest precedence.
* `and` has higher precedence than `or`.
* `or` has the lowest precedence.

---

## Day 1 Topics Covered ✅

* Algorithm
* Flowchart
* Pseudocode
* Why Python?
* IDEs
* Variables
* Data Types
* Operators
* Concatenation
* Naming Conventions
* Logical Operators
* Comparison Operators
* Operator Precedence

---

**Status:** ✅ Day 1 Completed
