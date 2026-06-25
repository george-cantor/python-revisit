def checkArgs(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int, float)):
        print((a+b+c)**2)
    else:
        print("Error: the input arguments are not of the expected types")
checkArgs(3,4,5)
checkArgs(3,4,"g")
checkArgs(1,2)