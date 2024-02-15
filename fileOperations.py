with open("Testing.txt","r+") as myfile:
    print(myfile.read())
    myfile.write(" I am fine is overwritten!")
myfile.close()