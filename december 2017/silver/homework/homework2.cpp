/*
ID: warwick2
LANG: C++11
TASK: homework
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
#include <cmath>
using namespace std;

#define MAX_N 100000

int n, grades[MAX_N];


int main(void){
	ifstream fin("homework.in");
    ofstream fout("homework.out");

    fin >> n;
    for (int i=0; i<n; i++){
        fin >> grades[i];
    }

    float highest_avg = 0;
    list<int> ks;

    int total = grades[n-1];
    int num = 1;
    int min = grades[n-1];

    for (int i=n-2; i>=1; i--){
        total += grades[i];
        num++;

        if (grades[i] < min){
            min = grades[i];
        }

        float avg = ((float)(total-min))/(num-1);

        cout << "avg" << avg << "\n";

        if (avg == highest_avg){
            ks.emplace_front(i);
        }
        if (avg > highest_avg){
            highest_avg = avg;
            ks.clear();
            ks.emplace_front(i);
        }
    }

    for (auto z: ks){
        // cout << z << "\n";
        fout << z << "\n";
    }

    return 0;
}