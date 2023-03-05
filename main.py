nullptr = -1
freeptr = rootptr = 0
tree =[]

def initiallise():
    global treenode, tree, nullptr, freeptr, rootptr
    rootptr = nullptr
    freeptr = 0
    for index in range(5):
        tree.append(treenode(index+1, "", nullptr))
    tree[4].leftptr = nullptr

def insertnode(newitem):
    global treenode, tree, nullptr, freeptr, rootptr
    prenode = newnode = thisnode = 0
    turnedleft = False

    if freeptr == nullptr:
        print("overflow: no space left")
    else:
        newnode = freeptr
        tree[newnode].data = newitem
        freeptr = tree[freeptr].leftptr
        tree[newnode].leftptr = nullptr

        if rootptr == nullptr:
            rootptr = newnode

        else:
            thisnode = rootptr
            while thisnode != nullptr:
                prenode = thisnode
                if tree[thisnode].data > newitem:
                    turnleft = True
                    thisnode = tree[thisnode].leftptr
                else:
                    turnleft = False
                    thisnode = tree[thisnode].rightptr

            if turnleft == True:
                tree[prenode].leftptr = newnode
            else:
                tree[prenode].righttptr = newnode

def findnode(searchitem):
    global treenode, tree, nullptr, freeptr, rootptr
    thisnode = rootptr
    while (thisnode != nullptr and tree[thisnode].data != searchitem):
        if tree[thisnode].data > searchitem:
            thisnode = tree[thisnode].leftptr
        else:
            thisnode = tree[thisnode].rightptr
    return thisnode

def traverse(Root):
    global treenode, tree, nullptr, freeptr, rootptr
    if Root != nullptr:
        traverse(tree[Root].leftptr)
        print(tree[Root].data)
        traverse(tree[Root].rightptr)

def getoption():
    print("1: Add Data\n2: Find Node\n3: Traverse\n4: End")
    choice = int(input("Enter choice"))
    return choice

class treenode():
    def __init__(self, leftptr, data, rightptr):
        self.leftptr = leftptr
        self.data = data
        self.rightptr = rightptr

initiallise()
choice = getoption()
while choice  != 4:
    if choice == 1:
        Data = input("Enter data: ")
        insertnode(Data)
        traverse(rootptr)
    elif choice == 2:
        Data = input("Enter search data: ")
        thisptr = findnode(Data)
        if thisptr == nullptr:
            print("value not found...")
        else:
            print("value found at ", thisptr)
        for i in range(5):
            print(i, tree[i].leftptr, tree[i].data, tree[i].rightptr)
    elif choice  == 3:
        traverse(rootptr)
    choice = getoption()




