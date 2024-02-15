import string
dict={}
data=""
file=open("Testing_op.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-2]
#print(dict)
with open("Testing.txt") as f:
    while True:
        c= f.read(1)
        if not c:
            print("EOF!!")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)

file.close()
with open("Testing_op.txt","r+") as myfile:
    print(myfile.read())

myfile.close()