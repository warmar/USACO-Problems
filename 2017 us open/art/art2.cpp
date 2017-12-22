#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
#define MAX_N 1000
#define MAX_C (MAX_N*MAX_N)
using namespace std;

struct position{
    int i;
    int j;
};

int n;
int square[MAX_N+1][MAX_N+1];

set<int> used_colors;
list<position> positions[MAX_C];
int rectangles[MAX_C][4];

int main(void){
    ifstream fin("art.in");
    ofstream fout("art.out");
    // load input
    fin >> n;
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            int color;
            fin >> color;
            square[i][j] = color;
            
            if (color == 0){
                continue;
            }

            if (!used_colors.count(color)){
                used_colors.insert(color);
                rectangles[color][0] = n; // Set topleft to bottomright
                rectangles[color][1] = n; // Bottomright is at topleft (0, 0) by default
            }
            
            position pos = {i, j};
            positions[color].emplace_back(pos);

            rectangles[color][0] = min(rectangles[color][0], i);
            rectangles[color][1] = min(rectangles[color][1], j);
            rectangles[color][2] = max(rectangles[color][2], i);
            rectangles[color][3] = max(rectangles[color][3], j);
        }
    }

    int possible_first = n*n;

    for (int color : used_colors){
        bool intersects = false;
        for (position pos : positions[color]){
            int i = pos.i;
            int j = pos.j;
            for (int color_ : used_colors){ // Check all other colors' rectangles
                if (color_ == color){
                    continue;
                }

                int top = rectangles[color_][0];
                int left = rectangles[color_][1];
                int bottom = rectangles[color_][2];
                int right = rectangles[color_][3];
                if (i >= top && i <= bottom && j >= left && j <= right){ // If color intersects
                    intersects = true;
                    possible_first--;
                    break;
                }
            }
            if (intersects){
                break;
            }
        }
    }

    cout << possible_first << "\n";
    fout << possible_first << "\n";

    return 0;
}