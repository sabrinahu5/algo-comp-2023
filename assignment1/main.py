#!usr/bin/env python3
import json
import sys
import os
import numpy as np

INPUT_FILE = 'testdata.json' # Constant variables are usually in ALL CAPS

class User:
    def __init__(self, name, gender, preferences, grad_year, responses):
        self.name = name
        self.gender = gender
        self.preferences = preferences
        self.grad_year = grad_year
        self.responses = responses


# Takes in two user objects and outputs a float denoting compatibility
def compute_score(user1, user2):

    # initializing
    total_score = 0
    grade_weight = 5
    responses_weight = 2

    # if not match return
    if user1.gender == user2.gender:
        return 0.01

    # first weight grade level difference inversely
    total_score += 1.0/(grade_weight * (1 + abs(user1.grad_year - user2.grad_year)))

    # then weight response similarity inversely by frequency of each answer
    for i in range(len(user1.responses)):
        if user1.responses[i] == user2.responses[i]:
            total_score += 1.0/(responses_weight * (5 + answers_freq[i][user1.responses[i]]))

    return total_score


if __name__ == '__main__':
    # Make sure input file is valid
    if not os.path.exists(INPUT_FILE):
        print('Input file not found')
        sys.exit(0)

    users = []
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
        for user_obj in data['users']:
            new_user = User(user_obj['name'], user_obj['gender'],
                            user_obj['preferences'], user_obj['gradYear'],
                            user_obj['responses'])
            users.append(new_user)

    # initialize 2d array to store frequencies
    answers_freq = np.zeros((len(users[0].responses), 6))

    for i in range(len(users)-1):
        for j in range(i+1, len(users)):
            user1 = users[i]
            user2 = users[j]
            score = compute_score(user1, user2)
            print('Compatibility between {} and {}: {}'.format(user1.name, user2.name, score))

    # iterate through each person, track how many responses for each question (for later use)
    for i in range(len(users)):
        user = users[i]
        responses = user.responses
        for j in range(len(responses)):
            answers_freq[j][user.responses[j]] += 1

    



