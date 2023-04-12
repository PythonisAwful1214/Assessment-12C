import math

def load_file(filename):
    with open(filename,'r') as text:
        lines = text.readlines()
    for i in range(0,len(lines)-1):
        lines[i] = lines[i][:-1]
    return lines

lines = load_file('test.txt') 
print("OUTPUT", lines)