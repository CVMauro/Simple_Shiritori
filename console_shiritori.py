from fugashi import Tagger

small_characters = {
    "ャ" : "ヤ",
    "ュ" : "ユ",
    "ョ" : "ヨ",
    "ァ" : "ア",
    "ゥ" : "ウ",
    "ォ" : "オ",
    "ェ" : "エ",
    "ィ" : "イ",
}

class Player:
    def __init__(self, name, input):
        self.name = name
        self.input = input

def first_turn(first_turn_result):
    if first_turn_result.pos[:2] != "名詞":
        print("Not a noun! P1 Loses!")
        return True
    elif first_turn_result.feature.kana[-1] == "ン":
        print("Ends in ン! P1 Loses!")
        return True
    else:
        return False
    
def multi_word_turn(current_player, player_result, previous_result, previous_kana):
    first_word = player_result[0]
    last_word = player_result[-1]

    if last_word.pos[:2] != "名詞":
        print(f"Not a noun! {current_player.name} Loses!")
        return False
    elif first_word.feature.kana[0] != previous_kana and previous_kana not in small_characters:
        print(f"Doesn't match previous kana! {current_player.name} Loses!")
        return False
    elif previous_kana in small_characters and small_characters[previous_kana] != first_word.feature.kana[0]:
        print(f"Doesn't match previous kana! {current_player.name} Loses!")
        return False
    elif last_word.feature.kana[-1] == "ン":
        print(f"Ends in ン! {current_player.name} Loses!")
        return False
    else:
        previous_result[0] = player_result[-1]
        return True

def turns(tagger, current_player, previous_result):
    current_player.input = input(f"{current_player.name}:")

    tagger.parse(current_player.input)

    previous_kana = previous_result[0].feature.kana[-1]
    if previous_kana == "ー":
        previous_kana = previous_result[0].feature.kana[-2]

    if len(tagger(current_player.input)) > 1:
        return multi_word_turn(current_player, tagger(current_player.input), previous_result, previous_kana)

    player_result = tagger(current_player.input)[0]

    print(tagger(current_player.input))

    if player_result.pos[:2] != "名詞":
        print(f"Not a noun! {current_player.name} Loses!")
        return False
    elif player_result.feature.kana[0] != previous_kana and previous_kana not in small_characters:
        print(f"Doesn't match previous kana! {current_player.name} Loses!")
        return False
    elif previous_kana in small_characters and small_characters[previous_kana] != player_result.feature.kana[0]:
        print(f"Doesn't match previous kana! {current_player.name} Loses!")
        return False
    elif player_result.feature.kana[-1] == "ン":
        print(f"Ends in ン! {current_player.name} Loses!")
        return False
    else:
        previous_result[0] = player_result
        return True

def game(tagger):
    p1 = Player("P1", "") 
    p2 = Player("P2", "")

    players = [p1, p2]

    first_turn_word = input("Starting Word:")
    tagger.parse(first_turn_word)

    first_turn_result = tagger(first_turn_word)[0]

    if len(tagger(first_turn_word)) > 1:
        first_turn_result = tagger(first_turn_word)[-1]

    print(tagger(first_turn_word))
    print(first_turn_result.feature.kana[-1])
    
    if first_turn(first_turn_result):
        return

    p1.input = first_turn_word
    n = -1

    current_player = players[n]
    previous_result = [first_turn_result]

    while turns(tagger, current_player, previous_result) is True:
        print(previous_result[0].feature.kana[-1])
        if n == -1:
            n += 1
        else:
            n -= 1
        current_player = players[n]

def main():
    tagger = Tagger('-Owakati')

    print("\u001b[2J\x1b[H\x1b[4mようこそ、\x1b[38;5;121mしりとりへ\x1b[0m")
    game(tagger)

if __name__ == "__main__":
    main()