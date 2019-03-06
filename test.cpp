#include <iostream>
using namespace std;

int main()
{

int a;
int *P;
P = &a;
a=5;

cout << a << endl;
cout << P << endl;
cout << &a << endl;
cout << &P << endl;
//cout << *a <<endl;
cout << *P << endl;
return 0;
}
