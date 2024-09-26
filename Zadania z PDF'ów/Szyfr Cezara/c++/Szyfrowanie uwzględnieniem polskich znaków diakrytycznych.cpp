#include <iostream>
#include <string>

using namespace std;

const string alfabet_m = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż";
const string alfabet_w = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ";

string Cezar_PL(string s, int klucz)
{
    string szyfrogram = "";
    char litera;
    int nowy_indeks;

    for (int i = 0; i < s.length(); i++)
    {
        litera = s[i];

        if (alfabet_m.find(litera) != string::npos)
        {
            nowy_indeks = (alfabet_m.find(litera) + klucz) % alfabet_m.length();
            szyfrogram += alfabet_m[nowy_indeks];
        }
        else if (alfabet_w.find(litera) != string::npos)
        {
            nowy_indeks = (alfabet_w.find(litera) + klucz) % alfabet_w.length();
            szyfrogram += alfabet_w[nowy_indeks];
        }
        else
        {
            szyfrogram += litera;
        }
    }

    return szyfrogram;
}

int main()
{
    cout << Cezar_PL("test", 3) << endl;
    return 0;
}
