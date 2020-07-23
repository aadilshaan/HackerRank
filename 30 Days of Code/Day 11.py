# 2D Arrays

arr = []
hourglass = []
for _ in range(6):
    arr.append(list(map(int,input().rstrip().split())))
for x in range(0,4):
    for y in range(0,4):
        hglass = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        hourglass.append(hglass)
print(max(hourglass))
