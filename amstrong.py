print("program to check the given number amstrong or not")
cum=0
ams=input("enter the number ")
print(int(len(ams)))
for i in range(int(len(ams))):
        cum=cum+int(ams[i])**len(ams)
        print(cum)
if cum==int(ams):
            print("yes,it is armstrong number")
else:
            print("no, not a armstrong number")
