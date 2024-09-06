#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <memory.h>
#define FIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(0);
using namespace std;
const int INF = 1e9;

int n, m;
int a, b, c;
int parent[1000001];

int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

void Union(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) return;
    parent[b] = a;
}
int main() {
    FIO;
    cin >> n >> m;
    for (int i = 0; i < n+1; i++)
        parent[i] = i;
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        if (a == 0) {
            Union(b, c);
        }
        else if (a == 1) {
            if (find(b) == find(c))
                cout << "YES" << '\n';
            else if (find(b) != find(c))
                cout << "NO" << '\n';
        }
    }
}