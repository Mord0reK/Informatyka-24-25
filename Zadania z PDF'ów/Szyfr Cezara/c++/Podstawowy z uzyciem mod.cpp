#include <iostream>
#include <string>

using namespace std;

int main() {
    string jawny, szyfrogram = "";
    int klucz;
    cout << "Podaj tekst do zaszyfrowania: ";
    cin >> jawny;
    cout << "Podaj klucz: ";
    cin >> klucz;
    for (int i = 0; i < jawny.length(); i++) {
        if (jawny[i] >= 'A' && jawny[i] <= 'Z') {
            szyfrogram += (jawny[i] - 'A' + klucz) % 26 + 'A';
        } else if (jawny[i] >= 'a' && jawny[i] <= 'z') {
            szyfrogram += (jawny[i] - 'a' + klucz) % 26 + 'a';
        }
    }
    cout << "Szyfrogram: " << szyfrogram << endl;
    return 0;
}
