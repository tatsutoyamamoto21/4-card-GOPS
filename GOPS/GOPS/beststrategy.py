import itertools
import numpy as np
from numbers import Number
from GOPS import payout2by2, payout3by3, payout4by4

def beststrategy(card, rem_cards, a_cards, b_cards, payoff=False):
    '''
    Returns best startegy for player A given the card, the remaining cards, the
    cards A has left and the cards B has left. Also returns payoff if payoff is
    set to True.
    
    Input:
    card: integer, the current card to bet on
    rem_cards: list, the remaining cards to bet on
    a_cards: list, Player A's cards
    b_cards: list, Player B's cards
    payoff: True or False, default is False

    Output:
    pay, strat: if payoff is true, tuple with pay as a number representing
    expected payoff and strat is a strategy array, where ith element
    corresponds to the probability player A should play the ith element in
    a_cards
    strat: if payoff is false, strat as above
    '''
    perms = list(itertools.permutations(rem_cards))
    for i, p in enumerate(perms):
        perms[i] = [card] + list(p)
    
    a = a_cards.copy()
    b = b_cards.copy()
    pay = 0

    if len(a_cards) == 4:
        strat = np.zeros(4)
        for p in perms:
            ret = payout4by4(p, a_cards, b_cards, moves=True)
            strat += ret[1][0]
            a_cards, b_cards = a.copy(), b.copy()
            if payoff:
                pay += ret[0][0]
        pay = pay/6

    
    elif len(a_cards) == 3:
        strat = np.zeros(3)
        for p in perms:
            ret = payout3by3(p, a_cards, b_cards, moves=True)
            strat += ret[1][0]
            a_cards, b_cards = a.copy(), b.copy()
            if payoff:
                pay += ret[0][0]
        pay = pay/2

    elif len(a_cards) == 2:
        strat = np.zeros(2)
        for p in perms:
            ret = payout2by2(p, a_cards, b_cards, moves=True)
            strat += ret[1][0]
            a_cards, b_cards = a.copy(), b.copy()
            if payoff:
                pay += ret[0][0]
        
    strat = strat/np.sum(strat)

    if payoff:
        if isinstance(pay, Number):
            return pay, strat
        else:
            return pay[0], strat

    return strat
