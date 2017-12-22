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

struct entry{
    int day;
    int cow;
    int change;
};

bool sort_entries(entry a, entry b){
    return b.day > a.day;
}

int n, g;
int changes[MAX_N][10000]; // [day #][cow #]
int gallons[MAX_N][10000];

list<int> find_best_cows(int day){
    int max = 0;
    list<int> best;

    for (int i=0; i<10000; i++){
        if (gallons[day][i] > max){
            max = gallons[day][i];
            best.clear();
            best.emplace_back(i);
            continue;
        }

        if (gallons[day][i] == max){
            best.emplace_back(i);
        }
    }

    return best;
}

int main(void){
	ifstream fin("base.in");
    ofstream fout("base.out");

    fin >> n >> g;
    for (int i=0; i<n; i++){
        int day, cow, change;
        fin >> day >> cow >> change;
        changes[day][cow] = change;
    }

    // list<int> prev_best_cows = find_best_cows(0);

    for (auto k : find_best_cows(0)){
        cout << k << "\n";
    }

    // for (int day=1; day<MAX_N; day++){
    //     for (int cow=0; cow<10000; cow++){
    //         gallons[day][cow] = gallons[day-1][cow] + changes[day][cow];
    //     }
    // }

    fout << 0 << "\n";
    return 0;
}