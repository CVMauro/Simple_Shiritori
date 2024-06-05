#include <iostream>
#include <string>
#include <io.h>
#include <fcntl.h>
using namespace std;

bool validWord(wstring previousWord, wstring nextWord);

int main() {
    //Setting console to print unicode characters from https://stackoverflow.com/questions/2492077/output-unicode-strings-in-windows-console
    _setmode(_fileno(stdout), _O_U16TEXT);

    wstring previousWord = L"おめでとう";
    wstring nextWord = L"うち";
    
    validWord(previousWord, nextWord);
    

    return 0;
}

bool validWord(wstring previousWord, wstring nextWord)
{
    if(previousWord[previousWord.length()-1] == nextWord[0]) {
        wcout << "Next word starts with: " << nextWord[0] << endl;
        return true;
    }
    wcout << "You lose!" << endl;
    return false;
}
