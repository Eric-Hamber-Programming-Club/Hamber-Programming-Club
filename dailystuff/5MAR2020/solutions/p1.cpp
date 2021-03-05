#include <bits/stdc++.h>

using namespace std;
int n, k;
int m[250][250][130];
int phi(int a, int b, int c){
    if (b==1) return 1;
    if (m[a-1][b-1][c-1] != -1)
        return m[a-1][b-1][c-1];
    int s=0;
    for (int i=c; i<=(a/b); i++){
        s=s+phi(a-i, b-1, i);
    }
    m[a-1][b-1][c-1] = s;
    return s;
}

int main() {
    cin >> n;
    cin >> k;
    memset(m, -1, sizeof(m)); 
    cout << phi(n, k, 1);
    return 0;
}

