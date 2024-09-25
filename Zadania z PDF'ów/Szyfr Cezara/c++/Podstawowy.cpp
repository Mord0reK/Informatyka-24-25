#include <iostream>
#include <string>

using namespace std;

int main() {
    string jawny, szyfrogram = "";
    int klucz, i;
    int kod;
    cout << "Podaj tekst do zaszyfrowania: ";
    cin >> jawny;
    cout << "Podaj klucz: ";
    cin >> klucz;
    for (i = 0; i < jawny.size(); i++)
    {
        kod = jawny[i] + klucz;
        if (kod > 'Z') kod = kod - 26;
        szyfrogram += char(kod);
    }
    cout << "Szyfrogram: " << szyfrogram << endl;
    return 0;
}
