LOSE_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

OWN_ROCK = LOSE
OWN_PAPER = DRAW
OWN_SCISSORS = WIN

symbol_scores = {
    OWN_ROCK: 1,
    OWN_PAPER: 2,
    OWN_SCISSORS: 3,
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

outcomes = {
    # SYMBOL: (Wins Against, Loses Against)
    ROCK: (SCISSORS, PAPER),
    PAPER: (ROCK, SCISSORS),
    SCISSORS: (PAPER, ROCK),
}

# P1
def get_symbol_score(symbol):
    return symbol_scores[symbol]
    
def get_match_score(arr):
    opp_symbol, own_symbol = arr
    outcome_score = LOSE_SCORE
    if opp_symbol is ROCK:
        if own_symbol is OWN_ROCK:
            outcome_score = DRAW_SCORE
        if own_symbol is OWN_PAPER:
            outcome_score = WIN_SCORE

    if opp_symbol is PAPER:
        if own_symbol is OWN_PAPER:
            outcome_score = DRAW_SCORE
        if own_symbol is OWN_SCISSORS:
            outcome_score = WIN_SCORE

    if opp_symbol is SCISSORS: 
        if own_symbol is OWN_SCISSORS:
            outcome_score = DRAW_SCORE
        if own_symbol is OWN_ROCK:
            outcome_score = WIN_SCORE

    return outcome_score + get_symbol_score(own_symbol)

# P2
def get_required_outcome(opp_symbol, outcome):
    if outcome is DRAW:
        return opp_symbol

    if outcome is WIN:
        return outcomes[opp_symbol][1]

    if outcome is LOSE:
        return outcomes[opp_symbol][0]

def get_match_score_improved(arr):
    opp_symbol, outcome = arr
    required_outcome_symbol = get_required_outcome(opp_symbol, outcome)
    outcome_symbol_score = get_symbol_score(required_outcome_symbol)

    if outcome is LOSE:
        return outcome_symbol_score
    
    if outcome is WIN:
        return outcome_symbol_score + WIN_SCORE

    return outcome_symbol_score + DRAW_SCORE

data = []
with open('in1.txt') as file:
    data = [line.replace('\n', '').split(' ') for line in file]

print("P1", sum(list(map(get_match_score, data))))
print("P2", sum(list(map(get_match_score_improved, data))))
