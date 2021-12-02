txtFile = open("list.txt","r")
txt1 = txtFile.read();
txt2 = txt1.split("\n")
txt3 = []
txtFile.close();
hor = 0
dep = 0
aim = 0

for i in range(len(txt2)):
  split = txt2[i].split(" ")
  txt3.append(split)

for k in range(len(txt3)):
  first = txt3[k][0]
  second = int(txt3[k][1])
  if first == 'forward':
    hor = hor + second
    dep = dep + (aim * second)
    print(hor)
    print(aim)
    print(dep)
    print("------------------")
  elif first == 'up':
    aim = aim - second
  elif first == 'down':
    aim = aim + second

print(dep*hor)
