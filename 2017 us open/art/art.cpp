#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#define MAX_N 1000
#define MAX_C (MAX_N*MAX_N)
using namespace std;

int n;
int square[MAX_N+1][MAX_N+1];
int rectangles[MAX_C][4];
set<int> used_colors;

int main(void){
    ifstream fin("art.in");
    ofstream fout("art.out");
    // load input
    fin >> n;
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            fin >> square[i][j];
            used_colors.insert(square[i][j]);
        }
    }


    for (int color=1; color<n*n+1; color++){
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                if (square[i][j] == color) {
                    rectangles[color][0] = min(rectangles[color][0], i);
                    rectangles[color][1] = min(rectangles[color][1], j);
                    rectangles[color][2] = max(rectangles[color][2], i);
                    rectangles[color][3] = max(rectangles[color][3], j);
                }
            }
        }
    }

    int possible_first = n*n;
    set<int> colors;

    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            if (colors.count(square[i][j])){
                continue;
            }

            int intersections = 0;
            for (int color=1; color<n*n+1; color++){
                if (i >= rectangles[color][0] && i <= rectangles[color][2] && j >= rectangles[color][1] && j <=rectangles[color][3]){
                    intersections++;
                }
                if (intersections >= 2){
                    colors.insert(square[i][j]);
                    possible_first--;
                    cout << color << "\n";
                    break;
                }
            }
            if (intersections >= 2){
                break;
            }
        }
    }

    cout << possible_first;
    fout << possible_first << "\n";

    return 0;
}