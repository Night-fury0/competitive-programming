#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int mod = 998244353;

int pow2(int r){
    long long result  = 1;
    while(r--){
        result = (result*2)%mod;
    }
    return result;
}

int main(){
    int t;
    // freopen("input.txt", "r", stdin);
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<long long> a(n);
        for (int i=0;i<n;i++) cin>>a[i];
        // count of elements that have all 
        int count = 0;
        long long prefix_sum, suffix_sum;
        prefix_sum = a[0];
        suffix_sum = (n*(n+1)/2) - a[0];
        if (a[0] == 1) count++;
        for (int i=1;i<n;i++)   {
            prefix_sum = prefix_sum + a[i];
            suffix_sum = suffix_sum - a[i];
            long long sum_till_i = (a[i])*(a[i]+1)/2;
            if ((prefix_sum == sum_till_i) && (suffix_sum == (n*(n+1)/2) - sum_till_i) && (a[i]==i+1)) {
                count++;
                // cout<<a[i]<<"#";
            }
        }
        // cout<<"used array: "; for (auto x: used) cout<<x<<" "; cout<<"\n";
        // cout<<"no of inversions: "<<ct<<"\n";
        if (count == n) cout<<(pow2(count)-1)%mod<<"\n";
        else    cout<<pow2(count)<<"\n";
    }
}