import random
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_cards_to_hand(self, cards):
        list_of_cards = []
        for card in cards:
            self.hand.append(card)
        return list_of_cards


class Card:
    fact = ""
    date = 0

    def __init__(self, fact, date):
        self.fact = fact
        self.date = date


def open_cards(file_c):
    # This method open the text file
    open_card = []
    with open(file_c, 'r') as file_r:
        for line in file_r:
            open_card.append(line.strip())
    return open_card


def one_card_more(cards):
    # this method add a card for the player or the board
    card_more = random.choice(cards)
    return card_more


def choose_cards(cards):
    # This method choose the cards from the player
    cards_for_player = random.sample(cards, 5)
    return cards_for_player


def remove_cards(cards_given, cards_board):
    # This method is to remove the cards given to the players or the board
    c = 0
    while c < len(cards_board):
        if cards_board[c] in cards_given:
            cards_board.remove(cards_board[c])
        else:
            c += 1
    return cards_board


def show_cards_for_player(cards):
    to_print_card = []
    for index, card in enumerate(cards):
        to_print = str([index, card.fact])
        to_print_card.append(to_print)
    for print in to_print_card:
        print_colored_text(print, 'cyan')


def show_cards(cards):
    to_print_card = []
    for index, card in enumerate(cards):
        to_print = str([index + 1, card.fact, card.date])
        to_print_card.append(to_print)
    for print in to_print_card:
        print_colored_text(print, 'red')


def wrong_answer_0(gender, cemetery, cards_board, cards_game, player):
    print(f"DAMN {gender}, YOU'RE WRONG :(")
    print("YOUR CARDS LOOK LIKE THIS NOW")
    cemetery.append(cards_board[0])
    cards_board.remove(cards_board[0])
    card_more = one_card_more(cards_game)
    cards_game.remove(card_more)
    player.append(card_more)
    return cemetery, cards_board, cards_game, player


def wrong_answer(gender, num, cemetery, cards_board, cards_game, player):
    print(f"DAMN {gender}, YOU'RE WRONG :(")
    print("YOUR CARDS LOOK LIKE THIS NOW")
    cemetery.append(cards_board[num])
    cards_board.remove(cards_board[num])
    card_more = one_card_more(cards_game)
    cards_game.remove(card_more)
    player.append(card_more)
    return cemetery, cards_board, cards_game, player


def correct_answer():
    print("WELL DONE, YOU HAVE ONE CARD LESS")
    print("YOUR CARDS LOOK LIKE THIS NOW")


def choose_of_player():
    while True:
        choose = input("WHAT CARD DO YOU WANT TO CHOOSE?").strip()
        if choose.isdigit():
            return int(choose)
        else:
            print("INVALID VALUE, IT MUST BE A NUMBER GREATER OR EQUAL TO 0")


def place_card(player):
    while True:
        place = input(f"WITH THE ABOVE, WHERE DO YOU WANT TO PUT IT {player}?").strip()
        if place.isdigit():
            return int(place)
        else:
            print("INVALID VALUE, IT MUST BE A NUMBER GREATER OR EQUAL TO 0")


def validate_cards_for_game(cards_game, cards_cemetery):
    empty = []
    if cards_game == empty:
        cards_game = cards_cemetery
        random.shuffle(cards_game)
        return cards_game
    else:
        return cards_game
        pass


def print_colored_text(text, color):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',
    }
    if color in colors:
        print(colors[color] + text + colors['reset'])
    else:
        print(text)


rounds = 0
correct_answers_p1 = 0
correct_answers_p2 = 0
wrong_answers_p1 = 0
wrong_answers_p2 = 0
cemetery_list = []
empty_list = []
cards_in_board = []
file = "cards.txt"
print("Hello, welcome to the Timeline Game")
name1 = input("Whats the name of the player 1?")
name1 = name1.upper()
gender1 = input("Are you man or woman?")
gender1 = gender1.upper()
print("Perfect, so let's continue")
name2 = input("Whats the name of the player 2?")
name2 = name2.upper()
gender2 = input("Are you man or woman?")
gender2 = gender2.upper()
print("So let's start the game. We will put one card on the board, then we'll give you 5 cards each one,")
print("from one of your cards "+name1+", you have to choose if the fact is before or after the card on the board,")
print("if you are correct, then will be the turn of "+name2+", but if you're wrong you have to take another card")
print("and put the chosen card in the cemetery. The winner will be the one who runs out of cards first")

