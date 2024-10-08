#ryzunki mozna robic po prostu printami nie koniecznie takimi skomplikowanymi
#wierze ze sobie poradzisz
#czas na sieste

def rysuj_a():
    # a) Wzór:
    #       * 
    #      * * 
    #     * * * 
    #    * * * * 
    #   * * * * * 
    #    * * * * 
    #     * * * 
    #      * 
    n = 5  # liczba wierszy (górna część)
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '* ' * i)


# Wywołanie wszystkich funkcji
rysuj_a()

