from copy import deepcopy
from collections import defaultdict
import random
import itertools
import ast


VALUE = 0
SUIT = 1

WILD = 25
SKIP = 15

DECK_PICKUP = 'XX'

ACE = 'A'

MAX_VALUE = 13
MIN_VALUE = 2

ACC_ACE_VALUE = 1

VALUES = {'K': MAX_VALUE,
          'Q': 12,
          'J': 11,
          '0': 10,
          '9': 9,
          '8': 8,
          '7': 7,
          '6': 6,
          '5': 5,
          '4': 4,
          '3': 3,
          '2': MIN_VALUE,
          ACE: WILD}

ACC_VALUES = VALUES.copy()
ACC_VALUES[ACE] = ACC_ACE_VALUE

SUITS = set('SHDC')

BLACK = 0
RED = 1

SUIT_COLOURS = {'S': BLACK,
                'H': RED,
                'D': RED,
                'C': BLACK}



PLAYERS = 4

# minimum number of natural cards in a phase
MIN_NATURAL_CARDS = 2

# elements of turn 2-tuple
TURN_PLAYER_ID = 0
TURN_PLAYS = 1


# elements of play 2-tuple
PLAY_TYPE = 0
PLAY_CARDS = 1

# elements of table 2-tuple
TABLE_TYPE = 0
TABLE_GROUPS = 1

# play types
PICKUP_DECK_PLAY = 1
PICKUP_DISCARD_PLAY = 2
PHASE_PLAY = 3
PLACE_PLAY = 4
DISCARD_PLAY = 5

# phase types
PHASE_NUM3 = 1
PHASE_SUIT7 = 2
PHASE_ACC34 = 3
PHASE_NUM4 = 4
PHASE_RUN8 = 5
PHASE_CACC34 = 6
PHASE_CRUN4NUM4 = 7

# sub-phase types
GROUP_INVALID = []
GROUP_NUM3 = 1
GROUP_SUIT7 = 2
GROUP_NUM4 = 3
GROUP_RUN8 = 4
GROUP_CRUN4 = 5
GROUP_ACC34 = 6
GROUP_CACC34 = 7

# minimum number of cards needed to make 34-acc
MIN_ACC34_CARDS = 3

ACC_SERIES = (34, 21, 13, 8, 5, 3, 2, 1, 1)


# group sizes
GROUPSIZE_SAMEVAL3 = 3
GROUPSIZE_SAMEVAL4 = 4
GROUPSIZE_RUN = 8
GROUPSIZE_CRUN4 = 4
GROUPSIZE_SAMESUIT = 7


TABLE_EMPTY_PHASE = (None, [])



HUMAN = 'manual'


HAND_SIZE = 10



import player1 as player1
import player2 as player2
import player3 as player3

import program as valid



play = [player1.phazed_play, 
        player2.phazed_play,
        player3.phazed_play,
        HUMAN]

random.shuffle(play)



