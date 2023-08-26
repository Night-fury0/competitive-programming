#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

void func_twist(long a,long b){
    cout<<2<<"\n";

    if (b-1 > 0 && b-1 % a != 0){
        cout<<a<<" "<<b-1<<"\n";
        cout<<a<<" "<<b<<"\n";
    }
    else{
        cout<<a-1<<" "<<b<<"\n";
        cout<<a<<" "<<b<<"\n";
    }
}

void func(long a, long b){
    cout<<1<<"\n";
    cout<<a<<" "<<b<<"\n";
}

int main(){
    int t;
    freopen("input.txt", "r", stdin);
    cin>>t;
    while(t--){
        long a,b;
        cin>>a>>b;
        if (a==1 && b==1) func(a,b);
        else if (a==b) func_twist(a,b);
        else if (a>b){
            if (a%b == 0) func_twist(a,b);
            else func(a,b);
        }
        else{
            if (b%a == 0) func_twist(a,b);
            else func(a,b);
        }
        }
    
}