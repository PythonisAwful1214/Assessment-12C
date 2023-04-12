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