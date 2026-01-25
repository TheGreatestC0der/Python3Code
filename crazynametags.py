#AM12 Project 1: Crazy Name Tags Printer
#Write a program that asks the user for their 
#name and stores it in a variable, and then writes that name 
#to an output file with one letter on each line. 
#After writing the name normally, write every other letter of the name 
#(skipping the second letter, the fourth, the sixth, etc.). 
#Finally, write the name to the output file backwards!

name = input("What is your name?")
n = open("crazy.txt", "w+")
for i in range(len(name)):
    n.write(name[i] + "\n")
for i in range(0, len(name), 2):
    n.write(name[i] + "\n")
for i in range(len(name) - 1, -1, -1):
    n.write(name[i] + "\n")
n.close()