# Open the file "cards.txt"
cards_f_g = open_cards(file)
# print(cards_f_g)
# Mix the cards for the game
random.shuffle(cards_f_g)
# Split the cards and convert to a Card object
cards_for_game = []
for card in cards_f_g:
    fact, date = card.split("/")
    ca_rd = Card(fact, date)
    cards_for_game.append(ca_rd)
# Add cards to the board
card_board = one_card_more(cards_for_game)
cards_in_board.append(card_board)
# Remove the card given to the board of the cards for the game
cards_for_game = remove_cards(cards_in_board, cards_for_game)
# print(cards_in_board)

# Deal cards to player 1
cards_p1 = choose_cards(cards_for_game)
cards_for_game = remove_cards(cards_p1, cards_for_game)
# Show to the player 1 their cards without the date(without using the object Player)

# Deal cards to player 2
cards_p2 = choose_cards(cards_for_game)
cards_for_game = remove_cards(cards_p2, cards_for_game)
# Show to the player 2 their cards without the date(without using the object Player)

player_1 = Player(name1)
player_1.add_cards_to_hand(cards_p1)
# Show to the player 1 their cards without the date
# show_cards_for_player(player_1.hand)

player_2 = Player(name2)
player_2.add_cards_to_hand(cards_p2)
# Show to the player 2 their cards without the date
# show_cards_for_player(player_2.hand)

