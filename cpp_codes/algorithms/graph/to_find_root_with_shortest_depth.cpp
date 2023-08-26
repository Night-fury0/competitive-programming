#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

map<int,vector<int>> children;

vector<int> find_depth(map<int,set<int>> &m, int initial_root, int root, vector<int> visited){
    vector<int> largest_route;
    for (auto x: m[root])
        if (find(visited.begin(), visited.end(), x) == visited.end()){        
            visited.push_back(x);
            vector<int> res = find_depth(m,initial_root, x, visited);
            if (root == initial_root){
                children[x] = res;
            }
            if (res.size() > largest_route.size()){
                largest_route = res;
            }
            visited.pop_back();
        }
    if (largest_route.size() < visited.size()) largest_route = visited;
    return largest_route;
}

int main(){
    int t;
    freopen("to_find_root_with_shortest_depth.txt","r",stdin);
    cin>>t;
    while(t--){
        children.clear();
        int n,u,v;
        cin>>n;
        map<int, set<int>> m;
        for (int i=0;i<n-1;i++){
            cin>>u>>v;
            m[u].insert(v);
            m[v].insert(u);
        }
        int root;
        for (auto x:m){
            if (x.second.size() > 1){
                root = x.first;
                break;
            }
        }
        cout<<"chosen initial root: "<<root<<"\n";
        vector<int> visited;
        visited.push_back(root);
        vector<int> b = find_depth(m,root, root,visited);

        // cout<<"largest route: ";
        // for (auto x: b) cout<<x<<" ";  cout<<"\n";

        int no = children.size();
        int root_for_largest_route = 0;
        vector<int> nos, largest_route;
        for (auto x: children){
            if (x.second.size() > largest_route.size()){
                root_for_largest_route = x.first;
                largest_route = x.second;
            }
            nos.push_back(x.second.size()-1);
        }
        sort(nos.begin(), nos.end());
        // cout<<"nos "<<nos[no-1]<<" "<<nos[no-2]<<"\n";
        if (nos[no-1] > nos[no-2] + 1){
            int change = nos[no-1] - ceil((nos[no-1] + nos[no-2])/2);
            root = largest_route[change];
            cout<<"new root is "<<root<<"\n";
        }
        else cout<<"no change in root\n";
        // we have chosen the optimal root, now print the structure such that every lca of each adjacent vertex no is 1.


    }
}