import re       #importing re module for regex

class bcolors:
    HEADER = '\033[95m'
    SKYBLUE = '\033[96m'
    OKYELLOW = '\033[93m'
    OKGREEN = '\033[92m'
    WARNING = '\033[91m' #red

    ENDC = '\033[0m'
    BOLD = '\033[1m'

print(bcolors.SKYBLUE + bcolors.BOLD + "Here is your real-calculater..." + bcolors.ENDC)
print("Type" + bcolors.HEADER + bcolors.BOLD + " 'quit'" + bcolors.ENDC  + " to exit\n" )

pre=0
run=True

def performMath():
    global run
    global pre
    equ= ""
    if pre == 0:
        equ = input("Enter equation: ")
    else:
        equ= input(str(pre))

    if(equ == 'quit'):
        print(bcolors.SKYBLUE + bcolors.BOLD + "Good Bye...\n" + bcolors.ENDC)
        run = False
    else:
        equ = re.sub('[a-zA-Z,:()" "]', '',equ) #replace unnecessary input into nothing
        if len(equ) == 0:
            print(bcolors.WARNING + bcolors.BOLD + "invalid expression" + bcolors.ENDC)
        elif(pre == 0):
            pre = eval(equ)
        else:
            pre = eval(str(pre) + str(equ))

while run:
    performMath()
