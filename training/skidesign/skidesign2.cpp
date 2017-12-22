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

int find_cost(bool bottom_bigger){
    int min_cost;
    bool first = true;
    for (int mid_height=1; mid_height<=100; mid_height++){
        int cost = 0;

        for (int i=0; i<n; i++){
            int height = heights[i];

            int top_gap, bottom_gap;
            if (bottom_bigger){
                top_gap = 8;
                bottom_gap = 9;
            } else {
                top_gap = 9;
                bottom_gap = 8;
            }

            int lower_limit = mid_height - bottom_gap;
            int upper_limit = mid_height + top_gap;

            if (height < lower_limit){
                int difference = lower_limit-height;
                cost += pow(difference, 2);
            }
            if (height > upper_limit){
                int difference = height-upper_limit;
                cost += pow(difference, 2);
            }
        }

        if (first) {
            min_cost = cost;
            first = false;
        } else {
            min_cost = min(cost, min_cost);
            // cout << "height" << mid_height << "cost" << cost << "\n";
        }
    }
    return min_cost;
}

int main(void){
	ifstream fin("skidesign.in");
    ofstream fout("skidesign.out");
    fin >> n;
    for (int i=0; i<n; i++){
        fin >> heights[i];
    }

    sort(heights, heights+n);

    int min_cost = min(find_cost(true), find_cost(false));

    fout << find_cost(false) << "\n";
    return 0;
}