#include <iostream>
using namespace std;
int main() {
  double c, l;
  cin >> c >> l;

  double total = 0;
  for(int i=0; i<l; i++) {
    double x, y;
    cin >> x >> y;

    total += x * y * c;
  }

  cout << total << endl;
}
