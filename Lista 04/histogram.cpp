#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, i;
    while (cin >> n && n) {
        vector<int> v(n);
        for (i = 0; i < n; i++) {
            cin >> v[i];
        }
        stack<int> s;
        long long ans = 0;
        i = 0;
        while (i < n) {
            if (s.empty() || v[s.top()] <= v[i]) {
                s.push(i++);
            } else {
                int t = s.top();
                s.pop();
                ans = max(ans, (long long)v[t] * (s.empty() ? i : i - s.top() - 1));
            }
        }
        while (!s.empty()) {
            int t = s.top();
            s.pop();
            ans = max(ans, (long long)v[t] * (s.empty() ? i : i - s.top() - 1));
        }
        cout << ans << endl;
    }
    return 0;
}
