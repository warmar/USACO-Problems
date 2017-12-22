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
int16_t loops[MAX_N];

int main(void){
	ifstream fin("shuffle.in");
    ofstream fout("shuffle.out");

    fin >> n;
    for (int i=0; i<n; i++){
        fin >> as[i];
        as[i] = as[i]-1;
    }

    for (int i=0; i<n; i++){
        if (loops[i]) continue; //already in a loop
        if (loops[i] == -1) continue; //already known bad
        
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
                loops[i] = -1;
                // set true for next
                loops[next] = true;

                int inner_loop = next;
                do {
                    inner_loop = as[inner_loop];
                    loops[inner_loop] = true;
                } while (inner_loop != next);

                break;
            }
            
            if (loops[next] == -1){
                // All visited are bad if they lead to a bad one
                for (int pos : visited){
                    loops[pos] = -1;
                }
                break;
            }
            visited.insert(next);
            prev = next;
        }

        if (didloop){
            for (int pos : visited){
                loops[pos] = 1;
            }
        }        
    }

    int num_filled = 0;
    for (int i=0; i<n; i++){
        if (loops[i]==1) {
            num_filled++;
        }
    }

    fout << num_filled << "\n";
    return 0;
}