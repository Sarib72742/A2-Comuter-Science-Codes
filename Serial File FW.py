import os

def addfile():
    sf = open("Alpha.txt", "at")
    stname = input("please enter name ("" for ending): ")
    while stname != "":
        stclass = input("enter class: ")
        stfee = float(input("enter fees: "))

        sf.write(stname + '\n')
        sf.write(stclass + '\n')
        sf.write(str(stfee)+ '\n')

        stname = input("please enter name ("" for ending): ")

    sf.close()

def readfile():
    sf = open("Alpha.txt", "rt")
    stname = sf.readline()
    while stname != "":
        stclass = sf.readline()
        stfee = float(sf.readline())

        print(stname, end='')
        print(stclass, end='')
        print(str(stfee))

        stname = sf.readline()

    sf.close()

def searchfile():
    found = False
    searchname = input("enter name to search: ")
    sf = open("Alpha.txt", "rt")
    stname = sf.readline()
    while stname != "":
        stclass = sf.readline()
        stfee = sf.readline()

        if stname[0:len(stname)-1] == searchname:
            found = True
            print(stname, end='')
            print(stclass, end='')
            print(stfee)

        stname = sf.readline()

    if found == False:
        print("no item match")

    sf.close()


def deletefile():
    found = False
    deletename = input("please enter name to delete: ")

    sf = open("Alpha.txt", "rt")
    tf = open("tempAlpha.txt", "wt")

    stname = sf.readline()
    while stname != "":
        stclass = sf.readline()
        stfee = sf.readline()

        if stname[0:len(stname)-1] != deletename:
            tf.write(stname)
            tf.write(stclass)
            tf.write(str(stfee))
        else:
            found = True
        stname = sf.readline()

    if found is False:
        print(deletename, "is not found" )
    else:
        print(deletename, "is deleted")

    sf.close()
    tf.close()
    os.remove("Alpha.txt")
    os.rename("tempAlpha.txt", "Alpha.txt")

def editfile():
    found = False
    searchname = input("please enter name to edit: ")

    sf = open("Alpha.txt", "rt")
    tf = open("tempAlpha.txt", "wt")

    stname = sf.readline()
    while stname != "":
        stclass = sf.readline()
        stfee = sf.readline()

        if stname[0:len(stname)-1] == searchname:
            print(stname)
            print(stclass)
            print(stfee)

            print("Now enter the data which you want to edit")
            stname = input("enter name: ") + "\n"
            stclass = input("enter class:") + "\n"
            stfee = float(input("enter fee: "))
            found = True

        tf.write(stname)
        tf.write(stclass)
        tf.write(str(stfee))

        stname = sf.readline()

    if found is False:
        print(searchname, "is not found" )
    else:
        print(searchname, "is deleted")

    sf.close()
    tf.close()
    os.remove("Alpha.txt")
    os.rename("tempAlpha.txt", "Alpha.txt")

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

