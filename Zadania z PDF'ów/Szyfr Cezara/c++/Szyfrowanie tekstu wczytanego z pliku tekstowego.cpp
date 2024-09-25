#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string Cezar(string s, int klucz)
{
    string szyfrogram = "";
    int kod;
    int i;
    for (i = 0; i < s.size(); i++)
    {
        if (toupper(s[i]) >= 'A' && toupper(s[i]) <= 'Z')
        {
            kod = s[i] + klucz;
            if ((s[i] <= 'Z' && kod > 'Z') || (s[i] >= 'a' && kod > 'z')) kod = kod - 26;
            szyfrogram += char(kod);
        }
        else szyfrogram = szyfrogram + s[i];
    }
    return szyfrogram;
}
int main()
{
    ifstream wejscie("dane.txt");
    ofstream wyjscie("wynik.txt");
    string s;
    int klucz;
    cout << "Podaj klucz: ";
    cin >> klucz;
    while (!wejscie.eof())
    {
        getline(wejscie, s);
        wyjscie << Cezar(s, klucz) << endl;
    }
    wejscie.close();
    wyjscie.close();
    cout << "Plik zostal utworzony.";
    return 0;
}
