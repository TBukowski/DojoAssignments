import random

def coin_toss(attempts):
    heads = 0
    tails = 0
    for flip in range(attempts):
        result = random.randint(0, 1)
        if result == 0:
            x = 'heads!'
            heads += 1
        else:
            x = 'tails!'
            tails += 1
        minStr = 'Flip # {}: It"s {} New total is {} head(s) and {} tail(s)'
        print minStr.format(flip + 1, x, heads, tails)

coin_toss(5000)