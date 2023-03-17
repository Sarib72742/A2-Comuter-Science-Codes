class stacklist():
    def __init__(self):
        self.data = ""
        self.pointer = 0

freeptr = tos = baseptr = 0
stack =[stacklist() for i in range(5)]

def initiallise():
    global freeptr, tos, stack, stacklist
    freeptr = 0
    tos = -1
    for index in range(5):
        stack[index].pointer = index +1
    stack[4].pointer = -1

def push(value):
    global freeptr, tos, stack, stacklist
    if freeptr == -1:
        print("no space avaliable")
    else:
        newnode = freeptr
        stack[newnode].data = value
        freeptr = stack[freeptr].pointer
        stack[newnode].pointer = tos
        tos = newnode

def pop():
    global freeptr, tos, stack, stacklist
    if tos == -1:
        print("no data exist")
    else:
        value = stack[tos].data
        stack[tos].pointer = freeptr
        stack[tos].data = None
        freeptr = tos
        tos = tos-1
    return value

def post_order_traversal(tos):
    if tos is not None:
        post_order_traversal(stack[tos].pointer)
        print(stack[tos].data)

def outputstack():
    global freeptr, tos, stack, stacklist
    for i in range(5):
        print(i, stack[i].data, stack[i].pointer)

initiallise()
print("1:push\n2:pop\n3:output\n4:End")
choice = int(input("please enter your choice"))
while choice != 4:
    if choice == 1:
        data = input("enter value")
        push(data)
        post_order_traversal(tos)
    elif choice == 2:
        value = pop()
        print("value pop is", value)
    elif choice == 3:
        outputstack()

    choice = int(input("please enter your choice"))


