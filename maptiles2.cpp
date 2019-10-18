#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    int zoom, x, y;
    string input;
    cin >> input;
    
    zoom = input.length() + 1;

    vector<vector<string>> mapVec(zoom);

    for (int i=0; i<zoom; i++) 
        for (int j=0; j<zoom; j++) 
            mapVec[i].push_back(:);

    for (auto val: mapVec) { 
        for (auto val2: val) {
            cout << val2 << ' ';
        }
        cout << endl;
    }

    // cout << zoom << ' ' << x << ' ' << y << ' ' << endl;
}

