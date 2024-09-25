#include <atomic>
#include <iostream>
#include <string>

using namespace std;

const string alfabet_m="aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż";
const string alfabet_w="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ";

char Cezar_PL(char znak, int klucz)
{
    int i=alfabet_m.find(znak);
    if (i >= 0 && i < 35) {
        i = (i + klucz) % 35;
        return alfabet_m[i];
    }
    i = alfabet_w.find(znak);
    if (i >= 0 && i < 35) {
        i = (i + klucz) % 35;
        return alfabet_w[i];
    }
    return znak;
}

string Cezar(string s, int klucz)
{
    string szyfrogram;
    for (int i = 0; i < s.length(); i++)
    {
        szyfrogram += Cezar_PL(s[i], klucz);
    }
    return szyfrogram;
}
int main()
{
    cout << Cezar("test", 3);
    return 0;
}
