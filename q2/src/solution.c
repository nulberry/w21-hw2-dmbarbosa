#include <stdio.h>
#include <solution.h>

int main() {
  int* x = malloc(10 * sizeof(int));
  x[10] = 0;
  
  printf("0.0\n");
  return(0);
}
