#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;


int main(){

    int t;
    // freopen("5_input.txt","r",stdin);
    cin>>t;
    while(t--){
        int n, temp;
        cin>>n;
        vector<int> a;
        for(int i=0;i<n;i++){
            cin>>temp;
            a.push_back(temp);
        }
        sort(a.begin(),a.end());
        if (a[0] == a[n-1]) cout<<"No"<<"\n";
        else{
            int z = a[n-1] + a[n-2];
            int value = a[n-1];
            int no = lower_bound(a.begin(),a.end(),value) + 1;
            if (no < n-1) cout<<"Yes"<<"\n";
            else cout<<"No"<<"\n";

        }
        

    }
    return 0;
}