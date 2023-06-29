#https://codeforces.com/blog/entry/101380

#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    scanf("%d", &t);
//    cin >> t;
    while (t--) {
        int n;
        scanf("%d", &n);
        vector<int> nums(n), used(n + 1);
        for (auto &i : nums) {
            scanf("%d", &i);
        }
        sort(nums.begin(), nums.end(), [](int a, int b) { return a > b; });
        bool isOk = true;
        for (auto &num : nums) {
            int x = num;
            while (x > n || used[x]) {
                x /= 2;
            }
            if (x) used[x] = 1;
            else {
                isOk = false;
                break;
            }
        }
        printf("%s\n", isOk ? "YES" : "NO");
    }
}