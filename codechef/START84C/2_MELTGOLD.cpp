#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){

    int t;
    cin>>t;
    while(t--){
        int x,y;
        cin>>x>>y;
        int count = 0;
        while(true){
            count++;
            y += count;
            if (y >= x) break;
        }
        cout<<count<<"\n";
    }
    return 0;
}