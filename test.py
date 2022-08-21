numlist = [1,1,1,0,0,0]

def ChainFinder(list,number):
    cont = 0
    maxcont = 0
    prev = list[0]
    for i in list:
        if i == number:
            if i != prev:
                cont = 1
        if i == prev == 1:
            cont += 1
        maxcont = max(maxcont,cont)
        prev = i
    return maxcont

print(ChainFinder(numlist,1))
