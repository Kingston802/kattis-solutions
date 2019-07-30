#include <iostream>
#include <vector>
using namespace std;
int main() {
  // This is a stupid solution, but likely faster than calculating 10! a lot
  int t;
  cin >> t;

  vector<int> values;
  for(int i=0; i<t; i++) {
    int n;
    cin >> n;

    values.push_back(n);
  }

  for(int val: values) {
    switch(val) {
      case 1: cout << 1 << endl; break; 
      case 2: cout << 2 << endl; break; 
      case 3: cout << 6 << endl; break; 
      case 4: cout << 4 << endl; break; 
      case 5: cout << 0 << endl; break; 
      case 6: cout << 0 << endl; break; 
      case 7: cout << 0 << endl; break; 
      case 8: cout << 0 << endl; break; 
      case 9: cout << 0 << endl; break; 
      case 10: cout << 0 << endl; break; 
    }
  }
}