print()
# Game cycle
while player_1.hand or player_2.hand:

    print()
    print_colored_text("CARDS ON BOARD", 'yellow')
    # Show the existent cards on the board
    show_cards(cards_in_board)
    print()
    print(f"IT'S YOUR TURN {player_1.name}")
    print("THESE ARE YOUR CARDS")
    show_cards_for_player(player_1.hand)
    print()
    print("(GIVE ME THE NUMBER THAT IT'S AT THE BEGINNING OF YOUR CHOICE)")
    choose_1 = choose_of_player()
    print(f"PERFECT, YOU WANT TO USE: {player_1.hand[choose_1].fact}")
    print()
    print("WE WILL TELL YOU HOW YOU SHOULD THROW, FOR EXAMPLE: ")
    print("IN CASE THAT THERE IS ONLY ONE CARD ON THE BOARD")
    print("USE 0 TO PUT BEFORE AND 1 TO PUT AFTER")
    print("IN CASE THAT THERE ARE MORE THAN ONE CARD ON THE BOARD")
    print("USE 0 TO PUT AT THE BEGINNING AND THE NUMBER AT THE BEGINNING\n"
          "OF THE LAST CARD TO PUT AT THE END OF THE CARDS")
    print("BUT IF YOU WANT TO PUT IT BETWEEN CARDS, ")
    print("THEN USE THE NUMBER OF THE CARD BEFORE THE PLACE YOU WANT TO PUT IT")
    print("FOR EXAMPLE:")
    print("CARD1, CARD2, CARD3, CARD4")
    print("IF YOU WANT TO PUT BETWEEN CARD3 AND CARD4 YOU SHOULD USE 3")
    place_1 = place_card(player_1.name)
    print()
    if place_1 == 0:
        cards_in_board.insert(place_1, player_1.hand[choose_1])
        player_1.hand.remove(player_1.hand[choose_1])
        print_colored_text("CARDS ON BOARD", 'yellow')
        show_cards(cards_in_board)
        print()
        cards_for_game = validate_cards_for_game(cards_for_game, cemetery_list)
        if cards_in_board[1].date < cards_in_board[0].date:
            cemetery_list, cards_in_board, cards_for_game, player_1.hand = wrong_answer_0(gender1,
                                                                                          cemetery_list,
                                                                                          cards_in_board,
                                                                                          cards_for_game,
                                                                                          player_1.hand)
            wrong_answers_p1 += 1
            show_cards_for_player(player_1.hand)
        else:
            correct_answer()
            correct_answers_p1 += 1
            show_cards_for_player(player_1.hand)
    else:
        cards_in_board.insert(place_1, player_1.hand[choose_1])
        player_1.hand.remove(player_1.hand[choose_1])
        print_colored_text("CARDS ON BOARD", 'yellow')
        show_cards(cards_in_board)
        print()
        cards_for_game = validate_cards_for_game(cards_for_game, cemetery_list)
        if cards_in_board[place_1].date < cards_in_board[place_1-1].date:
            cemetery_list, cards_in_board, cards_for_game, player_1.hand = wrong_answer(gender1,
                                                                                        place_1,
                                                                                        cemetery_list,
                                                                                        cards_in_board,
                                                                                        cards_for_game,
                                                                                        player_1.hand)
            wrong_answers_p1 += 1
            show_cards_for_player(player_1.hand)
        else:
            correct_answer()
            correct_answers_p1 += 1
            show_cards_for_player(player_1.hand)
    input("PRESS ENTER TO CONTINUE")
    # clear_console()
    # Turn of player 2
    print()
    print_colored_text("CARDS ON BOARD", 'yellow')
    # Show the existent cards on the board
    show_cards(cards_in_board)
    print()
    print(f"NOW IT'S YOUR TURN {player_2.name}")
    print("THESE ARE YOUR CARDS")
    show_cards_for_player(player_2.hand)
    print("(GIVE ME THE NUMBER THAT IT'S AT THE BEGINNING OF YOUR CHOICE)")
    choose_2 = choose_of_player()
    print(f"PERFECT, YOU WANT TO USE: {player_2.hand[choose_2].fact}")
    print()
    print("WE WILL TELL YOU HOW YOU SHOULD THROW, FOR EXAMPLE: ")
    print("IN CASE THAT THERE IS ONLY ONE CARD ON THE BOARD")
    print("USE 0 TO PUT BEFORE AND 1 TO PUT AFTER")
    print("IN CASE THAT THERE ARE MORE THAN ONE CARD ON THE BOARD")
    print("USE 0 TO PUT AT THE BEGINNING AND THE NUMBER AT THE BEGINNING\n"
          "OF THE LAST CARD TO PUT AT THE END OF THE CARDS")
    print("BUT IF YOU WANT TO PUT IT BETWEEN CARDS, ")
    print("THEN USE THE NUMBER OF THE CARD BEFORE THE PLACE YOU WANT TO PUT IT")
    print("FOR EXAMPLE:")
    print("CARD1, CARD2, CARD3, CARD4")
    print("IF YOU WANT TO PUT BETWEEN CARD3 AND CARD4 YOU SHOULD USE 3")
    place_2 = place_card(player_2.name)
    print()
    if place_2 == 0:
        cards_in_board.insert(0, player_2.hand[choose_2])
        player_2.hand.remove(player_2.hand[choose_2])
        print_colored_text("CARDS ON BOARD", 'yellow')
        show_cards(cards_in_board)
        print()
        cards_for_game = validate_cards_for_game(cards_for_game, cemetery_list)
        if cards_in_board[1].date < cards_in_board[0].date:
            cemetery_list, cards_in_board, cards_for_game, player_2.hand = wrong_answer_0(gender2,
                                                                                          cemetery_list,
                                                                                          cards_in_board,
                                                                                          cards_for_game,
                                                                                          player_2.hand)
            wrong_answers_p2 += 1
            show_cards_for_player(player_2.hand)
        else:
            correct_answer()
            correct_answers_p2 += 1
            show_cards_for_player(player_2.hand)
    elif place_2 > 0:
        cards_in_board.insert(place_2, player_2.hand[choose_2])

        player_2.hand.remove(player_2.hand[choose_2])
        print_colored_text("CARDS ON BOARD", 'yellow')
        show_cards(cards_in_board)
        print()
        cards_for_game = validate_cards_for_game(cards_for_game, cemetery_list)
        if cards_in_board[place_2].date < cards_in_board[place_2 - 1].date:
            cemetery_list, cards_in_board, cards_for_game, player_2.hand = wrong_answer(gender2,
                                                                                        place_2,
                                                                                        cemetery_list,
                                                                                        cards_in_board,
                                                                                        cards_for_game,
                                                                                        player_2.hand)
            wrong_answers_p2 += 1
            show_cards_for_player(player_2.hand)
        else:
            correct_answer()
            correct_answers_p2 += 1
            show_cards_for_player(player_2.hand)
    rounds += 1
    input("PRESS ENTER TO CONTINUE")
    # clear_console()

print()
print(f"TOTAL OF ROUNDS {rounds}")
print(f"TOTAL OF CORRECT ANSWERS OF {player_1.name}: {correct_answers_p1}")
print(f"TOTAL OF WRONG ANSWERS OF {player_1.name}: {wrong_answers_p1}")
print(f"TOTAL OF CORRECT ANSWERS OF {player_2.name}: {correct_answers_p2}")
print(f"TOTAL OF WRONG ANSWERS OF {player_2.name}: {wrong_answers_p2}")
if correct_answers_p1 > correct_answers_p2 or wrong_answers_p1 < wrong_answers_p2:
    print(f"THE WINNER IS {player_1.name}")
else:
    print(f"THE WINNER IS {player_2.name}")
