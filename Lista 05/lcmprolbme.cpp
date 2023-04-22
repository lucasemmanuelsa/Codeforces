#include <iostream>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int l, r;
        cin >> l >> r;

        int x = l;
        int y = 2*x;
        if(y>r){
            cout << "-1 -1" << endl;
        }else{
            cout << x << " " << y << endl;
        }
        
    }
    return 0;
}
