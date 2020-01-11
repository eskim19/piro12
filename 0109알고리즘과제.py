var=int(input('Input your number: '))
ans_list=[]

for i in range (1,1000001):
    d=list(map (int,str(i)))
    f=i
    for j in range(len(d)):
        f+=d[j]
    if f==var:
        ans_list.append(i)

if len(ans_list)==0:
    print(0) #There is no answer
else:
    print(min(ans_list)) #Print the minimum number from the list
