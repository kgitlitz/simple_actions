
def x(y):
    print(y, " ", end="")
    return y + 1

def a(y):
    print(y, " ", end="")
    return y + 2

x(1)					

print( a(1))			

print( x( a(1) ))	

print( a( x(1) ))		

