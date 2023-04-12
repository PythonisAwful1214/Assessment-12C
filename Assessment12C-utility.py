#   Nicolas Callier
#  ​ CSCI 102 – Section H
#   Assessment 12C
#   Time: 45 minutes

import math

def load_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip().split() for line in f]
    return lines

def update_string(string1, string2, index):
    string1 = list(string1)
    string1[index] = string2
    print("".join(string1))

def find_word_count(word_list, word):
    count = 0
    for w in word_list:
        count += w.count(word)
    return count

def score_finder(players, scores, player):
    player = player.capitalize()
    if player in players:
        index = players.index(player)
        print(f"{player} got a score of {scores[index]}")
    else:
        print("player not found")

def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.union(set2))

def intersect(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

def not_in(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.difference(set2))

def is_prime(n):
    if n <= 1:
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
