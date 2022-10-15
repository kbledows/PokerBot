import itertools

cards = ['2s', '2h', '2d', '2c', '3s', '3h', '3d', '3c', '4s', '4h', '4d', '4c', '5s', '5h', '5d', '5c', '6s', '6h', '6d', '6c', '7s', '7h', '7d', '7c', '8s',
         '8h', '8d', '8c', '9s', '9h', '9d', '9c', 'Ts', 'Th', 'Td', 'Tc', 'Js', 'Jh', 'Jd', 'Jc', 'Qs', 'Qh', 'Qd', 'Qc', 'Ks', 'Kh', 'Kd', 'Kc', 'As', 'Ah', 'Ad', 'Ac']

possible_hands = itertools.combinations(cards, 5)

STier = ['AAo', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s',
         'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s', 'AKo',
         'KKo', 'KQs', 'KJs', 'KTs', 'AQo', 'KQo', 'QQo', 'QJs', 'QTs', 'AJo',
         'JJo', 'JTs', 'ATo', 'TTo', 'T9s', '99o', '88o', '77o', '66o', '65s', '55o']

ATier = ['KJo', 'QJo', 'K9s', 'K8s', 'Q9s',
         'J9s', '98s', '87s', '76s', '54s', '44o']

BTier = ['KTo', 'QTo', 'JTo', 'K7s', 'K6s', 'K5s', 'Q8s',
         'J8s', 'T8s', '97s', '86s', '75s', '33o', '22o']

CTier = ['K4s', 'K3s', 'K2s', 'Q7s', 'Q6s', 'Q5s', 'J7s', 'T7s', 'T6s', 'A9o', 'K9o', 'Q9o',
         'J9o', 'T9o', 'A8o', '98o', '96s', '85s', 'A7o', 'A6o', 'A5o', 'A4o', '64s', '53s', '43s']

DTier = ['Q4s', 'Q3s', 'Q2s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s', 'T5s', 'T4s', 'T3s', 'T2s', '95s', '94s', '84s', 'K8o', 'Q8o', 'J8o', 'T8o', 'K7o', 'Q7o',
         'J7o', 'T7o', '97o', '87o', '74s', '73s', 'K6o', 'Q6o', '86o', '76o', '63s', 'K5o', 'Q5o', '75o', '65o', '52s', 'K4o', '64o', '54o', '42s', 'A3o', '32s', 'A2o']
