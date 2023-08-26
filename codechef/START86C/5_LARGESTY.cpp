#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

const int N = 31;

int main(){
    int t;
    // freopen("input.txt","r",stdin);
    cin>>t;
    while(t--){
        int n, x, temp;
        cin>>n>>x;
        set<int> a;

        for (int i=0;i<n;i++){
            cin>>temp;
            a.insert(temp);
        }
        // find minimum bit that can show difference in 
        int min_bit = 31;
        int max_bit = 0;
        int no = *a.begin();
        int c = 0;
        for (auto i: a)
            for (auto j:a)
                if (i!=j)  { c = c|(i^j); }
        bitset<N> X = x;
        bitset<N> C = c;
        // cout<<"x: "<<x<<" leading zeroes: "<<__builtin_clz(x)<<" # ";
        // cout<<"c: "<<c<<" leading zeroes: "<<__builtin_clz(c)<<"\n";
        if (__builtin_clz(x) > __builtin_clz(c)) cout<<x<<"\n";
        else{
            int i;
            int beg = 32-__builtin_clz(x);
            int count=0;
            int pos = -1;
            // cout<<"checking till (excluding) "<<beg<<"c is "<<C<<"\n";
            for (i=0;i<beg;i++)
                if (C[i] == 1)
                    if (X[i] != 0) {
                        if (pos == -1)  pos = i;
                    }
                    else count++;
            if (count>0) cout<<x<<"\n";
            else{
                // cout<<"pos: "<<pos<<"\n";
                X[pos] = 0;
                while(pos>0) X[--pos] = 1;
                cout<<(int)X.to_ulong()<<"\n";
            }
        }

    }
}