#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){

    int t;
    cin>>t;
    while(t--){
        int n,x, temp;
        cin>>n>>x;
        int count =0 ;

        for(int i=0;i<n;i++){
            cin>>temp;
            if (temp>=x) count++;
        }
        cout<<count<<"\n";
    }
    return 0;
}