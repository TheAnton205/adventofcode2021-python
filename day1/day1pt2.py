txtFile = open("list.txt","r")
txt1 = txtFile.read();
txt2 = txt1.split("\n")
txtFile.close();

counter = 0
increased = -1
addprev = 0

for i in range(len(txt2)):
  counter = i
  add = int(txt2[counter]) + int(txt2[counter+1]) + int(txt2[counter+2])

  i = i+4

  if add > addprev:
    print(str(add) + " increased!")
    increased = increased + 1
    print(increased)

  else:
    print(str(add) + " decreased!")
    print(increased)
  
  addprev = add
