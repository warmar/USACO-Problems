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
#include <vector>
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
entry entries[MAX_N];
int gallons[10000];
vector<int> best_cows;

vector<int> find_best_cows(){
    vector<int> best;
    int max = 0;
    for (int i=0; i<n; i++){
        if (gallons[i] > max){
            best.clear();
            best.emplace_back(i);
        }
        if (gallons[i] == max){
            best.emplace_back(i);
        }
    }

    for (auto a : best){
        cout << "best" << a << "\n";
        cout << "\n";
    }

    return best;
}

int main(void){
	ifstream fin("measurement.in");
    ofstream fout("measurement.out");

    fin >> n >> g;
    for (int i=0; i<n; i++){
        int day, cow, change;
        fin >> day >> cow >> change;
        entries[i] = {day, cow, change};
    }

    sort(entries, entries+n, sort_entries);

    int next_entry = 0;
    int changes = 0;
    int first_day = entries[0].day;
    int last_day = entries[n-1].day;    

    best_cows = find_best_cows();

    for (int day=first_day; day<=last_day; day++){
        while (entries[next_entry].day == day){
            gallons[entries[next_entry].cow] += entries[next_entry].change;
            next_entry++;
        }
        vector<int> new_best_cows = find_best_cows();
        if (!equal(best_cows.begin(), best_cows.begin()+n, new_best_cows.begin())){
            changes++;
            best_cows = new_best_cows;
        }
    }

    fout << changes << "\n";
    return 0;
}