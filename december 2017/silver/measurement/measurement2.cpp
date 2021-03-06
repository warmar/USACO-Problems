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
#include <map>
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
set<int> all_cows;
map<int,int> gallons;
vector<int> best_cows;
int prev_max;

vector<int> find_best_cows(){
    vector<int> best;
    bool first = true;
    int max;
    for (auto i : all_cows){
        if (first){
            first = false;
            max = gallons[i];
        }
        if (gallons[i] > max){
            max = gallons[i];
            best.clear();
            best.emplace_back(i);
            continue;
        }
        if (gallons[i] == max){
            best.emplace_back(i);
        }
    }

    prev_max = max;

    return best;
}

int main(void){
	ifstream fin("measurement.in");
    ofstream fout("measurement.out");

    fin >> n >> g;
    for (int i=0; i<n; i++){
        int day, cow, change;
        fin >> day >> cow >> change;
        all_cows.insert(cow);
        entries[i] = {day, cow, change};
    }

    sort(entries, entries+n, sort_entries);

    int next_entry = 0;
    int changes = 0;
    int first_day = entries[0].day;
    int last_day = entries[n-1].day;    

    best_cows = find_best_cows();

    for (int day=first_day; day<=last_day; day++){
        bool changed = false;
        while (entries[next_entry].day == day){
            int cow_num = entries[next_entry].cow;
            gallons[cow_num] += entries[next_entry].change;
            next_entry++;

            changed = true;
            // if (find(best_cows.begin(), best_cows.end(), cow_num) != best_cows.end()){
            //     changed = true;
            // }
            // if (gallons[cow_num] > prev_max){
            //     changed = true;
            // }
        }
        
        if (!changed){
            continue;
        }

        vector<int> new_best_cows = find_best_cows();
        if (best_cows.size() != new_best_cows.size()){
            changes++;
            best_cows = new_best_cows;
            continue;
        }
        for (int i=0; i<best_cows.size(); i++){
            if (best_cows.at(i) != new_best_cows.at(i)){
                changes++;
                best_cows = new_best_cows;
                break;
            }
        }
    }

    fout << changes << "\n";
    return 0;
}