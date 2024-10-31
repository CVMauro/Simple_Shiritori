from jisho_api.word import Word
import sys, os, re

class Player():
    def __init__(self, name: str):
        self.name = name
        self.health = 3
        self.current_word = ""

    # def currentWord(self, word: str):
    #     self.current_word = word

class JishoRequest():
    def __init__(self):
        self.output = sys.stdout
    def __enter__(self):
        sys.stdout = open(os.devnull, "w")
    def __exit__(self, *args):
        sys.stdout = self.output

# def order():
#     first_name = input("Enter player name: ")
#     second_name = input("Enter second player name: ")

#     print("Rock-Paper-Scissors for starting order!")

#     while True:
#         first_selection = input(first_name + ", Enter your selection facing away from P2 (R, P, or S): ")
#         second_selection = input(second_name + ", enter your selection (R, P, or S): ")

#         if first_selection == "R" and second_selection == "S":

def shiritori(player: Player):
    player1_input = input(f"{player.name}: ")

    while not confirm(player1_input):
        player1_input = input(f"{player.name}: ")

    player.current_word = player1_input
    
    # print("Current Word: " + player1_input)

    # player2_input = input("Player 2: ")

    # while not confirm(player2_input):
    #     player2_input = input("Player 2: ")


    # survived = clash(player1_input, player2_input)

    

def confirm(p1_word: str) -> bool:
    regex = re.compile("[^あ-んア-ンーぁ-ゎァ-ン]")

    if regex.search(p1_word):
        print("Invalid character in word!")
        return False
    
    request = "\"" + p1_word + "\""
    try:
        with JishoRequest():
            word_call = Word.request(request)
        valid = word_call.meta.status

        word_data = word_call.data
        for configs in word_data[0]:
            if configs.parts_of_speech[0] == "Noun":
                break
            else:
                print("Not a noun!")
                return False
    except:
        print("Word does not exist!")
        return False
    return True

def clash(old_word: str, new_word: str) -> bool:
    if new_word[0] == old_word[-1] and not (new_word[-1] == "ん" or new_word[-1] == "ン"):
        return True
    else:
        return False

def main():
    p1 = Player("P1")
    p2 = Player("P2")

    words_used = set()

    shiritori(p1)

    while p1.current_word[-1] == "ん" or p1.current_word[-1] == "ン":
        print("Last character cannot be ん")
        shiritori(p1)
    
    words_used.add(p1.current_word)

    shiritori(p2)

    while p2.current_word in words_used:
        print("Duplicate word!")
        shiritori(p2)

    if not clash(p1.current_word, p2.current_word):
        print(f"{p2.name} lost!")
        return

    words_used.add(p2.current_word)
    while True:
        shiritori(p1)

        while p1.current_word in words_used:
            print("Duplicate word!")
            shiritori(p1)

        if not clash(p2.current_word, p1.current_word):
            print(f"{p1.name} lost!")
            break

        words_used.add(p1.current_word)

        shiritori(p2)

        while p1.current_word in words_used:
            print("Duplicate word!")
            shiritori(p1)

        if not clash(p1.current_word, p2.current_word):
            print(f"{p2.name} lost!")
            break

        words_used.add(p2.current_word)
    # msg = input("Type: ")
    # r = Word.request("\"" + msg + "\"")
    # print(r)

    # word_data = r.data
    

    # for configs in word_data[0]:
    #     if configs.parts_of_speech[0] == "Noun":
    #         print("YES")
        #print(configs)
    # iter = word_data.__iter__

    # for iter in word_data:
    #     print(*iter)
    #     iter += 1

    # msg = input("Type: ")
    # request = "\"" + msg + "\""
    # regex = re.compile("[^あ-んア-ンーぁ-ゎァ-ン]")

    # if regex.search(msg):
    #      print("Bruh")

    # try:
    #     with jishoRequest():
    #         word_call = Word.request(request)

    #     clash(msg)
    #     valid = word_call.meta.status
    # except:
    #     print("Yep")

if __name__ == "__main__":
    main()