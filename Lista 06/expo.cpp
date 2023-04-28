#include <iostream>
using namespace std;

const int MOD = 1e9 + 7;

int power(int a, int b) {
    int res = 1;
    while (b > 0) {
        if (b & 1) {
            res = (1LL * res * a) % MOD;
        }
        a = (1LL * a * a) % MOD;
        b >>= 1;
    }
    return res;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int a, b;
        cin >> a >> b;
        int result = power(a, b);
        cout << result << endl;
        
    }
    return 0;
}
