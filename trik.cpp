#include <iostream>
#include <string>
using namespace std;

bool cups[3] = {1, 0, 0};

void swap(int a, int b) {
    bool temp = cups[b];
    cups[b] = cups[a];
    cups[a] = temp;
}

int main() {
    string input;
    cin >> input;

    for(auto c: input) {
        switch(c) {
            case 'A': swap(0, 1); break;
            case 'B': swap(1, 2); break;
            case 'C': swap(0, 2); break;
        }
    }

    for(int i=0; i<3; i++) {
        if(cups[i]) {
            cout << i+1 << endl;
        }
    }
}
