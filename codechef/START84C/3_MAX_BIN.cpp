#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;


int main(){

    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        string b;
        cin>>b;
        if (b[0] == '0') {
            b[0] = '1';
            k--;
        }
        b = b + string(k,'0');
        cout<<b<<"\n";


    }
    return 0;
}