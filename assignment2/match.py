import numpy as np
from typing import List, Tuple

# makes matched boolean array
matched = [False] * 10

def run_matching(scores: List[List], gender_id: List, gender_pref: List) -> List[Tuple]:
    """
    TODO: Implement Gale-Shapley stable matching!
    :param scores: raw N x N matrix of compatibility scores. Use this to derive a preference rankings.
    :param gender_id: list of N gender identities (Male, Female, Non-binary) corresponding to each user
    :param gender_pref: list of N gender preferences (Men, Women, Bisexual) corresponding to each user
    :return: `matches`, a List of (Proposer, Acceptor) Tuples representing monogamous matches

    Some Guiding Questions/Hints:
        - This is not the standard Men proposing & Women receiving scheme Gale-Shapley is introduced as
        - Instead, to account for various gender identity/preference combinations, it would be better to choose a random half of users to act as "Men" (proposers) and the other half as "Women" (receivers)
            - From there, you can construct your two preferences lists (as seen in the canonical Gale-Shapley algorithm; one for each half of users
        - Before doing so, it is worth addressing incompatible gender identity/preference combinations (e.g. gay men should not be matched with straight men).
            - One easy way of doing this is setting the scores of such combinations to be 0
            - Think carefully of all the various (Proposer-Preference:Receiver-Gender) combinations and whether they make sense as a match
        - How will you keep track of the Proposers who get "freed" up from matches?
        - We know that Receivers never become unmatched in the algorithm.
            - What data structure can you use to take advantage of this fact when forming your matches?
        - This is by no means an exhaustive list, feel free to reach out to us for more help!
    """
    matches = [()]

    proposers = [0, 1, 2, 3, 4]
    acceptor = [5, 6, 7, 8, 9]


    rows, cols = (10, 5)
    pref_lists = [[0 for i in range(cols)] for j in range(rows)]

    # iterates through each proposer
    for i in range(0,10):
        if (0 <= i <= 4):
            # preference scores for proposer for the acceptors
            curr_prefs = scores[i][5:10]
            tmp = scores[i][5:10]
        
            # sorts the scores
            curr_prefs = sort(curr_prefs)

            # iterates through preference scores for acceptors
            for j in range(0, 5):
                for k in range(0, 5):
                    if curr_prefs[j] == tmp[k]:
                        pref_lists[i][j] = k+5
                        break
        elif (5 <= i <= 9):
            # preference scores for proposer for the acceptors
            curr_prefs2 = scores[i][0:5]
            tmp2 = scores[i][0:5]
        
            # sorts the scores
            curr_prefs2 = sort(curr_prefs2)

            # iterates through preference scores for acceptors
            for j in range(0, 5):
                for k in range(0, 5):
                    if tmp2[k] == curr_prefs2[j]:
                        pref_lists[i][j] = k
                        break

    
    for i in range(0, 10):
        print(pref_lists[i])


    while not allMatched:
        # iterates through proposers
        for i in range(0, 5):
            if matched[i] == True:
                break

            curr = pref_lists[i]
            prospect = 0
            if gender_id[curr[prospect]] != gender_pref[i]:
                prospect += 1
                continue

            if matched[curr[prospect]] == True:
                prospect += 1
                continue

            matches[i] = (i, prospect)
            matched[i] = True
            matched[prospect] = True


    #for match in matches:
        #print (match[0] + " matched with " + match[1])
        #print()

    return matches


def allMatched() -> bool:
    for i in range(len):
        if not matched[i]:
            return False
    
    return True


def sort(curr_prefs):
     
    arr = curr_prefs
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    raw_scores = np.loadtxt('raw_scores.txt').tolist()
    genders = []
    with open('genders.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            genders.append(curr)

    gender_preferences = []
    with open('gender_preferences.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            gender_preferences.append(curr)

    gs_matches = run_matching(raw_scores, genders, gender_preferences)
