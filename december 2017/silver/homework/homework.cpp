/*
ID: warwick2
LANG: C++11
TASK: homework
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
#include <cmath>
using namespace std;

#define MAX_N 100000
#define MAX_SCORE 10000;

int n, grades[MAX_N];

int teacher_avg(int values[], int start, int end){
    int tot = 0;
    int num = end-start-1; // -1 bc lowest is discarded

    cout << "start" << start << "end" << end << "\n";

    int lowest = MAX_SCORE+1;

    for (int i=start; i<end; i++){
        int score = values[i];
        // cout << "score" << score << "\n";
        tot += score;
        lowest = min(score, lowest);
    }

    tot -= lowest; // Remove lowest

    int avg = (tot*1000)/num;

    cout << "avg" << avg << "\n";

    return avg; // multiple by 1000 to avoid floats but to have greater precision
}

int main(void){
	ifstream fin("homework.in");
    ofstream fout("homework.out");

    fin >> n;
    for (int i=0; i<n; i++){
        fin >> grades[i];
    }

    int highest_avg = 0;
    list<int> ks;

    for (int k=1; k<=n-2; k++){
        int avg = teacher_avg(grades, k, n);
        if (avg < highest_avg){ // Average is less than highest
            continue;
        }
        if (avg == highest_avg){ // Average equals highest
            ks.emplace_back(k);
            continue;
        }
        // Average is better than previous highest
        highest_avg = avg;
        ks.clear();
        ks.emplace_back(k);
    }

    for (auto z: ks){
        // cout << z << "\n";
        fout << z << "\n";
    }

    return 0;
}