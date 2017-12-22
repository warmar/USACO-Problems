/*
ID: warwick2
LANG: C++11
TASK: base
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
#include <cmath>
using namespace std;

#define MAX_N 100000

int n, as[MAX_N];
bool filled[MAX_N]; // filled[position]
bool curr[MAX_N];

int main(void){
	ifstream fin("shuffle.in");
    ofstream fout("shuffle.out");

    fin >> n;
    for (int i=0; i<n; i++){
        fin >> as[i];
        as[i] = as[i]-1;
    }

    fill_n(filled, n, true);

    bool changed = true;
    while (changed){
        for (int pos=0; pos<n; pos++){
            if (filled[pos]){
                curr[as[pos]] = true;
            }
        }

        changed = false;
        for (int pos=0; pos<n; pos++){
            if (curr[pos] != filled[pos]){
                filled[pos] = false;
                changed = true;
            }
        }
        fill_n(curr, n, false);
    }

    for (int step=0; step<n; step++){
        if (step==0){
            for (int pos=0; pos<n; pos++){
                filled[as[pos]] = true;
            }
            continue;
        }
        for (int pos=0; pos<n; pos++){
            // cout << filled[pos] << "\n";
            filled[as[pos]] = filled[pos] || filled[as[pos]];
        }
    }

    int num_filled = 0;
    for (int i=0; i<n; i++){
        if (filled[i]) {
            num_filled++;
        }
    }

    fout << num_filled << "\n";
    return 0;
}