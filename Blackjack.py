"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    deck = [0, 'A', '2', '3', '4', '5', '6' , '7', '8', '9', '10',"K", 'J', 'Q']
    if card in deck:
        if deck.index(card) >=10:
            card = 10
            return card
        else: 
            card = deck.index(card)
            return card
print(value_of_card('10'),value_of_card('A'))
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    if value_of_card(card_one) > value_of_card(card_two): return card_one
    else: return card_two
print(higher_card('K', '10'))
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one)+value_of_card(card_two) > 10:
        return 1
    if card_one == 'A' or card_two == 'A':
        return 1
    else: return 11
print(value_of_ace('6', 'K'))
print(value_of_ace('2', 'A'))
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) == 1 and value_of_card(card_two) == 1:
        return False
    if value_of_card(card_one) == 1 or value_of_card(card_two) == 1:
        if value_of_card(card_one) in [1, 10] and value_of_card(card_two) in [1, 10]:
            return True
    if value_of_card(card_one) + value_of_card(card_two) == 21:
        return True
    else: 
        return False
print(is_blackjack('A', 'K'))
print(is_blackjack('Q', 'K'))
print(is_blackjack('A', 'A'))
print(is_blackjack('10', 'A'))
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:return False
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    if value_of_card(card_one) == 1 and value_of_card(card_two) == 1:
        return False
    if value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]:
        return True
    else: return False