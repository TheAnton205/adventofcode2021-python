txtFile = open("list2.txt","r")
txt1 = txtFile.read();
txt2 = txt1.split("\n")
txtFile.close();
prevnum = 0
increased = 0

for i in range(len(txt2)):
    num = int(txt2[i])

    if num > prevnum:
        print(str(num) + " increased!")
        increased = increased + 1
        prevnum = num
    else:
        print(str(num) + " decreased!")
        prevnum = num

increased = increased-1
print("Total number of increased is " + str(increased))