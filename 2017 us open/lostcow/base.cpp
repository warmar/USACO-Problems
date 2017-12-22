#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
using namespace std;

int x,y;

int main(void){
	ifstream fin("lostcow.in");
    ofstream fout("lostcow.out");

    fin >> x;
    fin >> y;

    int move = 1;
    int traveled = 0;
    int prev = x;
    int curr = x;

    while (true){
        prev = curr;
        curr = x+move;
        traveled += abs(curr-prev);

        if (y > x){
            if (curr >= y){
                traveled -= abs(y-curr);
                break;
            }
        } else {
            if (curr <= y){
                traveled -= abs(y-curr);
                break;
            }
        }

        move *= -2;
    }

    cout << traveled << "\n";
    fout << traveled << "\n";
    return 0;
}