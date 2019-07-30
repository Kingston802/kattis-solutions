#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main() {
    int tcount=0, ccount=0, gcount=0;
    string input;
    cin >> input;

    for(char c: input) {
        switch(c) {
            case 'C':ccount++; break;
            case 'T':tcount++; break;
            case 'G':gcount++; break;
        }
    }

    int points = pow(ccount, 2.0) + pow(tcount, 2.0) + pow(gcount, 2.0);

    int sevencount = 0;
    while(true) {
        if(ccount>0 && tcount>0 && gcount>0) {
            ccount--; tcount--; gcount--;
            sevencount++;
        } else {
            break;
        }
    }

    points += 7 * sevencount;
    cout << points << endl;
}

