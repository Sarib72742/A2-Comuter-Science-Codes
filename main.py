import os

def addfile():
    sf = open("AlphaR.txt", "at")
    stname = input("please enter name ("" for ending): ")
    while stname != "":
        stclass = input("enter class: ")
        stfee = float(input("enter fees: "))

        sf.write(stname + '#' + stclass + '#' + str(stfee) + "\n")
        stname = input("please enter name ("" for ending): ")

    sf.close()

def readfile():
    sf = open("AlphaR.txt", "rt")
    recline = sf.readline()
    while recline != "":
        fno = 0
        stname = ""
        stclass = ""
        stfee = ""

        for i in range(len(recline) - 1):
            mychar = recline[i]
            if mychar == "#":
                fno +=1
            elif fno == 0:
                stname = stname + mychar
            elif fno == 1:
                stclass = stclass + mychar
            else:
                stfee = stfee + mychar

        print(stname, stclass, stfee)
        recline = sf.readline()

    sf.close()

def searchfile():
    found = False
    searchname = input("enter name to search: ")
    sf = open("AlphaR.txt", "rt")
    recline = sf.readline()
    while recline != "":
        fno = 0
        stname = ""
        stclass = ""
        stfee = ""

        for i in range(len(recline) - 1):
            mychar = recline[i]
            if mychar == "#":
                fno += 1
            elif fno == 0:
                stname = stname + mychar
            elif fno == 1:
                stclass = stclass + mychar
            else:
                stfee = stfee + mychar

        if stname == searchname:
            found = True
            print(stname, stclass, stfee)
        recline = sf.readline()

    if found == False:
        print(searchname, "is not found")
    sf.close()


def deletefile():
    found = False
    deletename = input("please enter name to delete: ")

    sf = open("AlphaR.txt", "rt")
    tf = open("tempAlphaR.txt", "wt")

    recline = sf.readline()
    while recline != "":
        fno = 0
        stname = ""
        stclass = ""
        stfee = ""

        for i in range(len(recline) - 1):
            mychar = recline[i]
            if mychar == "#":
                fno += 1
            elif fno == 0:
                stname = stname + mychar
            elif fno == 1:
                stclass = stclass + mychar
            else:
                stfee = stfee + mychar

        if stname == deletename:
            found  = True
        else:
            tf.write(stname + "#" + stclass + "#" + stfee + "\n")
        recline = sf.readline()
    if found is False:
        print(deletename, "is not found")
    else:
        print(deletename, "is deleted")
    sf.close()
    tf.close()
    os.remove("AlphaR.txt")
    os.rename("tempAlphaR.txt", "AlphaR.txt")

def editfile():
    found = False
    searchname = input("please enter name to edit: ")

    sf = open("AlphaR.txt", "rt")
    tf = open("tempAlphaR.txt", "wt")

    recline = sf.readline()
    while recline != "":
        fno = 0
        stname = ""
        stclass = ""
        stfee = ""

        for i in range(len(recline) - 1):
            mychar = recline[i]
            if mychar == "#":
                fno += 1
            elif fno == 0:
                stname = stname + mychar
            elif fno == 1:
                stclass = stclass + mychar
            else:
                stfee = stfee + mychar

        if stname == searchname:
            print(stname, stclass, stfee)

            print("Now enter the data which you want to edit")
            stname = input("enter name: ")
            stclass = input("enter class:")
            stfee = float(input("enter fee: "))
            found = True

        tf.write(stname + "#" + stclass + "#" + str(stfee) + "\n")

        recline = sf.readline()

    if found is False:
        print(searchname, "is not found" )
    else:
        print(searchname, "is edited")

    sf.close()
    tf.close()
    os.remove("AlphaR.txt")
    os.rename("tempAlphaR.txt", "AlphaR.txt")

def options():
    print("1. add field per line wise")
    print("2. read field per line wise")
    print("3. search field per line wise")
    print("4. delete field per line wise")
    print("5. edit field per line wise")
    print("0. quit")
    x = int(input("enter option... "))
    return x

# main program
opt = options()
while opt != 0:
    if opt == 1: addfile()
    if opt == 2: readfile()
    if opt == 3: searchfile()
    if opt == 4: deletefile()
    if opt == 5: editfile()
    opt = options()
