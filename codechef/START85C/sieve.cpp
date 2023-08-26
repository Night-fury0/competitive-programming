#include<bits/stdc++.h>

using namespace std;


const int N = 1000001;

int min_prime[N];
void sieve(int n) {
    memset(min_prime, 0, sizeof(min_prime));
    for (int i=2;i*i<N;i++)
        if (min_prime[i]==0) 
            for (int j=i*i;j<N;j+=i) 
                { min_prime[j]=i; }
}


int  main(){
    freopen("sieve1.txt","w",stdout);
    sieve(N);
    for (auto x: min_prime) cout<<x<<" ";

}