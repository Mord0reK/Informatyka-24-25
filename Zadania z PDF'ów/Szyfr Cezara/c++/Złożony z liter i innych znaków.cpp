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
        if (toupper(jawny[i]) >= 'A' && toupper(jawny[i]) <= 'Z')
        {
            kod = jawny[i] + klucz;
            if ((jawny[i] <= 'Z' && kod > 'Z') || (jawny[i] >= 'a' && kod > 'z')) kod = kod - 26;
            szyfrogram += char(kod);
        }
        else szyfrogram = szyfrogram + jawny[i];
    }
    cout << "Szyfrogram: " << szyfrogram << endl;
    return 0;
}
