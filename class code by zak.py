def unknown(x,y):
    value = 1
    while (x != y):
        if x < y:
            sum = x+y
            print(sum)
            value = (value * 2)
            x = x+1
        else:
            if x > y:
                sum = x+y
                print(sum)
                value = (value // 2)
                x = x-1
    return value



print(unknown(10,15))

print(unknown(10,10))

print(unknown(15,10))
