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
bool loops[MAX_N];

int main(void){
	ifstream fin("shuffle.in");
    ofstream fout("shuffle.out");

    fin >> n;
    for (int i=0; i<n; i++){
        fin >> as[i];
        as[i] = as[i]-1;
    }

    set<int> bad_visited;
    for (int i=0; i<n; i++){
        if (loops[i]) continue; //already in a loop
        if (bad_visited.count(i)) continue; //already known bad
        
        bool didloop = false;

        int prev = i;
        set<int> visited;
        visited.insert(i);
        while (true){
            int next = as[prev];
            if (next==i){ // full loop
                didloop = true;
                break;
            }
            if (visited.count(next)){ // next is in loop but loop didn't include i
                bad_visited.insert(i);
                // set true for next
                loops[next] = true;

                int inner_loop = next;
                do {
                    inner_loop = as[inner_loop];
                    loops[inner_loop] = true;
                } while (inner_loop != next);

                break;
            }
            if (bad_visited.count(next)){
                // All visited are bad if they lead to a bad one
                for (int pos : visited){
                    bad_visited.insert(pos);
                }
                break;
            }
            visited.insert(next);
            prev = next;
        }

        if (didloop){
            for (int pos : visited){
                loops[pos] = true;
            }
        }        
    }

    int num_filled = 0;
    for (int i=0; i<n; i++){
        if (loops[i]) {
            num_filled++;
        }
    }

    fout << num_filled << "\n";
    return 0;
}