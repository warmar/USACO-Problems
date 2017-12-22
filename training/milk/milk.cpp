/*
ID: warwick2
LANG: C++11
TASK: milk
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <list>
using namespace std;

#define MAX_N 2000000
#define MAX_M 5000

struct farmer{
    int price;
    int amount;
};

int n, m;
farmer farmers[MAX_M+1];

bool compare_farmers(farmer i, farmer j){
    return i.price < j.price;
}

int main(void){
	ifstream fin("milk.in");
    ofstream fout("milk.out");
    
    fin >> n >> m;
    for (int i=0; i<m; i++){
        int price, amount;
        fin >> price >> amount;
        farmers[i] = {price, amount};
    }

    sort(farmers, farmers+m, compare_farmers);

    int cost = 0;
    int n_remaining = n;

    for (int i=0; i <m; i++){
        farmer a = farmers[i];
        n_remaining -= a.amount;
        cost += a.price*a.amount;

        if (n_remaining <= 0){
            cost += a.price*n_remaining;
            break;
        }
    }

    cout << cost << "\n";
    fout << cost << "\n";
    
    return 0;
}