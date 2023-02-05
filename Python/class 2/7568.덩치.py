class specs :
    def __init__(self,weight,height,idx,rank):
        self.weight = weight
        self.height = height
        self.idx = idx
        self.rank = rank

N = int(input())
people = list()
for i in range(N):
    weight, height = map(int,input().split())
    people.append(specs(weight,height,i,0))

people.sort(key=lambda x : x.weight, reverse=True)

for i in range(N):
    count = 0
    for j in range(i):
        if people[i].weight == people[j].weight:
            continue
        if people[i].height < people[j].height:
            count+=1
    people[i].rank = count+1

people.sort(key=lambda x : x.idx)

for person in people:
    print(person.rank)