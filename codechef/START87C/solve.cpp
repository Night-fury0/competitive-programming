#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

bool MyComparator(pair<int, int> a, pair<int, int> b) {
    float one = (float) a.second/a.first;
    float two = (float) b.second/b.first;
    if(one > two){
        return true;
    } 
    return false;
}

void gfgGame(int N, int G, vector<int> &require, vector<int> &recieve) {
    // code here
    int score = G, no = 0;
    vector<pair<int,int>> a;
    for (int i=0;i<N;i++)
        a.push_back(make_pair(require[i], recieve[i]));
    sort(a.begin(),a.end(), MyComparator);
    for (auto x:a) cout<<x.first<<" "<<x.second<<"\n";
    
}

int main(){
    bitset<100000> a;
    cout<<1<<a;
}
