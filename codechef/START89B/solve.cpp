#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,q;
        cin>>n>>q;
        vector<int> a(n);
        for (int i=0;i<n;i++) cin>>a[i];
        sort(a.begin(),a.end(),greater<int>());
        vector<pair<int,int>> s(n,make_pair(0,0));
        for (int i=0;i<n;i++)
            s[i].second = i;
        int l,r;
        while(q--){
            cin>>l>>r;
            l--;r--;
            while(l<=r) s[l++].first++;
        }
        sort(s.begin,s.end(),greater<pair<int,int>());
        vector<int> f(n);
        long long score = 0;
        for (int i=0;i<n;i++){
            f[s[i].second] = a[i];
            score += s[i].first * a[i];
        }
        cout<<score<<"\n";
        for (int i=0;i<n;i++)
            cout<<f[i]<<" ";
            cout<<"\n";
        
        }
        
}