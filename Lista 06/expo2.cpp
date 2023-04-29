#include <iostream>
using namespace std;

const int MOD = 1e9 + 7;

int power(int a, int b, int m) {
    int res = 1;
    while (b > 0) {
        if (b & 1) {
            res = (1LL * res * a) % m;
        }
        a = (1LL * a * a) % m;
        b >>= 1;
    }
    return res;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int a, b, c;
        cin >> a >> b >> c;
        int result1 = power(b, c, MOD - 1);
        int result = power(a,result1, MOD);
        cout << result << endl;
        
    }
    return 0;
}
