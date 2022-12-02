f = open('in1.txt')

R_SCORE = 1
P_SCORE = 2
S_SCORE = 3

lose_score = 0
draw_score = 3
win_score = 6

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'


outcomes = {
    # SYMBOL: (Wins Against, Loses Against)
    ROCK: (SCISSORS, PAPER),
    PAPER: (ROCK, SCISSORS),
    SCISSORS: (PAPER, ROCK),
}

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

OWN_ROCK = LOSE
OWN_PAPER = DRAW
OWN_SCISSORS = WIN

# P1
def get_symbol_score(symbol):
    if symbol in [ROCK, OWN_ROCK]:
        return R_SCORE

    if symbol in [PAPER, OWN_PAPER]:
        return P_SCORE
    
    if symbol in [SCISSORS, OWN_SCISSORS]:
        return S_SCORE
    
def get_match_score(arr):
    a = arr[0]
    b = arr[1]
    outcome_score = 0
    if a == ROCK:
        if b == OWN_ROCK:
            outcome_score = 3
        if b == OWN_PAPER:
            outcome_score = 6

    if a == PAPER:
        if b == OWN_PAPER:
            outcome_score = 3
        if b == OWN_SCISSORS:
            outcome_score = 6

    if a == SCISSORS: 
        if b == OWN_SCISSORS:
            outcome_score = 3
        if b == OWN_ROCK:
            outcome_score = 6

    return outcome_score + get_symbol_score(b)

data = []

with open('in1.txt') as file:
    data = [line.replace('\n', '').split(' ') for line in file]

print("P1", sum(list(map(get_match_score, data))))


# P2
def get_required_outcome(arr):
    a = arr[0]
    b = arr[1]

    if arr[1] == DRAW:
        return arr[0]

    if arr[1] == WIN:
        return outcomes[arr[0]][1]

    if arr[1] == LOSE:
        return outcomes[arr[0]][0]

def get_match_score_improved(arr):
    required_outcome = get_required_outcome(arr)
    outcome_symbol_score = get_symbol_score(required_outcome)

    if arr[1] == LOSE:
        return outcome_symbol_score
    
    if arr[1] == WIN:
        return outcome_symbol_score + 6

    return outcome_symbol_score + 3


print("P2", sum(list(map(get_match_score_improved, data))))
