#include <iostream>
#include <fstream>

int main ()
{
  int a, b;
  std::ifstream read("input.txt");
  read >> a >> b;
  read.close();
  std::ofstream write("output.txt");
  write << a + b;
  write.close();
  return 0;
}