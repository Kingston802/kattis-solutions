#include <iostream>
#include <string>
using namespace std;
int main() { 
  string input; 
  cin >> input;

  char lastCharacter; 
  int index = 0;
  for(auto c: input) {
    if(c==lastCharacter) {
      input.erase(index,1);
      continue;
    }
    lastCharacter = c;
    index++;
  }
  
  cout << input << endl;
}


