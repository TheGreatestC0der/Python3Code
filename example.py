f = open("numbers.txt", "w+")

for i in range(10):
  f.write("This is line %d\n" % (i+1))

f.close()
f = open("numbers.txt", "r")
content = f.readlines()
print(content)
f.close()

t = open("ishaan.txt", "w+")

t.write("Ishaan")

t.close()

t = open("ishaan.txt", "r")

name = t.readlines()
print(name[0].strip())
t.close()