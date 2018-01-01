# Little Command-Line Calc, Written by: ENic2004
# See github for more Informarions
#Import 2nd File
from operations import ops

#Input Manager(cl)
class cl:
    def main():
        print("Here the wlctext has to go!")
        f = int(input("Wich Function to do? "))
        cl.choose(f)
    def choose(f):
        if f == 1:
            cl.inputmgr()
            ops.add(x, y)
            cl.main()
        else:
            print("Not known Function!")
            cl.main()
    def inputmgr():
        global x
        global y
        x = int(input("First Number: "))
        y = int(input("Second Number: "))
    def space(x):
        while x > 0:
            print()
            x = x - 1

#Start MainLoop
#------ DO NOT PUT CODE BELOW, WILL BE NEVER PROCEED -------
cl.main()
