# flashcards by Oskar Eriksson

import sys
import random


class Card:
    """The Card class represents a flash card"""
    def __init__(self, question, hint, answer):
        self.question = question
        self.hint = hint
        self.answer = answer


def main():
    """Main function of the Flash Cards program"""
    lines = get_lines(sys.argv[1])
    cards = make_cards(lines)
    # Display all flash cards
    while len(cards) > 0:
        print("Remaining questions: " + str(len(cards)))
        card = cards.pop(random.randrange(0, len(cards)))
        print(card.question)
        # First action, get hint or display answer
        action = get_action("Press enter for the answer or type 'h' for a hint... ")
        if (action == 'h'):
            print("\n" + card.hint)
            get_action("Press enter for the answer... ")
            print("\n" + card.answer)
        else:
            print("\n" + card.answer)
        # Second action, successful or not successful
        action = get_action("Press enter if you were successful or type 'n' otherwise... ")
        if (action == 'n'):
            cards.append(card)
        print()
    print("Finished, well done!")

def get_lines(path):
    """Reads file and returns list of lines"""
    try:
        f = open(sys.argv[1], 'r')
    except:
        print_usage()
    else:
        lines = f.read().split('\n')
        f.close()
        return lines

def make_cards(lines):
    """Creates a list of Card objects from the input lines"""
    cards = list()
    while len(lines) >= 3:
        if not lines[0] or lines[0][0] == '#':
            lines.pop(0)
            continue
        else:
            card = Card(lines.pop(0), lines.pop(0), lines.pop(0))
            cards.append(card)
    return cards

def print_usage():
    """Prints usage message and exits"""
    usage_file = "usage.txt"
    try:
        f = open(usage_file, 'r')
    except:
        print("Critical error: File " + usage_file + " not found")
        sys.exit(1)
    else:
        print(f.read(), end='')
        f.close()
        sys.exit(0)

def get_action(prompt):
    """Reads from standard in and converts to lower case"""
    return input(prompt).strip().lower()


if __name__ == "__main__":
    if (len(sys.argv) == 2):
        main()
    else:
        print_usage()

