#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    vector<int> v;
    cin >> n;

    for(int i=0; i<n; i++) {
        int temp; 
        cin >> temp;

        v.push_back(temp);
    }

    int minIdx = 0;
    for(int i=0; i<v.size(); i++) {
        if(v[i] < v[minIdx]) {
            minIdx = i;
        }
    }

    cout << minIdx << endl;
}
