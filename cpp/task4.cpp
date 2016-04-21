#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

std::vector<std::string> split(std::string str, char delimiter) {
  std::vector<std::string> internal;
  stringstream ss(str);
  string tok;

  while(getline(ss, tok, delimiter)) {
    internal.push_back(tok);
  }

  return internal;
}


int main(int argc, char *argv[])
{

    int N;
    std::string input, input2;
    std::vector<int> scores;

    std::getline(std::cin, input2);
    std::getline(std::cin, input);

    std::vector<string> splitedString = split(input2, ' ');
    N = atoi(splitedString[0].c_str());

    splitedString = split(input, ' ');
    int result = 0;

    for (int i = 0; i < N; i++) {
        scores.push_back(atoi(splitedString[i].c_str()));
    }

    for (int i = 1; i < N + 1; i++) {
        std::vector<int> scores_tmp;
        for (int j = 0; j < i; j++) {
            scores_tmp.push_back(scores[j]);
        }
        std::sort(scores_tmp.begin(), scores_tmp.end(), std::greater<int>());
        result += scores_tmp[i/2];
    }

    std::cout << result << endl;

    return 0;
}
