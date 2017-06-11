from random import randint

fname = input("Please, enter the name of the output file: ")
if len(fname) < 1: fname = "input/input.txt"

count_str = input("Please, enter the number of elements: ")
count = int(count_str)

fhandle_write = open(fname, "w")
for i in range(count):
    num = randint(0, 100000)
    fhandle_write.write(str(num) + "\n")

