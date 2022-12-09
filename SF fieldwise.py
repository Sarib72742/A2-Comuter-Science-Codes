def addFWserialfile():
    sf = open("ALPHA.txt", "at")

    stname = input("enter student name")
    while stname != "":
        stclass = input("enterclass: ")
        stfee = float(input("enter fee: ")

        sf.write(stname + '\n')
        sf.write(stclass + '\n')
        sf.write(stfee + '\n')

        stname = input("enter student name")

    sf.close()

def readFWserialfile():
    sf = open("ALPHA.txt", "rt")
    stname = sf.readline()
    while sf != "":
        stclass = sf.readline()
        stfee = float(sf.readline)

        print(stname, end='')
        print(stclass, end='')
        print(stfee, end='')
        stname = sf.readline()
    sf.close()

def searchFWserialfile():
    found = False
    searchname = input("enter name to search: ")

    sf = open("ALPHA.txt" "rt")
    stname = sf.readfile()
    while sf != "":
        stclass = sf.readline()
        stfee = float(sf.readline)

        if stname[0:len(stname)-1] == searchname:
            found = true
            print(stname, end='')
            print(stclass, end='')
            print(stfee, end='')
            stname = sf.readline()
    if found = False:
        print("data not found")
    sf.close()

def deleteFWserialfile():
    found = False
    searchname = input("enter name to delete")

    sf = open("ALPHA.txt", "rt")
    tf = open("ALPHAt.txt", "wt")

    stname = sf.readline()
    while stname != "":
        stclass = sf.readline()
        stfee = float(sf . readline())

        if stname[0:len(stname) -1] != searchname:
            tf.write(stname)
            tf.write(stclass)
            tf.write(str(stfee) = '\n')
        else:
            found = True
        stname = sf.readline()
    if found = False:
        print("data des not exixt1:")
    else:
        print(searchname, "is deleted")
    sf.close()
    tf.close()
    os.remove("ALPHA.txt")
    os.rename("ALPHAt.txt", "ALPHA.txt")

def editFWserialfile():

    found = False
    searchname = input("enter name to delete")

    sf = open("ALPHA.txt", "rt")
    tf = open("ALPHAt.txt", "wt")

    stname = sf.readline()
    while stname != "":
        stclass = sf.readline()
        stfee = float(sf . readline())
        if stname[0:len(stname)-1] == searchname:
            print(stname, end='')
            print(stclass, end='')
            print(stfee, end='')

            print("Now reenter data for editing")
            stname = input("enter name: ")
            stclass = input("enter class: ")
            stfee = float(input("enterfee: ")
            found = True
        tf.write(stname)
        tf.write(stclass)
        tf.write(stfee)
        st.readline()

    if found = False:
        print("data des not exixt1:")
    else:
        print(searchname, "is edited")
    sf.close()
    tf.close()
    os.remove("ALPHA.txt")
    os.rename("ALPHAt.txt", "ALPHA.txt")

addFWserialfile()
