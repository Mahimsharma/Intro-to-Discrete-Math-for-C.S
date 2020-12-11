import itertools as it

def is_solution(perm):
    
    for i1 in range(0, len(perm)):
        for i2 in range(i1+1,len(perm)):
            if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
                return False

    return True

for perm in it.permutations(range(8)):
    if is_solution(perm):
        print(perm)
        exit(0)
