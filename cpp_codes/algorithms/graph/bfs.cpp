#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){

    int n,u,v;
    freopen("input.txt","r", stdin);
    cin>>n;
    map<int,set<int>> m;
    for (int i=0;i<n-1;i++){
        cin>>u>>v;
        m[u].insert(v);
    }
    // breadth first search
    queue <int> q;
    // let 0 be the root by default
    q.push(0);
    int dist[n];
    memset(dist, 0, sizeof(dist));
    
    while(!q.empty()){
        int x = q.front();
        cout<<x<<" ";
        q.pop();
        for (auto y: m[x])
            if (dist[y] == 0){    
                dist[y] = dist[x]+1;
                q.push(y);    
            }    
    }
    cout<<"\n";
    for (int i=0;i<n;i++)
        cout<<i<<" shortest distance from 0 is: "<<dist[i]<<"\n";

        

}