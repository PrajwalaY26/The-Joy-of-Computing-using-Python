elements=int(input("Enter the number of elements : "))
mylist=[]
for _ in range(elements):
    mylist.append(input())
l=input("Enter whose anagram to be found")

for i in range(len(mylist)):
    if sorted(l)== sorted(mylist[i]):
        print("found")
        print(mylist[i])