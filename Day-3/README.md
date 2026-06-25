# Functions
It is defined using the def keyword, followed by the function name, parentheses () containing optional parameters, and a colon :.
```bash
def function_name(parameter1, parameter2):
    """Optional docstring describing the function."""
    # Function body (indented code)
    result = parameter1 + parameter2
    return result
```
# core syntax components:
```text
* def keyword : Start of function header.
* function name: unique identifier of particular function
* parameters: input placeholders placed inside the parentheses. It can be blanked.
* dolon(:): end of function signature line.
* return statement : exit the function and pass back the value.
```
# Calling of function:
write the function's name followed by parentheses (), adding any required values (arguments) inside those parentheses. 
# Function(doc string)
It is just like comment explaining what function is doing and its enclosed under triple qitation mark(""" """) and must be written immediately under function header line.
# Function(input arguments):
It is the actual data values you pass into a function when you call it.
# function multiple input arguments:
```bash
def printMessage(msg1,msg2):
    printMessage(msg1,msg2)
```