baseptr = topofstack = 0
stack = []

def initiallise():
    global baseptr, topofstack, stack
    topofstack = 0
    baseptr = -1
    stack = [None for i in range(0,5)]

def push (value):
    global baseptr, topofstack, stack
    if topofstack < 5:
        stack[topofstack] = value
        topofstack +=1
    else:
        print("overflow")

def pop():
    global baseptr, topofstack, stack
    if topofstack == baseptr + 1:
        print("underflow stack is empty")
    else:
        topofstack -= 1
        value = stack[topofstack]
        stack[topofstack] = None
    return value

def outputstack():
    global baseptr, topofstack, stack
    for i in range(5):
        print(i, stack[i])

initiallise()
print("1:push\n2:pop\n3:output\n4:End")
choice = int(input("please enter your choice"))
while choice != 4:
    if choice == 1:
        data = input("enter value")
        push(data)
    elif choice == 2:
        value = pop()
        print("value pop is", value)
    elif choice == 3:
        outputstack()

    choice = int(input("please enter your choice"))
