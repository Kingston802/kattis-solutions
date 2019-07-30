#include <iostream>
using namespace std;
int main() {
  float coords[5];
  while(true) {
    for(int i=0; i<=4; i++) {
      float temp;
      cin >> temp;

      coords[i] = temp;
      if(temp == 0) {
        break;
      }
    }
  }
}
