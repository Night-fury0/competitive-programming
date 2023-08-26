#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;


int no_of_nodes(map<int,set<int>> &m, int root, bool visited[]){
    int no=0; 
    for (auto x: m[root])
        if (!visited[x-1]){
            no++;
            visited[x-1] = true;
            no += no_of_nodes(m,x,visited);
        }
    // cout<<"no of nodes is "<<no<<" while leaving vertex "<<root<<"\n";
    return no;
}

int main(){
    int t;
    freopen("input.txt","r",stdin);
    cin>>t;
    while(t--){
        int n,u,v;
        cin>>n;
        map<int, set<int>> m;
        for (int i=0;i<n-1;i++){
            cin>>u>>v;
            m[u].insert(v);
            m[v].insert(u);
        }
        int root = 1;
        for (auto x:m){
            if (x.second.size() > 1){
                root = x.first;
                break;
            }
        }
        
        while(true){
            map<int,int> neighbour_node_count;
            bool visited[n];
            memset(visited, false, sizeof(visited));
            visited[root-1] = true;
            for (auto x: m[root]){
                visited[x-1] = true;
                neighbour_node_count[x] = no_of_nodes(m,x,visited);
            }
            bool flag = false;
            for (auto x:neighbour_node_count){
                if (x.second > ((n-1)/neighbour_node_count.size())){
                    root = x.first;
                    flag = true;
                    break;
                }
            }
            if (!flag) break;
        }
        cout<<"optimal root "<<root<<"\n";
        // choosing the root is not about only the no. of immediate connections the vertex has, or the longest depth it can lead to, 
        // but the total no. of vertices that it can lead to.
    }
}