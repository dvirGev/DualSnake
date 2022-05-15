ls = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]]
newHead = ls[-1]
newHead=[6,6]
ls.append(newHead)
if newHead == [5,6]:
    pass
else:
    ls.pop(0)
print(ls)