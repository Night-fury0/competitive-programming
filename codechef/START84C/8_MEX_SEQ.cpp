#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

long long MOD = 1000000007;

int no_seqs_starting_with_0_no_res_on_m(int n){
    if (n == 1) return 1;
    else if (n==2) return 3;
    else{
        int res = 0;
        long long pow_of_2_for_3 = 1;
        long long pow_of_2_for_2 = 1;
        for (int i=3;i<=n;i++){
            pow_of_2_for_2 = (pow_of_2_for_2 * 2) % MOD;
            res = ((res*2) + pow_of_2_for_2) % MOD;
            pow_of_2_for_3 = (pow_of_2_for_3 * 2) % MOD;
        }
        res = (res + 3*pow_of_2_for_3) % MOD;
        return res;
    }
}


long ncr(int n, int r)
{
    long long p = 1, k = 1;
    if (n - r < r)
        r = n - r;
    if (r != 0) {
        while (r) {
            p *= n;
            k *= r;
            long long m = __gcd(p, k);
            p /= m;
            k /= m;
            n--;
            r--;
        }
    }
     else
        p = 1;
    return p % MOD;
}

int count_possiblities(int n, int r){
    long long res = 1;
    for (int i=1;i<=r;i++) res = ((res * (n+i-1) % MOD)/i) % MOD;
    return res;
}

int main(){
    int t;
    // freopen("8_MEX_SEQ_input.txt", "r", stdin);
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        long long count=0;
        if (m==0) cout<<1<<"\n";
        else{
            if (m > 0) count = 1;
            else count = 0;
            vector<int> a ={0};
            long long res = no_seqs_starting_with_0_no_res_on_m(n);
            // cout<<"total for n="<<n<<" is : "<<res<<"\n";
            count = (count + res) % MOD;
            long long sub = 0;
            if (m+1==n) sub ++;
            else if (m < n){
                // subtract cases where seq uses ele >m from count.
                // for i==m case, pow(2,n-m-1)
                // for i==m+1
                int no = n-m-1;
                long long pow_of_2 = 1;
                // cout<<"remaining is "<<n-m-1<<"\n";
                while (no--)  {pow_of_2 = (pow_of_2 * 2) % MOD;}
                sub += pow_of_2;
                // cout<<"for unrequired nos in index "<<m<<" no of seq to reduce is "<<sub<<"\n";
                long long pow_of_m = 0, pow_of_m_plus_1 = 1;
                for (int i=m+1;i<n;i++){
                    // count the no of possiblities i.e pow_of_m and pow_of_m_plus_1 properly, only pending part.
                    // cout<<"i="<<i<<" for pow_of_m, calculating ncr("<<i-m+1<<","<<m-1<<")\n";
                    if (i-m>m) {pow_of_m = count_possiblities(i-m+1,m-1) % MOD; }
                    else {
                        pow_of_m = 0;
                        for (int j=1;j<=i-m;j++)
                            pow_of_m = (pow_of_m + ncr(m, j) * ncr(i-m-1,j-1)) % MOD;
                    }
                    pow_of_2 = pow_of_2 / 2;
                    // if (i==n-1){sub at i="<<i<<" # "<<pow_of_2<<" "<<pow_of_m<<" "<<no_seqs_starting_with_0_no_res_on_m(n-i)<<" "<<pow_of_m_plus_1<<" "<<pow_of_2<<"\n";
                    sub = (sub + pow_of_m*pow_of_2 + pow_of_m_plus_1*no_seqs_starting_with_0_no_res_on_m(n-i) + pow_of_m_plus_1*pow_of_2) % MOD;
                    // cout<<"i="<<i<<" for pow_of_m+1, calculating ncr("<<i-m+1<<","<<m<<")\n";
                    if (i-m>m+1){pow_of_m_plus_1 = count_possiblities(i-m+1,m) % MOD; }
                    else {
                        pow_of_m_plus_1 = 0;
                        // cout<<"pow_of_m+1 starting from 0"<<"\n";
                        for (int j=1;j<=i-m;j++){
                            // cout<<"adding ncr("<<m+1<<","<<j<<") * ncr("<<i-m<<","<<j-1<<") \n";
                            pow_of_m_plus_1 = (pow_of_m_plus_1 + ncr(m+1,j) * ncr(i-m-1,j-1)) % MOD;
                        }
                        // cout<<"for i= "<<i+1<<" pow_of_m+1 is "<<pow_of_m_plus_1<<"\n";
                    }
                    // cout<<"for unrequired nos in index "<<i<<" no of seq to reduce is "<<sub<<"\n";

                }
            }
            count = count - sub;
            if (count<0) count+=MOD;
            cout<<count<<"\n";
        }
    }
            // cout<<"no. of seq starting with 0 for n="<<n<<" : "<<count<<endl;
        
        // use normal O(n) formula to find no. od seq starting with 0 for m+1 > n, but need to know how to remove count the no. of seqs to remove from that vontaining elements > m.
    

    // Observations:    
    // for 1,_: any n is 1
    // for 2,_: - not possible
    // for 3,_: n=2 is 3 but anything for b>=3, its pow(2,n-1) - not possible

}
    