def interactive_game(bonus=False, verbatim=True):
    global play
    global scores
    global phase_status
    global hand_number
    
    deck = [val+suit for i in range(2) for val,suit in itertools.product(VALUES, SUITS)]
    random.shuffle(deck)
    player_hands = [[], [], [], []]

    for i in range(PLAYERS):
        for j in range(HAND_SIZE):
            player_hands[i].append(deck.pop())

    prev_tricks = []
    discard_pile = [None, deck.pop()]
    table = [(None, []) for i in range(PLAYERS)]
    turn_history = []

    player_seq = itertools.cycle(range(PLAYERS))

    for i in range(hand_number):
        next(player_seq)
    

    game_over = False
    for player_id in player_seq:
        plays = []
        while True:
            if play[player_id] == HUMAN:
                sorted_hand = sorted(player_hands[player_id], key=lambda x: VALUES[x[VALUE]])
                print(f"\n== Game state (Player {player_id}) ==\n\n\ttable: {table}\n\tturn_history: {turn_history}\n\tphase_status: {phase_status}\n\thand: {sorted_hand}\n\tdiscard top: {repr(discard_pile[-1])}\n")
                while True:
                    try:
                        attempted_play = ast.literal_eval(input("Enter play: "))
                        play_type, play_content = attempted_play
                        assert(type(play_type) == int and PICKUP_DECK_PLAY <= play_type <= DISCARD_PLAY)
                        # if play_type == PHASE_PLAY:
                        #     played_cards = []
                        #     phase_type, phase = play_content
                        #     for group in phase:
                        #         played_cards.append([])
                        #         for card_id in group:
                        #             played_cards[-1].append(sorted_hand[card_id])
                        #     play_content = (phase_type, played_cards)
                        assert(valid.phazed_is_valid_play((play_type, play_content), player_id, table, turn_history, phase_status, player_hands[player_id], discard_pile[-1]))
                        break
                    except (TypeError, AssertionError, ValueError, SyntaxError, IndexError) as e:
                        print(f"ERROR: Enter a valid play ({e})")
            else:
                if not player_hands[player_id]:
                    game_over = True
                    break
                play_type, play_content = play[player_id](player_id, deepcopy(table), deepcopy(turn_history), deepcopy(phase_status), deepcopy(player_hands[player_id]), discard_pile[-1])
            if play_type == PICKUP_DECK_PLAY:
                player_hands[player_id].append(deck.pop())
                turn_history.append((player_id, [(play_type, DECK_PICKUP)]))
            elif play_type == PICKUP_DISCARD_PLAY:
                player_hands[player_id].append(discard_pile.pop())
                turn_history.append((player_id, [(play_type, play_content)]))
            elif play_type == PHASE_PLAY:
                declared_phase_type, phase = play_content
                phase_type = valid.phazed_phase_type(phase)
                if declared_phase_type not in phase_type:
                    print("ERROR: invalid phase declaration")
                table[player_id] = (declared_phase_type, phase)
                turn_history[-1][1].append((play_type, play_content))
                phase_status[player_id] = declared_phase_type
                hand = player_hands[player_id]
                for group in phase:
                    for played_card in group:
                        for i, card in enumerate(hand):
                            if played_card == card:
                                hand.pop(i)
                                break
            elif play_type == PLACE_PLAY:
                played_card, (playto_player_id, playto_group_id, playto_id) = play_content
#                print("Play to play of {}, group {}, position {}".format(playto_player_id, playto_group_id, playto_id))
                group = table[playto_player_id][1][playto_group_id]
                table[playto_player_id][1][playto_group_id] = group[:playto_id] + [played_card] + group[playto_id:]
                turn_history[-1][1].append((play_type, play_content))
                hand = player_hands[player_id]
                for i, card in enumerate(hand):
                    if played_card == card:
                        hand.pop(i)
                        break
            elif play_type == DISCARD_PLAY:
                discard_pile.append(play_content)
                turn_history[-1][1].append((play_type, play_content))
                hand = player_hands[player_id]
                for i, card in enumerate(hand):
                    if card == play_content:
                        hand.pop(i)
                        break
                if not hand:
                    game_over = True
                break
            else:
                print("ERROR: invalid play")
        if game_over:
            print(f"\n== GAME END STATE ==\n\n\ttable: {table}\n\tturn_history: {turn_history}\n\tphase_status: {phase_status}\n\thand: {sorted_hand}\n\tdiscard top: {repr(discard_pile[-1])}\n")
            for player_id in range(PLAYERS):
                scores[player_id] += valid.phazed_score(player_hands[player_id])
            break
#[5, [['9C', 'AC', 'AS', 'QS', 'KS'], ['6D', '6H', '6S', '6S']]]

if __name__ == "__main__":
    hand_number = 0
    phase_status = [0, 0, 0, 0]
    scores = [0, 0, 0, 0]
    
    while True:
        interactive_game()
        print(f"\n\n**** END OF HAND ****\n\n\tscores: {scores}\n\n")
        response = input("Another hand (y/n)? ")
        hand_number += 1
        if response == 'n':
            print("\nBYEEEE!\n")
            break
