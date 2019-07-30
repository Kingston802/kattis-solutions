#include <iostream>
using namespace std;
int main() {
  int n;
  cin >> n;

  float total = 0.0;
  for(int i=0; i<n; i++) {
    float a, b;
    cin >> a >> b;

    total += a * b;
  }

  cout << total << endl;
}

    
