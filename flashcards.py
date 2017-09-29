# flashcards by Oskar Eriksson

import sys

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
        if not lines[0]:
            lines.pop(0)
            continue
        else:
            card = Card(lines.pop(0), lines.pop(0), lines.pop(0))
            cards.append(card)

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

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        main()
    else:
        print_usage()

