#include <iostream>
#include <vector>
#include <utility>
using namespace std;
int main() {
    vector<pair<int, int> > fractions;
    int a, b;
    while(true) {
        cin >> a >> b;

        if(a == 0 && b == 0) {
            break;
        }
        fractions.push_back(pair<int, int>(a, b));
    }

    for(auto fraction: fractions) {
        int value = fraction.first / fraction.second;
        int remainder = fraction.first % fraction.second;

        cout << value << " " << remainder << " / " << fraction.second << endl;
    }
}
