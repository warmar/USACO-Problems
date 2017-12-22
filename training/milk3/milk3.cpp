/*
ID: warwick2
LANG: C++11
TASK: milk3
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
#include <cmath>
#include <vector>
using namespace std;

#define MAX_VOLUME 20

int a, b, c;
int max_cap[3];
int state[3];
set<int> all_c_volumes;
bool visited[MAX_VOLUME][MAX_VOLUME][MAX_VOLUME];

void pour(){
    // Don't go deeper if at an already-visisted state
    if (visited[state[0]][state[1]][state[2]]){
        return;
    }
    visited[state[0]][state[1]][state[2]] = true;

    for (int source=0; source<3; source++){
        for (int dest=0; dest<3; dest++){
            if (source==dest){ // Can't pour bucket into itself
                continue;
            }

            // Copy state to revert it after search
            int prev[3];
            copy(state, state+3, prev);

            // Do pour
            int available = state[source];
            int room_left = max_cap[dest] - state[dest];

            if (available == 0){ // Nothing to pour
                continue;
            }
            if (room_left == 0){ // No room in destination
                continue;
            }

            int moved = min(available, room_left);
            state[source] -= moved;
            state[dest] += moved;

            // Check if a was emptied and add c's volume to curr_volumes
            if (source == 0 && state[source] == 0){
                all_c_volumes.insert(state[2]);
            }

            pour();

            // Revert state to previous
            copy(prev, prev+3, state);
        }
    }

}

int main(void){
	ifstream fin("milk3.in");
    ofstream fout("milk3.out");

    fin >> a >> b >> c;
    state[0] = 0;
    max_cap[0] = a;
    state[1] = 0;
    max_cap[1] = b;
    state[2] = c;
    max_cap[2] = c;
    
    pour(); // Perform search

    vector<int> sorted_volumes;
    for (int vol : all_c_volumes){
        sorted_volumes.emplace_back(vol);
    }
    sort(sorted_volumes.begin(), sorted_volumes.end());

    for (int i=0; i<sorted_volumes.size(); i++){
        fout << sorted_volumes.at(i);
        if (i < sorted_volumes.size()-1){ // Add space after all but the last one
            fout << " ";
        }
    }

    fout << "\n";
    return 0;
}