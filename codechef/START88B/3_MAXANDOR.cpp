#include<bits/stdc++.h>

#define ios_base : sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

const int N = 30;

int main(){
    int t;
    // freopen("input.txt","r",stdin);
    cin>>t;
    while(t--){
        int a,b,c;
        cin>>a>>b>>c;
        bitset<N> x(b);
        bitset<N> y(a);
        int count = 0;
        for (int i=0;i<c;i++){
            if (x[i] == 0) x[i] = 1;
            else x[i] = 0;
            if ((x[i]==0 && y[i]==0) || (x[i]==1 && y[i]==1)) count++;
        }
        cout<<pow(2,count)<<"\n";
    }
}