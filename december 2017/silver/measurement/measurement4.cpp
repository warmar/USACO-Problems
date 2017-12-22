/*
ID: warwick2
LANG: C++11
TASK: base
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
using namespace std;

#define MAX_N 100000

struct entry{
    int day;
    int cow;
    int change;
};

int n, g;
entry entries[MAX_N];
map<int,int> gallons;
vector<int> best_cows;
int prev_max;

vector<int> find_best_cows(){
    vector<int> best;
    bool first = true;
    int max;

    for (map<int,int>::iterator i=gallons.begin(); i != gallons.end(); i++){
        if (first){
            max = i->second;
            first = false;
        }
        if (i->second == max){
            best.emplace_back(i->first);
            continue;
        }
        if (i->second > max){
            max = i->second;
            best.clear();
            best.emplace_back(i->first);
            continue;
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
        gallons[cow] = g;
        entries[i] = {day, cow, change};
    }

    sort(entries, entries+n, [](entry a, entry b){
            return b.day > a.day;
        });

    int next_entry = 0;
    int changes = 0;
    int first_day = entries[0].day;
    int last_day = entries[n-1].day;

    for (int day=first_day; day<=last_day; day++){
        bool changed = false;
        while (entries[next_entry].day == day){
            int cow_num = entries[next_entry].cow;
            gallons[cow_num] += entries[next_entry].change;
            next_entry++;

            if (find(best_cows.begin(), best_cows.end(), cow_num) != best_cows.end()){
                changed = true;
            }
            if (gallons[cow_num] >= prev_max){
                changed = true;
            }
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