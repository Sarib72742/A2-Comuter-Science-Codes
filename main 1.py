rptr = fptr = 0
queue = []

def initiallise():
    global rptr, fptr, queue
    rptr = 0
    fptr = -1
    queue = [None for i in range (0, 5)]

def enqueue(value):
    global rptr, fptr, queue
    if rptr > 4:
        print("no space to edit")
    else:
        queue[rptr] = value
        rptr += 1
        if fptr == -1:
            fptr = 0

def dequeue():
    global rptr, fptr, queue
    if rptr == 0:
        print("no data in queue")
    else:
        value = queue[fptr]
        fptr +=1
    return value

def outputqueue():
    global rptr, fptr, queue
    print("Front pointer = ", fptr, "Rare pointer = ", rptr)
    for i in range(5):
        print(i, queue[i])

initiallise()
print("1:enqueue\n2:dequeue\n3:output\n4:End")
choice = int(input("please enter your choice"))
while choice != 4:
    if choice == 1:
        data = input("enter value")
        enqueue(data)
    elif choice == 2:
        value = dequeue()
        print("value pop is", value)
    elif choice == 3:
        outputqueue()

    choice = int(input("please enter your choice"))

