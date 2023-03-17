rptr = fptr = 0
queue = []
ub = 4
qlen = 0
qfull = 5

def initiallise():
    global rptr, fptr, queue
    rptr = -1
    fptr = 0
    queue = [None for i in range (0, 5)]

def enqueue(value):
    global rptr, fptr, queue, ub, qlen, qfull
    if qlen < qfull:
        if rptr < ub:
            rptr += 1
        else:
            rptr = 0
        queue[rptr] = value
        qlen = qlen + 1
    else:
        print("overflow no space")

def dequeue():
    global rptr, fptr, queue, ub, qlen
    if qlen == 0:
        print("under flow no data in queue")
    else:
        value = queue[fptr]
        queue[fptr] = None
        if fptr == ub:
            fptr = 0
        else:
            fptr +=1
        qlen = qlen - 1
        return value

def outputqueue():
    global rptr, fptr, queue, ub, qlen
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