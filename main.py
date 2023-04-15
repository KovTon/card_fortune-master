from typing import List, Dict, Any, Optional
import random


class Card():
    def __init__(self, value: int, rank: str, suit: str) -> None:
        self.value = value
        self.rank = rank
        self.suit = suit


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []


# Card = Dict[str, Any]
# Player = Dict[str, Any]


def get_grade(number: int):
    grades = {11: "V", 12: "Q", 13: "K", 14: "A"}
    if number in grades:
        return grades[number]
    return str(number)


def generate_deck(suits: List[str], values: List[int]):
    deck = []
    for suit in suits:
        for value in values:
            card = Card(value, get_grade(value), suit)
            deck.append(card)
    return deck


def generate_standard_deck():
    suits = ["♠", "♦", "♥", "♣"]
    values = list(range(2, 15, 1))
    deck = generate_deck(suits, values)
    return deck


def generate_single_suite_deck():
    suits = ["♠"]
    values = list(range(2, 15, 1))
    deck = generate_deck(suits, values)
    return deck


def generate_double_suite_deck():
    suits = ["♠", "♦"]
    values = list(range(2, 15, 1))
    deck = generate_deck(suits, values)
    return deck


def pull_random_card(deck: List[Card]) -> Card:
    card_index = random.randint(0, len(deck)-1)
    card = deck.pop(card_index)
    return card


def cards_are_equal(card_1: Card, card_2: Card) -> bool:
    return card_1.value == card_2.value


def start_round(deck: List[Card], player_1: Player, player_2: Player):
    player_1_card = pull_random_card(deck)
    player_2_card = pull_random_card(deck)
    if cards_are_equal(player_1_card, player_2_card):
        return

    if player_1_card.value > player_2_card.value:
        hand_1: List[Card] = player_1.hand
        # добавить в руку
        hand_1.append(player_1_card)
    else:
        # получить руку
        hand_2: List[Card] = player_2.hand
        # добавить в руку
        hand_2.append(player_2_card)


def introduce_game(deck):
    print(f'вы играете колодой из {len(deck)} карт')


def start_game_loop(deck: List[Card], player_1: Player, player_2: Player):
    while deck:  # неявная конвертация из list в bool. Явная когда вызвали
        start_round(deck, player_1, player_2)


def show_results(player_1: Player, player_2: Player):
    print(len(player_1.hand), len(player_2.hand))


def define_winner(player_1: Player, player_2: Player) -> Optional[Player]:
    if len(player_1.hand) > len(player_2.hand):
        return player_1
    else:
        return player_2
    return None


def announce_winner(winner: Optional[Player]) -> None:
    if winner is None:
        print('draw')
    else:
        print(f'winner {winner.name}')


def main():
    # player_1 = {'name': 'Ivan', 'hand': []}
    # player_2 = {'name': 'Pavel', 'hand': []}
    player_1 = Player('Pavel')
    player_2 = Player('Ivan')
    deck = generate_standard_deck()
    random.shuffle(deck)
    introduce_game(deck)
    start_game_loop(deck, player_1, player_2)
    announce_winner(define_winner(player_1, player_2))
    show_results(player_1, player_2)


if __name__ == '__main__':
    main()
