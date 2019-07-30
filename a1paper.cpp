#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

float calculateLength(int paperSize) {
    return 0;
}

int main() {
    vector<int> v;
    int n;
    cin >> n;
    
    int temp;
    for(int i=0; i<n-1; i++) {
        cin >> temp;

        v.push_back(temp);
    }

    int totalLengthOfTape = 0;

    vector<int> required(v.size(), 0);
    required[0] = ;
    for(int i=1; i<v.size(); i++) {
        required[i] = 2*required[i-1] - required[i];
    }

//    for(auto val:v) {
//        cout << val << endl;
//    }
}
