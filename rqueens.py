c = 0
def check_diag(perm):
    x2 = len(perm) -1
    for i in range(x2-1,-1,-1):
        if(x2 - i == abs(perm[x2] - perm[i])):
            return True
    return False
    
def get_perm(perm,n):
    global c
    for i in range(0,n):
        if i not in perm:
            perm.append(i)
            if check_diag(perm) == False:
                get_perm(perm,n)
            perm.pop()
    if len(perm)== n:
        print(perm)
        c = c+1
get_perm([],8)
print(c)

