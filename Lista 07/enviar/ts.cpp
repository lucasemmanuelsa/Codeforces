#include <iostream>
#include <vector>

using namespace std;

using ll = long long;
const ll MOD = 1e9 + 7;

vector<ll> fact, inv;

ll pow_mod(ll x, ll n) {
    ll res = 1;
    while (n > 0) {
        if (n & 1) res = res * x % MOD;
        x = x * x % MOD;
        n >>= 1;
    }
    return res;
}

void init(int maxN) {
    fact.resize(maxN + 1);
    inv.resize(maxN + 1);

    fact[0] = 1;
    for (int i = 1; i <= maxN; i++) {
        fact[i] = fact[i - 1] * i % MOD;
    }

    inv[maxN] = pow_mod(fact[maxN], MOD - 2);
    for (int i = maxN - 1; i >= 0; i--) {
        inv[i] = inv[i + 1] * (i + 1) % MOD;
    }
}

ll choose(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD;
}

int main() {
    int N, M;
    cin >> N >> M;

    init(N + M);

    cout << choose(N + M - 1, M) << endl;

    return 0;
}
