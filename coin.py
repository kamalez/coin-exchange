arr=[int(n) for n in input().strip().split()]
tot=int(input())
ans=[]
tot+=1
for i in range(tot):
    if i in arr:
        ans.append([[i]])
    else:
        ans.append([])
for each in arr:
    for i in range(each,tot):
        for single in ans[i-each]:
            temp=list(single)
            temp.append(each)
            temp.sort()
            ans[i].append(temp)
for each in ans:
    temp=[]
    for e in each:
        if(e not in temp):
            temp.append(e)
    print(temp)