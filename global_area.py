numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

print square(4)

