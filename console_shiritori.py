from jisho_api.word import Word
import sys, os

class jishoRequest():
    def __init__(self):
        self.output = sys.stdout
    def __enter__(self):
        sys.stdout = open(os.devnull, "w")
    def __exit__(self, *args):
        sys.stdout = self.output

def shiritori(new_word: str):
    old_word = "はなみ"
    if new_word[0] == old_word[2]:
        print("YES")

def main():
    msg = input("Type: ")
    request = "\"" + msg + "\""

    # if re.fullmatch("[a-z0-9]", msg): figure out how to stop bad inputs later
    #     print("Bruh")

    with jishoRequest():
        word_call = Word.request(request)

    shiritori(msg)

    try:
        valid = word_call.meta.status
    except:
        print("Yep")

if __name__ == "__main__":
    main()