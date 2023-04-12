#   Nicolas Callier
#  ​ CSCI 102 – Section H
#   Assessment 12C
#   Time: 2 hours

import math

def load_file(filename):
    with open(filename,'r') as text:
        lines = text.readlines()
    for i in range(0,len(lines)-1):
        lines[i] = lines[i][:-1]
    return lines

lines = load_file('test.txt') 
print("OUTPUT", lines)
    

def update_string(string1, string2, index):
    print(string1[:index] + string2 + string1[index+1:])
update_string("Hello World", 'yup', 3)

def find_word_count(lst, word):
    count = 0
    for line in lst:
        count += line.count(word)
    return count

def score_finder(players, scores, name):
    name = name.lower().capitalize()
    if name in players:
        idx = players.index(name)
        print(f"{name} got a score of {scores[idx]}")
    else:
        print("player not found")
players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
scores = [5, 8, 10, 6, 10, 4]
score_finder(players, scores, "jill")
score_finder(players, scores, "Manuel")

def union(lst1, lst2):
    return list(set(lst1) | set(lst2))
players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
union(scores, players2)
[5, 8, 10, 6, 4, "Melvin", "Martian", "Baka", "Xai", "Cody"]

def intersect(lst1, lst2):
    return list(set(lst1) & set(lst2))

def not_in(lst1, lst2):
    return list(set(lst1) - set(lst2))

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True

