f = open('in1.txt')

R_SCORE = 1
P_SCORE = 2
S_SCORE = 3

lose_score = 0
draw_score = 3
win_score = 6

OPP_ROCK = 'A'
OPP_PAPER = 'B'
OPP_SCISSORS = 'C'

OWN_ROCK = 'X'
OWN_PAPER = 'Y'
OWN_SCISSORS = 'Z'

def get_symbol_score(symbol):
    if symbol == OWN_ROCK:
        return R_SCORE

    if symbol == OWN_PAPER:
        return P_SCORE
    
    if symbol == OWN_SCISSORS:
        return S_SCORE
    

def get_match_score(arr):
    a = arr[0]
    b = arr[1]
    outcome_score = 0
    if a == OPP_ROCK:
        if b == OWN_ROCK:
            outcome_score = 3
        if b == OWN_PAPER:
            outcome_score = 6

    if a == OPP_PAPER:
        if b == OWN_PAPER:
            outcome_score = 3
        if b == OWN_SCISSORS:
            outcome_score = 6

    if a == OPP_SCISSORS: 
        if b == OWN_SCISSORS:
            outcome_score = 3
        if b == OWN_ROCK:
            outcome_score = 6

    return outcome_score + get_symbol_score(b)

scores = []

with open('in1.txt') as file:
    scores = map(get_match_score, [line.replace('\n', '').split(' ') for line in file])

print(sum(list(scores)))
su