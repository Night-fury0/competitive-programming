
#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

bool comparator(pair<int,int>a, pair<int,int>b){
    if (a.second < b.second)
        return true;
    return false;
}

int main(){
    int t;
    freopen("4_UTLA_input.txt", "r", stdin);
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> a(n);
        for (int i=0;i<n;i++) cin>>a[i];
        map<int, vector<pair<int,int>>> sums;
        for (int i=0;i<n;i++)
            for (int j=0;j<i;j++)
                sums[a[i] + a[j]].push_back(make_pair(j,i));
        int max_count = 0;
        for (auto x: sums){
            sort(x.second.begin(),x.second.end(),comparator);
            int rmax = -1;
            int count = 0;
            for (auto y:x.second)
                if (y.first > rmax){
                    count++;
                    rmax = y.second;
                }
            max_count = max(max_count,count);
        }
        cout<<n-2*max_count<<"\n";
    }
}