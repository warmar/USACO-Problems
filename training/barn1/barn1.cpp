/*
ID: warwick2
LANG: C++11
TASK: barn1
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
using namespace std;

#define MAX 200

int max_boards, num_stalls, num_cows;
int positions[MAX];
int gaps[MAX];
int num_gaps;

bool reverse_sort(int i, int j){
    return i > j;
}

int main(void){
	ifstream fin("barn1.in");
    ofstream fout("barn1.out");

    fin >> max_boards >> num_stalls >> num_cows;
    
    for (int i=0; i<num_cows; i++){
        fin >> positions[i];
    }

    sort(positions, positions+num_cows);

    int prev = positions[0];
    int curr = positions[0];
    for (int i=0; i<num_cows; i++){
        prev = curr;
        curr = positions[i];
        int gap = curr-prev;
        if (gap > 1){
            gaps[num_gaps] = gap;
            num_gaps++;
        }
    }

    sort(gaps, gaps+num_gaps, reverse_sort);
    // print gaps
    for (int i=0; i<num_gaps; i++){
        cout << gaps[i] << "\n";
    }

    int total_length = positions[num_cows-1]-positions[0]+1;
    int num_covered = total_length;

    for (int i=0; i<max_boards-1; i++){
        num_covered -= gaps[i]-1;

        if (num_covered <= num_cows){ // Excess boards != fewer covered than the number of cows
            num_covered = num_cows;
            break;
        }
    }
    
    cout << num_covered << "\n";
    fout << num_covered << "\n";
    return 0;
}