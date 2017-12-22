/*
ID: warwick2
LANG: C++11
TASK: skidesign
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
#include <cmath>
using namespace std;

#define MAX_N 1000
#define MAX_DIFFERENCE 17

int n, heights[MAX_N];

int find_cost(bool raise_low_more){
    int cost = 0;
    int index = 0;

    int biggest_d = heights[n-1] - heights[0];
    if (biggest_d <= MAX_DIFFERENCE){
        return 0;
    }
    int change = (biggest_d-MAX_DIFFERENCE);
    int raise_low = change/2;
    int lower_high = change/2;
    if (change % 2 != 0){
        if (raise_low_more){
            raise_low++;
        } else {
            lower_high++;
        }
    }
    cost += pow(raise_low, 2);
    cost += pow(lower_high, 2);
    
    heights[0] += raise_low;
    heights[n-1] -= lower_high;

    cout << heights[0] << "\n";
    cout << heights[n-1] << "\n";

    for (int i=1; i<n-1; i++){
        int height = heights[i];

        if (height < heights[0]){
            cost += pow(heights[0]-height,2);
        }
        if (height > heights[n-1]){
            cost += pow(height-heights[n-1],2);
        }
    }

    return cost;
}

int main(void){
	ifstream fin("skidesign.in");
    ofstream fout("skidesign.out");
    fin >> n;
    for (int i=0; i<n; i++){
        fin >> heights[i];
    }

    sort(heights, heights+n);

    fout << find_cost(true) << "\n";
    return 0;
}