#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;


void traverse(map<int,set<int>> &m, int root){
    for (auto x:m[root]){
        cout<<x<<" ";
        traverse(m,x);
    }
}

int main(){

    int n,u,v;
    freopen("input.txt", "r", stdin);
    cin>>n;
    map <int,set<int>> m;
    for (int i=0;i<n-1;i++){
        cin>>u>>v;
        m[u].insert(v);
    }
    bool visited[n];
    memset(visited, false, sizeof(visited));
    cout<<0<<" ";
    traverse(m, 0);

}