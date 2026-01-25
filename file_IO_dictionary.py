#AM12 Project 2: File IO and Dictionaries
#Read each line from the given input file into a dictionary.
#Every other line, starting from the first line, is a key, 
#with the subsequent line being its value 
#(in other words, odd number lines contain a key,
#and the even number lines contain the corresponding value).

ninput = open("input.txt", "r")
nlist = ninput.readlines()
diction = {}
for i in range(0, len(nlist), 2):
    key = nlist[i].strip()
    value = nlist[i+1].strip()
    diction[key] = value
ninput.close()
print(diction)
