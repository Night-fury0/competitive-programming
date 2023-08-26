#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define f first
#define s second
#define mp make_pair
#define rep(a,b) for (int i=a;i<b;i++)

using namespace std;

vector<int> subset;

void generate_subsets(int i, int n){
    if (i == n+1){
        for(auto x: subset)
            cout<<x<<" ";
        cout<<endl;
    }
    else {
        subset.push_back(i);
        generate_subsets(i+1, n);
        subset.pop_back();
        generate_subsets(i+1, n);        
    }
}

int main(){
    int k = 5;
    generate_subsets(1,k);
}