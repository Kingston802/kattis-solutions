#include <iostream>
#include <map>
#include <utility>
#include <vector>
#include <string>
using namespace std;

map<char, int> printerValues;

int main() {
  printerValues.insert(pair<char, int>(' ', 0));
  printerValues.insert(pair<char, int>('&', 24));
  printerValues.insert(pair<char, int>(',', 7));
  printerValues.insert(pair<char, int>('2', 22));
  printerValues.insert(pair<char, int>('8', 23));
  printerValues.insert(pair<char, int>('>', 10));
  printerValues.insert(pair<char, int>('D', 26));
  printerValues.insert(pair<char, int>('J', 18));
  printerValues.insert(pair<char, int>('P', 23));
  printerValues.insert(pair<char, int>('V', 19));
  printerValues.insert(pair<char, int>('\\', 10));
  printerValues.insert(pair<char, int>('b', 25));
  printerValues.insert(pair<char, int>('h', 21));
  printerValues.insert(pair<char, int>('n', 18));
  printerValues.insert(pair<char, int>('t', 17));
  printerValues.insert(pair<char, int>('z', 19));
  printerValues.insert(pair<char, int>('!', 9));
  printerValues.insert(pair<char, int>('\'', 3));
  printerValues.insert(pair<char, int>('-', 7));
  printerValues.insert(pair<char, int>('3', 23));
  printerValues.insert(pair<char, int>('9', 26));
  printerValues.insert(pair<char, int>('?', 15));
  printerValues.insert(pair<char, int>('E', 26));
  printerValues.insert(pair<char, int>('K', 21));
  printerValues.insert(pair<char, int>('Q', 31));
  printerValues.insert(pair<char, int>('W', 26));
  printerValues.insert(pair<char, int>(']', 18));
  printerValues.insert(pair<char, int>('c', 17));
  printerValues.insert(pair<char, int>('i', 15));
  printerValues.insert(pair<char, int>('o', 20));
  printerValues.insert(pair<char, int>('u', 17));
  printerValues.insert(pair<char, int>('{', 18));
  printerValues.insert(pair<char, int>('\"', 6));
  printerValues.insert(pair<char, int>('(', 12));
  printerValues.insert(pair<char, int>('.', 4));
  printerValues.insert(pair<char, int>('4', 21));
  printerValues.insert(pair<char, int>(':', 8));
  printerValues.insert(pair<char, int>('@', 32));
  printerValues.insert(pair<char, int>('F', 20));
  printerValues.insert(pair<char, int>('L', 16));
  printerValues.insert(pair<char, int>('R', 28));
  printerValues.insert(pair<char, int>('X', 18));
  printerValues.insert(pair<char, int>('^', 7));
  printerValues.insert(pair<char, int>('d', 25));
  printerValues.insert(pair<char, int>('j', 20));
  printerValues.insert(pair<char, int>('p', 25));
  printerValues.insert(pair<char, int>('v', 13));
  printerValues.insert(pair<char, int>('|', 12));
  printerValues.insert(pair<char, int>('#', 24));
  printerValues.insert(pair<char, int>(')', 12));
  printerValues.insert(pair<char, int>('/', 10));
  printerValues.insert(pair<char, int>('5', 27));
  printerValues.insert(pair<char, int>(';', 11));
  printerValues.insert(pair<char, int>('A', 24));
  printerValues.insert(pair<char, int>('G', 25));
  printerValues.insert(pair<char, int>('M', 28));
  printerValues.insert(pair<char, int>('S', 25));
  printerValues.insert(pair<char, int>('Y', 14));
  printerValues.insert(pair<char, int>('_', 8));
  printerValues.insert(pair<char, int>('e', 23));
  printerValues.insert(pair<char, int>('k', 21));
  printerValues.insert(pair<char, int>('q', 25));
  printerValues.insert(pair<char, int>('w', 19));
  printerValues.insert(pair<char, int>('}', 18));
  printerValues.insert(pair<char, int>('$', 29));
  printerValues.insert(pair<char, int>('*', 17));
  printerValues.insert(pair<char, int>('0', 22));
  printerValues.insert(pair<char, int>('6', 26));
  printerValues.insert(pair<char, int>('<', 10));
  printerValues.insert(pair<char, int>('B', 29));
  printerValues.insert(pair<char, int>('H', 25));
  printerValues.insert(pair<char, int>('N', 25));
  printerValues.insert(pair<char, int>('T', 16));
  printerValues.insert(pair<char, int>('Z', 22));
  printerValues.insert(pair<char, int>('`', 3));
  printerValues.insert(pair<char, int>('f', 18));
  printerValues.insert(pair<char, int>('l', 16));
  printerValues.insert(pair<char, int>('r', 13));
  printerValues.insert(pair<char, int>('x', 13));
  printerValues.insert(pair<char, int>('~', 9));
  printerValues.insert(pair<char, int>('%', 22));
  printerValues.insert(pair<char, int>('+', 13));
  printerValues.insert(pair<char, int>('1', 19));
  printerValues.insert(pair<char, int>('7', 16));
  printerValues.insert(pair<char, int>('=', 14));
  printerValues.insert(pair<char, int>('C', 20));
  printerValues.insert(pair<char, int>('I', 18));
  printerValues.insert(pair<char, int>('O', 26));
  printerValues.insert(pair<char, int>('U', 23));
  printerValues.insert(pair<char, int>('[', 18));
  printerValues.insert(pair<char, int>('a', 23));
  printerValues.insert(pair<char, int>('g', 30));
  printerValues.insert(pair<char, int>('m', 22));
  printerValues.insert(pair<char, int>('s', 21));
  printerValues.insert(pair<char, int>('y', 24));

  vector<int> totals;

  string line; 
  while(getline(cin, line)) {
    int total = 0;
    for(char c:line) {
      total += printerValues[c];
    }

    totals.push_back(total);
  }

  for(auto total: totals) {
    cout << total << endl;
  }
}
