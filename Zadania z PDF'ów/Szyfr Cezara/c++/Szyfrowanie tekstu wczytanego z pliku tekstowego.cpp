#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string Cezar(string s, int klucz)
{
    string szyfrogram = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            szyfrogram += (s[i] - 'A' + klucz) % 26 + 'A';
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            szyfrogram += (s[i] - 'a' + klucz) % 26 + 'a';
        }
    }
    return szyfrogram;
}
int main()
{
    ifstream wejscie("C:/dane.txt");
    ofstream wyjscie("C:/wynik.txt");
    string s;
    int klucz;

    cout << "Podaj klucz: ";
    cin >> klucz;

    while (getline(wejscie, s))
    {
        wyjscie << Cezar(s, klucz) << endl;
    }

    wejscie.close();
    wyjscie.close();

    cout << "Plik zostal utworzony.";
    return 0;
}



