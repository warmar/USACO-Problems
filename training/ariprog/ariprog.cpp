/*
ID: warwick2
LANG: C++11
TASK: ariprog
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
#include <cmath>
using namespace std;

#define MAX_N 25
#define MAX_M 250


int n, m;
bool bisquares[2*MAX_M*MAX_M];

struct sequence{
    int first;
    int difference;
};

bool sort_sequences(sequence a, sequence b){
    if (b.difference > a.difference) return true;
    if (b.difference < a.difference) return false;
    return b.first > a.first;
}

sequence found[10000];
int num_found;

bool is_bisquare(int num){
    return bisquares[num];
}

int main(void){
	ifstream fin("ariprog.in");
    ofstream fout("ariprog.out");

    fin >> n >> m;

    // find all bisquares    
    for (int p=0; p<=m; p++){
        for (int q=p; q<=m; q++){
            bisquares[p*p + q*q] = true;
        }
    }

    // cout << "done\n";

    int max_a = 2*m*m - n + 1; // m^2 + m^2 - n

    int good_sequences = 0;

    // cout << "n" << n << "\n";
    // cout << "m" << m << "\n";
    // cout << "maxa" << max_a << "\n";

    for (int a=0; a<=max_a; a++){
        if (!is_bisquare(a)){
            continue;
        }

        int max_b = ((2*m*m)-a)/(n-1);
        for (int b=1; b<=max_b; b++){
            bool good = true;
            for (int i=1; i<n; i++){
                int next = a + i*b;
                if (!is_bisquare(next)){
                    good = false;
                    break;
                }
            }

            if (good){
                good_sequences++;
                sequence k = {a, b};
                found[num_found] = k;
                num_found++;
            }
        }
    }

    sort(found, found+num_found, sort_sequences);

    cout << good_sequences << "\n";

    if (good_sequences == 0){
        fout << "NONE\n";
    } else {
        for (int i=0; i<num_found; i++){
            fout << found[i].first << " " << found[i].difference << "\n";
        }
    }
    return 0;
}