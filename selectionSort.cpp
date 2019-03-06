#include <iostream>
#include <vector>
using namespace std;

void print(vector<int> A, int n)
{
    for( int i = 0; i < n; i ++)
     {
       cout << A[i] << " ";
     }
cout << endl;
}

void SelectionSortExtraSpace(vector<int> &A, int n)
{
vector<int> myArray;  
     

for (int i = 0; i < n; i++)
    {
        int lowest = 9999;
        int index = 9999;
        for (int j = 0; j < n; j++)
        {
             if (A[j]<lowest)
             {
                lowest = A[j];
                index = j;
             }        
        }
     myArray.push_back(lowest);
     A[index] = 9999;
             
    }
A = myArray; 
}

void SelectionSortInPlace(vector<int> &A, int n)
{
    
for (int i = 0; i < n; i++)
    {
        int lowest = 9999;
        int index = 9999;
        for (int j = 0; j < n; j++)
        {
             if (A[j]<lowest)
             {
                lowest = A[j];
                index = j;
             }
        }
     int temp = A[i];
     A[i]=A[index];
     A[index]=temp;

    }
}

int main()
{
vector<int> myArray {8, 6, 4, 3, 1, 2, 9, 5,7,0};
print(myArray, myArray.size());
cout <<"Sort with extra space" << endl;
SelectionSortExtraSpace(myArray,myArray.size());
print(myArray, myArray.size());
cout<< " ---------------------" << endl;
vector<int> myArray2 {8, 6, 4, 3, 1, 2, 9, 5,7,0};
print(myArray2, myArray2.size());
cout <<"Sort in place" << endl;
SelectionSortInPlace(myArray,myArray.size());
print(myArray2, myArray2.size());


}
