#if we look at one side of the street and mark X as a plot where building is allowed and Y as a free plot, we have; XYX, YXY, YYX, XXY,YYY. Because the same number exists on the other side, we have 5*5=25 combinations.
# input = 3
# Output = 25

from itertools import product
M = int(input(" "))
cnt = 0
l = []

for w in product(['x','y'], repeat=M):
    tmp = ''.join(w)
    if 'xx' not in tmp:
        l.append(tmp)
        cnt += 1
print(cnt*cnt)
print (l)