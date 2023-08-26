// # zeroes - no. of zeroes; ones - no. of ones
// # remove leading zeroes
// # ( 1 + zeroes>0?zeroes:1 ) or (ones)
#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

const int N = 100000;

int main(){
    int t;
    freopen("input.txt","r",stdin);
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string a;
        cin>>a;
        bitset<N> b(a);
        int ones = b.count();
        int zeros = b._Find_first() + 1 - ones;
        int p_zeros = 0, p_ones = 0, s_zeros = zeros, s_ones = ones;
        int min_ones = ones, pos = -1;
        for (int i=0;i<=b._Find_first();i++){
            if (i+1<N && 1 + (s_zeros>0?s_zeros:1) > s_ones){
                int t = p_ones + (a[i+1]==1?0:1) + (s_zeros>0?s_zeros:1);
                if (t<min_ones){
                    min_ones = t;
                    pos = i;
                }
            }
            if (b[i]==0){
                p_zeros+=1;
                s_zeros-=1;
            }
            else{
                p_ones+=1;
                s_ones-=1;
            }
        }
        if  (pos == -1) cout<<b<<"\n"<<0<<"\n";
        else{
            // same till pos, pos+1 to be 1 and rest 0
            b[pos+1] = 1;
            

        }
    }
}

