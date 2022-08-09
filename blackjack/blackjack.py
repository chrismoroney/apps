import random

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

while True:
        hand_size = 2
        play_continue = True

        while hand_size < 5 and play_continue:
                command = input("hit or stay: ")
                if command == "hit":
                        card = random.choice(deck)
                        cards.append(card)
                        deck.remove(card)
                        print(cards)
                        hand_size = len(cards)
                elif command == "stay":
                        play_continue = False
        quit()