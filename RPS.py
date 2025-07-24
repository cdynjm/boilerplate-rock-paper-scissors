# RPS.py

import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # Not enough history, pick random
    if len(opponent_history) < 3:
        return "R"

    # Count the most common move
    last = opponent_history[-1]
    counts = {'R': 0, 'P': 0, 'S': 0}
    for move in opponent_history:
        counts[move] += 1

    predict = max(counts, key=counts.get)

    # Counter the predicted move
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    return counter_moves[predict]
