#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

const int N = 1000001;
int main(){
    int primes[N];
    memset(primes,0,sizeof(primes));
    for (int i=2;i*i<N;i++)
        if (primes[i] == 0)
            for (int j=i*i;j<N;j+=i) 
                primes[j] = i;

    int t;
    // freopen("input.txt","r",stdin);
    cin>>t;
    while(t--){
        // cout<<"no error till here for t="<<t<<"\n";
        int n, m;
        cin>>n>>m;
        vector<int> a(n);
        set<int> a_pf, pf, gcd;
        bool all_same = true;
        for (int i=0;i<n;i++){
            cin>>a[i];
            int no =a[i];
            if (i>0 && a[i] != a[i-1]) all_same = false;
            pf.clear();
            while (no>1){
                int j = primes[no];
                if (j==0) j = no;
                while(no%j==0) no/=j;
                pf.insert(j);
            }
            if (i==0) gcd=pf;
            else if (!gcd.empty()){
                set<int> new_gcd;
                // cout<<"gcd had : ";
                // for (auto x: gcd) cout<<x<<" "; cout<<"pf has :"; for (auto x:pf) cout<<x<<" ";
                // cout<<"\n";
                set_intersection(gcd.begin(),gcd.end(),pf.begin(),pf.end(), inserter(new_gcd, new_gcd.begin()));
                gcd = new_gcd;
            }
            a_pf.insert(pf.begin(),pf.end());
        }
        // cout<<"the problem must be before this t="<<t<<"\n";
        // no. of prime numbers between 2 and M
        if (all_same){
            cout<<0<<"\n";
        }
        else if (!gcd.empty()){
            // cout<<"coming from gcd\n";
            cout<<1<<"\n"<<*gcd.begin()<<"\n";
        }
        else{
            int last_prime=2;
            int i=2;
            while(i<=m){
                if (primes[i]==0){
                    last_prime = i;
                    if (a_pf.find(i) == a_pf.end()) break;
                }
                i++;
            }
            if (i<=m) cout<<1<<"\n"<<last_prime<<"\n";
            else cout<<2<<"\n"<<"2 3\n"; 
        }
    }

}