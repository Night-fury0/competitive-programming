#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

const int MOD = 1000000007;

int main(){

    int t;
    // freopen("7_AWESUM_OR_input.txt","r",stdin);
    cin>>t;
    while (t--){
        long long n;
        cin>>n;
        long long result = 1;
        int no = __builtin_popcountll(n);
        if (no < 3) result = 0;
        else{
            long long zero_case = 1;
            while(no--){
                result = (result*3) % MOD;
                zero_case = (zero_case*2) % MOD;
            }
            result = (result - 3*zero_case + 3) % MOD;
            
        }
        if (result<0) result += MOD;
        cout<<result<<"\n";
    }
    

}