test_cases = {
    "phazed_group_type":
    [
        ("""submission.phazed_group_type(['2H', '2S', '2C'])""", [1]), 
        ("""submission.phazed_group_type(['AH', '2S', '2C'])""", [1]), 
        # INVALID: not enough natural cards
        ("""submission.phazed_group_type(['AH', '2S', 'AC'])""", []), 
        ("""submission.phazed_group_type(['2S', '3S', '4S', '5S', '6S', '7S', '8S'])""", [2]), 
        ("""submission.phazed_group_type(['2S', '3S', '4S', '5S', '6S', 'AC', '7S'])""", [2]), 
        # INVALID: too many cards for set of 7; order/composition wrong for run of 8
        ("""submission.phazed_group_type(['2S', '3S', '4S', '5S', '6S', 'AC', '7S', '7S'])""", []), 
        ("""submission.phazed_group_type(['2S', '2S', '2C', '2H'])""", [3]), 
        ("""submission.phazed_group_type(['AC', '2S', '2S', '2C'])""", [3]), 
        # INVALID: not enough natural cards
        ("""submission.phazed_group_type(['2S', '2S', '2C', '3H'])""", []), 
        # INVALID: not enough natural cards
        ("""submission.phazed_group_type(['AC', 'AS', 'AS', '2C'])""", []), 
        # INVALID: not enough natural cards
        ("""submission.phazed_group_type(['AC', 'AS', 'AC', 'AH'])""", []), 
        ("""submission.phazed_group_type(['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9H'])""", [4]), 
        ("""submission.phazed_group_type(['2S', '3S', '4S', '5S', '6S', '7S', 'AS', '9H'])""", [4]), 
        ("""submission.phazed_group_type(['AC', '2S', '3S', '4S', '5S', '6S', '7S', 'AS'])""", [4]), 
        # INVALID: wrong order for run
        ("""submission.phazed_group_type(['2S', '3S', '4S', '5S', '6S', '7S', '9H', 'AS'])""", []), 
        # INVALID: wrong cards for run (gap at end)
        ("""submission.phazed_group_type(['2S', '3S', '4S', '5S', '6S', '7S', '8S', '0H'])""", []), 
        ("""submission.phazed_group_type(['2S', '3S', '4S', '5S'])""", [5]), 
        ("""submission.phazed_group_type(['2C', '3S', '4C', '5S'])""", [5]), 
        ("""submission.phazed_group_type(['2C', 'AH', '4C', 'AD'])""", [5]), 
        # INVALID: run of *five* not four
        ("""submission.phazed_group_type(['2C', 'AH', '4C', 'AD', '6S'])""", []), 
        # INVALID: wrong order for run
        ("""submission.phazed_group_type(['AH', '2C', '4C', 'AD'])""", []), 
        # INVALID: not enough natural cards
        ("""submission.phazed_group_type(['AH', '2C', 'AC', 'AD'])""", []), 
        # INVALID: colour mismatch for same-colour run of 4
        ("""submission.phazed_group_type(['2C', '3S', '4C', '5H'])""", []), 
        # INVALID: wrong order for run
        ("""submission.phazed_group_type(['2C', '3S', '4C', 'KS'])""", []), 
        # INVALID: wrong order for run (x2)
        ("""submission.phazed_group_type(['AH', '3S', '4C', 'KS'])""", []), 
        # INVALID: wrong order for run (x2)
        ("""submission.phazed_group_type(['AH', '2C', '3S', 'KS'])""", []), 
        # INVALID: wrong order for run (x2)
        ("""submission.phazed_group_type(['AH', '3S', 'AC', 'KS'])""", []), 
        ("""submission.phazed_group_type(['AH', '3S', 'AC', 'KS', 'KH', '3C'])""", [6]), 
        ("""submission.phazed_group_type(['AS', '3S', 'AC', 'KS', 'KC', '3C'])""", [6, 7]), 
        ("""submission.phazed_group_type(['AH', '3S', 'AC', 'KS', 'KC', '3C'])""", [6]), 
        ("""submission.phazed_group_type(['KH', 'KC', '8H'])""", [6]), 
    ],

    "phazed_phase_type":
    [
        # two sets of three of same value (basic case)
        ("""submission.phazed_phase_type([['9D', '9S', '9D'], ['0D', '0S', '0D']])""", [1]), 
        # two sets of three of same value (case where value is the same)
        ("""submission.phazed_phase_type([['9D', '9S', '9D'], ['9H', '9S', '9H']])""", [1]), 
        # INVALID version of two sets of three of same value, as TOO MANY Wilds
        ("""submission.phazed_phase_type([['9D', '9S', 'AD'], ['6D', 'AS', 'AD']])""", []), 
        # INVALID version of two sets of three, as one set is all Wilds
        ("""submission.phazed_phase_type([['9D', '9S', 'AD'], ['AC', 'AS', 'AD']])""", []), 

        # one set of seven cards of same suit (basic case)
        ("""submission.phazed_phase_type([['9D', '7D', '9D', '2D', '0D', '0D', 'KD']])""", [2]), 
        # one set of seven cards of same suit (with Wilds)
        ("""submission.phazed_phase_type([['9D', '7D', 'AH', '2D', '0D', 'AS', 'KD']])""", [2]), 
        # INVALID set of seven cards of same suit (as ALL Wilds)
        ("""submission.phazed_phase_type([['AD', 'AD', 'AH', 'AH', 'AS', 'AS', 'AC']])""", []), 
        # INVALID one set of cards of same suit, as wrong number
        ("""submission.phazed_phase_type([['9D', '7D', 'AH', '2D', '0D', 'AS', 'KD', 'JD']])""", []), 

        # two 34-accumulations (basic case)
        ("""submission.phazed_phase_type([['2C', 'KH', 'QS', '7H'], ['3H', '7S', '0D', 'KD', 'AD']])""", [3]),
        # INVALID two 34-accumulations (second adds up to 35)
        ("""submission.phazed_phase_type([['2C', 'KH', 'QS', '7H'], ['3H', '7S', '0D', 'KD', '2D']])""", []),

        # two sets of four of same value (basic case)
        ("""submission.phazed_phase_type([['9D', '9S', '9D', '9C'], ['0D', '0S', '0D', '0H']])""", [4]), 
        # two sets of four of same value (case where value is the same)
        ("""submission.phazed_phase_type([['9D', '9S', '9D', '9C'], ['9H', '9S', '9H', '9C']])""", [4]), 
        # INVALID version of two sets of four of same value, as TOO MANY Wilds
        ("""submission.phazed_phase_type([['9D', '9S', 'AD', '9H'], ['6D', 'AS', 'AD', 'AH']])""", []), 
        # INVALID version of two sets of four, as one set is all Wilds
        ("""submission.phazed_phase_type([['9D', '9S', 'AD', '9H'], ['AC', 'AS', 'AD', 'AH']])""", []), 

        # one run of eight cards (basic case)
        ("""submission.phazed_phase_type([['2D', '3C', '4D', '5S', '6C', '7D', '8H', '9S']])""", [5]), 
        # INVALID run of eight cards (out of order)
        ("""submission.phazed_phase_type([['3C', '2D', '4D', '5S', '6C', '7D', '8H', '9S']])""", []), 
        # one run of eight cards (with Wilds)
        ("""submission.phazed_phase_type([['3C', 'AD', '5S', '6C', '7D', '8H', 'AC', 'AS']])""", [5]), 
        # one run of eight cards (with Wilds, incl at start)
        ("""submission.phazed_phase_type([['AH', 'AC', 'AD', '5S', '6C', '7D', '8H', '9S']])""", [5]), 
        # one run of eight cards (with first Wild assigned to King)
        ("""submission.phazed_phase_type([['AD', '2D', '3C', 'AD', '5S', '6C', '7D', '8H']])""", [5]), 

        # two 34-accumulations of same colour (basic case)
        ("""submission.phazed_phase_type([['2C', 'KC', 'QS', '7C'], ['3H', '7H', '0D', 'KD', 'AD']])""", [3, 6]),
        # INVALID two 34-accumulations (second adds up to 35)
        ("""submission.phazed_phase_type([['2C', 'KC', 'QS', '7C'], ['3H', '7H', '0D', 'KD', '2D']])""", []),

        # one run of four cards of same colour + one set of four of same value (basic case)
        ("""submission.phazed_phase_type([['2D', '3H', '4D', '5D'], ['7C', '7D', '7H', '7C']])""", [7]), 
        # one run of four cards of same colour + one set of four of same value (with Wilds)
        ("""submission.phazed_phase_type([['AD', '3H', '4D', '5D'], ['7C', '7D', 'AH', '7C']])""", [7]), 
        # one run of four cards of same colour + one set of four of same value (order wrong)
        ("""submission.phazed_phase_type([['7C', '7D', '7H', '7C'], ['2D', '3H', '4D', '5D']])""", []), 
        # one run of four cards of same colour + one set of four of same value (Wild in run wraps around to King)
        ("""submission.phazed_phase_type([['AC', 'AD', '3H', '4D'], ['7C', '7D', 'AH', '7C']])""", [7]), 
        # one run of four cards of same colour + one set of four of same value (with Wilds)
        ("""submission.phazed_phase_type([['AD', '3D', '4D', '5D'], ['7C', '7D', 'AH', '7C']])""", [7]),
        # INVALID run of four cards of same colour + one set of four of same value (run out of order)
        ("""submission.phazed_phase_type([['AD', '4D', '3D', '5D'], ['7C', '7D', 'AH', '7C']])""", []), 

        # # INVALID phase (set of three and set of four)
        # ("""submission.phazed_phase_type([['9D', '9S', 'AD'], ['AC', 'AS', 'AD', 'AH']])""", []), 
        # ("""submission.phazed_phase_type([['7D', '7S', '7H'], ['8D', '8S', '8D']])""", [1]), 
        # ("""submission.phazed_phase_type([['7D', '7S', 'AH'], ['8D', 'AS', '8D']])""", [1]), 
        # ("""submission.phazed_phase_type([['7D', '7S', 'AH'], ['8D', 'AS', 'AD']])""", []), 
        # ("""submission.phazed_phase_type([['7D', '7S', 'AH'], ['8D', 'AS', '8D', '8H']])""", []), 
        # ("""submission.phazed_phase_type([['9D', '6D', '2D', '3D', '0D', '0D', 'JD']])""", [2]), 
        # ("""submission.phazed_phase_type([['9D', '6D', 'AS', '3D', '0D', '0D', 'JD']])""", [2]), 
        # ("""submission.phazed_phase_type([['9D', '6D', '2D', '3D', '0D', '0D']])""", []), 
        # ("""submission.phazed_phase_type([['9D', '6D', '2D', '3D', '0D', '0D', 'JD', 'QD']])""", []), 
        # ("""submission.phazed_phase_type([['7D', '7S', '7H', '7D'], ['8D', '8S', '8D', '8H']])""", [4]), 
        # ("""submission.phazed_phase_type([['AD', '7S', 'AH', '7D'], ['AD', '8S', '8D', 'AH']])""", [4]), 
        # ("""submission.phazed_phase_type([['7D', '7S', '7H', '7D', '7S'], ['8D', '8S', '8D', '8H']])""", []), 
        # ("""submission.phazed_phase_type([['AD', '7S', 'AH', '7D'], ['AD', '8S', 'AD', 'AH']])""", []), 
        # ("""submission.phazed_phase_type([['2D', '3C', '4D', '5H', '6C', '7D', '8H', '9S']])""", [5]), 
        # ("""submission.phazed_phase_type([['2D', 'AC', '4D', 'AH', '6C', '7D', '8H', 'AS']])""", [5]), 
        # ("""submission.phazed_phase_type([['AH', '2D', '3C', '4D', '5H', '6C', '7D', '8H']])""", [5]), 
        # ("""submission.phazed_phase_type([['2D', '3C', '4D', '5H', '6C', '7D', '8H', '9S', '0D']])""", []), 
        # ("""submission.phazed_phase_type([['2D', '3H', '4D', '5H'], ['6C', '6D', '6H', '6S']])""", [7]), 
        # ("""submission.phazed_phase_type([['2D', '3H', '4D', 'AH'], ['6C', 'AD', '6H', '6S']])""", [7]), 
        # ("""submission.phazed_phase_type([['2D', '3C', '4D', 'AH'], ['6C', 'AD', '6H', '6S']])""", []), 
        # ("""submission.phazed_phase_type([['2D', '3H', '4D', 'AH', '6H'], ['6C', 'AD', '6H', '6S']])""", []), 
    ],

    "phazed_is_valid_play":
    [
        ("""submission.phazed_is_valid_play((1, 'XX'), 0, [(None, []), (None, []), (None, []), (None, [])], [(0, [(1, 'XX')])], [3, 0, 0, 0], ['QC', 'KS', 'AH', 'AH', 'AD', 'AC', 'AC', 'AS', 'AH', 'KH', 'KS'], '7H')""", False),
        ("""submission.phazed_is_valid_play((2, '7H'), 0, [(None, []), (None, []), (None, []), (None, [])], [(0, [(1, 'XX')])], [3, 0, 0, 0], ['QC', 'KS', 'AH', 'AH', 'AD', 'AC', 'AC', 'AS', 'AH', 'KH', 'KS'], '7H')""", False),
        ("""submission.phazed_is_valid_play((3, (2, [['2C', 'AC', '4C', '5C', '6C', '7C', '8C']])), 0, [(None, []), (None, []), (None, []), (None, [])], [(0, [(1, 'XX')])], [1, 0, 0, 0], ['2C', '4C', '5C', '6C', '7C', '8C', '8C', '9C', 'AC', 'AS', 'KS'], '7S')""", True),
        ("""submission.phazed_is_valid_play((5, '7C'), 0, [(None, []), (None, []), (None, []), (None, [])], [(0, [(1, 'XX')])], [1, 0, 0, 0], ['2C', '4C', '5C', '6C', '7C', '8C', '8C', '9C', 'AC', 'AS', 'KS'], '7S')""", True),
        ("""submission.phazed_is_valid_play((5, '2S'), 0, [(None, []), (1, [['6C', '6S', '6D'], ['JC', 'JD', 'JH']]), (None, []), (None, [])], [(1, [(1, 'XX'), (5, 'QD')]), (2, [(1, 'XX'), (5, '0C')]), (3, [(1, 'XX'), (5, '4S')]), (0, [(1, 'XX'), (5, '3C')]), (1, [(1, 'XX'), (5, '0H')]), (2, [(1, 'XX'), (5, '9C')]), (3, [(2, '9C'), (5, '6S')]), (0, [(1, 'XX'), (5, 'JH')]), (1,  [(2, 'JH'),   (3, (1, [['6C', '6S', '6D'], ['JC', 'JD', 'JH']])),   (5, '4C')]), (2, [(1, 'XX'), (5, '9C')]), (3, [(2, '9C'), (5, '7H')]), (0, [(1, 'XX')])], [0, 1, 0, 0], ['2C', '2H', '5D', '6C', '8S', '0C', 'KD', 'AD', 'AD', '2S','KS'], 'QS')""", True),
        ("""submission.phazed_is_valid_play((3, (1, [['2C', '2H', '2S'], ['KS', 'KD', 'AD']])), 0, [(None, []), (1, [['6C', '6S', '6D'], ['JC', 'JD', 'JH']]), (None, []), (None, [])], [(1, [(1, 'XX'), (5, 'QD')]), (2, [(1, 'XX'), (5, '0C')]), (3, [(1, 'XX'), (5, '4S')]), (0, [(1, 'XX'), (5, '3C')]), (1, [(1, 'XX'), (5, '0H')]), (2, [(1, 'XX'), (5, '9C')]), (3, [(2, '9C'), (5, '6S')]), (0, [(1, 'XX'), (5, 'JH')]), (1,  [(2, 'JH'),   (3, (1, [['6C', '6S', '6D'], ['JC', 'JD', 'JH']])),   (5, '4C')]), (2, [(1, 'XX'), (5, '9C')]), (3, [(2, '9C'), (5, '7H')]), (0, [(1, 'XX')])], [0, 1, 0, 0], ['2C', '2H', '5D', '6C', '8S', '0C', 'KD', 'AD', 'AD', '2S', 'KS'], 'QS')""", True),
        ("""submission.phazed_is_valid_play((3, (4, [['2C', '2H', '2S', 'AD'], ['KS', 'KD', 'AD', 'AH']])), 0, [(None, []), (1, [['6C', '6S', '6D'], ['JC', 'JD', 'JH']]), (None, []), (None, [])], [(1, [(1, 'XX'), (5, 'QD')]), (2, [(1, 'XX'), (5, '0C')]), (3, [(1, 'XX'), (5, '4S')]), (0, [(1, 'XX'), (5, '3C')]), (1, [(1, 'XX'), (5, '0H')]), (2, [(1, 'XX'), (5, '9C')]), (3, [(2, '9C'), (5, '6S')]), (0, [(1, 'XX'), (5, 'JH')]), (1,  [(2, 'JH'),   (3, (1, [['6C', '6S', '6D'], ['JC', 'JD', 'JH']])),   (5, '4C')]), (2, [(1, 'XX'), (5, '9C')]), (3, [(2, '9C'), (5, '7H')]), (0, [(1, 'XX')])], [0, 1, 0, 0], ['2C', '2H', '5D', '6C', '8S', 'AH', 'KD', 'AD', 'AD', '2S', 'KS'], 'QS')""", False),
        ("""submission.phazed_is_valid_play((4, ('6C', (1, 0, 0))), 0, [(None, []), (1, [['6C', '6S', '6D'], ['JC', 'JD', 'JH']]), (None, []), (None, [])], [(1, [(1, 'XX'), (5, 'QD')]), (2, [(1, 'XX'), (5, '0C')]), (3, [(1, 'XX'), (5, '4S')]), (0, [(1, 'XX'), (5, '3C')]), (1, [(1, 'XX'), (5, '0H')]), (2, [(1, 'XX'), (5, '9C')]), (3, [(2, '9C'), (5, '6S')]), (0, [(1, 'XX'), (5, 'JH')]), (1,  [(2, 'JH'),   (3, (1, [['6C', '6S', '6D'], ['JC', 'JD', 'JH']])),   (5, '4C')]), (2, [(1, 'XX'), (5, '9C')]), (3, [(2, '9C'), (5, '7H')]), (0, [(1, 'XX')])], [0, 1, 0, 0], ['2C', '2H', '5D', '6C', '8S', 'AH', 'KD', 'AD', 'AD', '2S', 'KS'], 'QS')""", False),
        ("""submission.phazed_is_valid_play((3, (3, [['2C', 'KH', 'QS', '7H'], ['3H', '7S', '0D', 'KD', 'AD']])), 0, [(None, []), (None, []), (None, []), (None, [])], [(0, [(1, 'XX')])], [2, 0, 0, 0], ['2C', 'KH', 'QS', '7H', '3H', '7S', '0D', 'KD', 'AD', 'JS', '0H'], 'KC')""", True),
        ("""submission.phazed_is_valid_play((4, ('JS', (0, 0, 4))), 0, [(3, [['2C', 'KH', 'QS', '7H'], ['3H', '7S', '0D', 'KD', 'AD']]), (None, []), (None, []), (None, [])], [(0, [(1, 'XX'), (3, (3, [['2C', 'KH', 'QS', '7H'], ['3H', '7S', '0D', 'KD', 'AD']]))])], [3, 0, 0, 0], ['JS', '0H'], 'KC')""", True),
        ("""submission.phazed_is_valid_play((4, ('0H', (0, 0, 5))), 0, [(3, [['2C', 'KH', 'QS', '7H', 'JS'], ['3H', '7S', '0D', 'KD', 'AD']]), (None, []), (None, []), (None, [])], [(0, [(1, 'XX'), (3, (3, [['2C', 'KH', 'QS', '7H'], ['3H', '7S', '0D', 'KD', 'AD']])), (4, ('JS', (0, 0, 4)))])], [3, 0, 0, 0], ['0H'], 'KC')""", True),
        # INVALID attempt to discard without "completing" accumulation
        ("""submission.phazed_is_valid_play((5, '0H'), 0, [(3, [['2C', 'KH', 'QS', '7H', 'JS'], ['3H', '7S', '0D', 'KD', 'AD']]), (None, []), (None, []), (None, [])], [(0, [(1, 'XX'), (3, (3, [['2C', 'KH', 'QS', '7H'], ['3H', '7S', '0D', 'KD', 'AD']])), (4, ('JS', (0, 0, 4)))])], [3, 0, 0, 0], ['0H'], 'KC')""", False),
	],

    "phazed_score":
    [
        ("""submission.phazed_score(['2C', '2H', '5D', '6C', '8S', 'AH', 'KD', 'AD', 'AD', '2S', 'KS'])""", 126), 
        ("""submission.phazed_score(['7D', 'AH'])""", 32), 
        ("""submission.phazed_score(['4C', '7S', '9C', 'AH', 'AD', 'KD', '0D', '9D', '9S', '4D', '9C'])""", 124), 
        ("""submission.phazed_score(['2C', '4C', '5C', '6C', '7C', '8C', '8C', '9C', 'AC', 'AS', 'KS'])""", 112), 
        ("""submission.phazed_score(['2C', '4C'])""", 6), 
        ("""submission.phazed_score(['AC'])""", 25), 
    ],

}
