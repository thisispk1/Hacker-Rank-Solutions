def catAndMouse(x, y, z):
    if abs(z-x)<abs(y-z):
        return('Cat A')
    elif abs(z-x)==abs(y-z):
        return('Mouse C')
    else:
        return('Cat B')

q = int(input())

for q_itr in range(q):
    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    result = catAndMouse(x, y, z)