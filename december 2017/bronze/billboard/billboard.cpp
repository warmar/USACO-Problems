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

struct rectangle{
    int left;
    int top;
    int right;
    int bottom;
};

int total;
rectangle truck;

void add_to_total(rectangle rect){
    int width = rect.right-rect.left;
    int height = rect.top-rect.bottom;
    total += width*height;
}

void subtract_from_total(rectangle rect){
    for (int x=rect.left; x<rect.right; x++){
        for (int y=rect.bottom; y<rect.top; y++){
            // Check if x in truck
            if (x >= truck.left && x < truck.right){
                // Check if y in truck
                if (y >= truck.bottom && y < truck.top){
                    total--;
                }
            }
        }
    }
}

int main(void){
	ifstream fin("billboard.in");
    ofstream fout("billboard.out");

    rectangle billboard0;  
    rectangle billboard1;

    fin >> billboard0.left >> billboard0.bottom >> billboard0.right >> billboard0.top;
    fin >> billboard1.left >> billboard1.bottom >> billboard1.right >> billboard1.top;
    fin >> truck.left >> truck.bottom >> truck.right >> truck.top;

    add_to_total(billboard0);
    add_to_total(billboard1);

    cout << total << "\n";

    subtract_from_total(billboard0);
    subtract_from_total(billboard1);

    cout << total << "\n";


    fout << total << "\n";
    return 0;
}