zz=1

def y():
    x()

def x():
    global zz
    zz = 3

y()
print(zz)