#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

// 🍒 🍋 🔔 💎 7 🍀

int main() {
    const char *symbols[] = {"🍒", "🍋", "🔔", "💎", "7", "🍀"};
    constexpr int symb_count = std::size(symbols);

    srand(static_cast<unsigned int>(time(nullptr)));

    cout << "🎰 Welcome to the Slot Machine! 🎰" << endl;

    char choice;
    do {
        // 0 ... MAX_INT / 6 = 0,1,2,3,4,5
        const int i1 = rand() % symb_count;
        const int i2 = rand() % symb_count;
        const int i3 = rand() % symb_count;

        cout << "Spinning ..." << endl;
        cout << "| " << symbols[i1] << " | " << symbols[i2] << " | " << symbols[i3] << " |" << endl;

        if (i1 == i2 && i2 == i3)
            cout << "🎉 JACKPOT!" << endl;
        else if (i1 == i2 || i2 == i3 || i3 == i1)
            cout << "✨ Nice, you have two matches symbols!" << endl;
        else
            cout << "🙁 No match :(" << endl;

        cout << "Do you want new spin? (y/n): ";
        cin >> choice;
        cout << endl;
    } while (choice == 'Y' || choice == 'y');

    cout << endl;
    cout << "🎲 Thanks for playing!" << endl;

    return 0;
}
