import random

money = 100
wager = 0

deck = ["|A%|", "|A<3|", "|A@|", "|A^|",
        "|2%|", "|2<3|", "|2@|", "|2^|",
        "|3%|", "|3<3|", "|3@|", "|3^|",
        "|4%|", "|4<3|", "|4@|", "|4^|",
        "|5%|", "|5<3|", "|5@|", "|5^|",
        "|6%|", "|6<3|", "|6@|", "|6^|",
        "|7%|", "|7<3|", "|7@|", "|7^|",
        "|8%|", "|8<3|", "|8@|", "|8^|",
        "|9%|", "|9<3|", "|9@|", "|9^|",
        "|10%|", "|10<3|", "|10@|", "|10^|",
        "|J%|", "|J<3|", "|J@|", "|J^|",
        "|Q%|", "|Q<3|", "|Q@|", "|Q^|",
        "|K%|", "|K<3|", "|K@|", "|K^|"]


cards = random.sample(deck, 2)
for card in cards:
        deck.remove(card)
print(cards)

def wager_func():
        print("Total money: $", money)
        wager = input("Enter amount you want to wager: ")
        if not isinstance(wager, int):
                print("Please input an integer.")
                wager_func()
        elif wager > money:
                print("Please input an integer that is less than your total money.")
                wager_func()
        elif wager <= 0:
                print("Please input a value greater than 0.")

def win():
        money += wager

def lose():
        money -= wager

def score_hand(cards):
        score = 0
        for card in cards:
                match card[1]:
                        case 'A':
                                score += 1
                        case '2':
                                score += 2
                        case '3':
                                score += 3
                        case '4':
                                score += 4
                        case '5':
                                score += 5
                        case '6':
                                score += 6
                        case '7':
                                score += 7
                        case '8':
                                score += 8
                        case '9':
                                score += 9
                        case '1' | 'J' | 'Q' | 'K':
                                score += 10
        return score


def play_game():
        hand_size = 2
        play_continue = True

        while hand_size < 5 and play_continue:
                score = score_hand(cards)
                print("Score: ", score)
                command = input("hit or stay: ")
                if command == "hit":
                        card = random.choice(deck)
                        cards.append(card)
                        deck.remove(card)

                        print(cards)
                        hand_size = len(cards)

                elif command == "stay":
                        play_continue = False
        
        score = score_hand(cards)
        print("Score: ", score)
        quit()

while True:
        #wager_func()
        play_game()

