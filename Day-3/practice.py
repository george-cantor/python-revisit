# Functions
def printSuccess():
    print("The task is successfull")
    print("Movinf to the next task.")
#calling of function
printSuccess()

# Function doc string
def printSuccess2():
    """This function is doing nothing except printing a message.
    That message is "hellow"
    """
    print("Hellow")
help(printSuccess2)
printSuccess2
# Function (input arguments)
def printMsg(msg):
    """The function prints the message supplied by the user or prints that msg is not in the form of string."""
    if isinstance(msg,str):
        print(msg)
    else:
        print("Your input argument is not a string.")
        print("Here is the type of what you have supplied:",type(msg))
help(printMsg)
printMsg(23)
printMsg("hello")
# Function multiple arguments
#Ex:1
def mypow(a,b):
    """This function computes power just like built pow function"""
    c = a**b
    print(c)
help(mypow)
mypow(3,4)
# Ex:2
def checkArgs(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int, float)):
        print((a+b+c)**2)
    else:
        print("Error: the input arguments are not of the expected types")
checkArgs(3,4,5)
checkArgs(3,4,"g")
checkArgs(1,2)