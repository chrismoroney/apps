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
        while True:
                try:
                        wager = int(wager)
                        break
                except ValueError:
                        print("Please input an integer.")
                        wager = input("Enter amount you want to wager: ")
        if wager > money:
                print("Please input an integer that is less than your total money.")
        elif wager <= 0:
                print("Please input a value greater than 0.")
        else:
                return wager

def win():
        money += wager

def lose(money, wager):
        money -= wager
        return money

def score_hand(cards):
        score = 0
        for card in cards:
                if card[1] == 'A':
                        score += 1
                if card[1] == '2':
                        score += 2
                if card[1] == '3':
                        score += 3
                if card[1] == '4':
                        score += 4
                if card[1] == '5':
                        score += 5
                if card[1] == '6':
                        score += 6
                if card[1] == '7':
                        score += 7
                if card[1] == '8':
                        score += 8
                if card[1] == '9':
                        score += 9
                if card[1] == '1' or card[1] =='J' or card[1] =='Q' or card[1] =='K':
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

while True:
        wager = wager_func()
        play_game()
        money = lose(money, wager)
        print(money)
