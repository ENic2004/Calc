# Little Command-Line Calc, Written by: ENic2004
# See github for more Informarions

#Import 2nd File
from operations import ops

#Input Manager(cl)
class cl:
    def main():
        # Mainloop
        print("Here the wlctext has to go!")
        f = int(input("Wich Function to do? "))
        cl.choose(f)
    def choose(f):
        # Function Chooser
        if f == 1:
            cl.inputmgr()
            ops.add(x, y)
            cl.main()
        else:
            print("Not known Function!")
            cl.main()
    def inputmgr():
        # Inputmanager
        try:
            global x
            global y
            x = int(input("First Number: "))
            y = int(input("Second Number: "))
        except ValueError:
            print("Wrong Value!")
            cl.space(1)
            cl.inputmgr()
    def space(x):
        #Spacing Function
        while x > 0:
            print()
            x = x - 1

#Start MainLoop
#------ DO NOT PUT CODE BELOW, WILL BE NEVER PROCEED -------
try:
    cl.main()
except ValueError:
    print("Wrong Value!")
    cl.space(2)
    cl.main()
