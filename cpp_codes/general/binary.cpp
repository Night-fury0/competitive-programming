#include<bits/stdc++.h>

#define ios_base ::synch_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

const int N = 8;

int main(){

    int a = 24;
    int k=2;
    bitset<N> b(a);
    cout<<"binary: "<<b<<endl;
    cout<<"No. of zeroes at beginning: "<<__builtin_clz(a)<<"\n";
    cout<<"No. of zeroes at end: "<<__builtin_ctz(a)<<"\n";
    cout<<"No. of ones: "<<__builtin_popcount(a)<<"\n";
    cout<<"No. of parity: "<<__builtin_parity(a)<<"\n";

    cout<<"Changing kth bit to 1: "<< (a|(1<<k))<<"\n";
    cout<<"Changing kth bit to 0: "<< (a&~(1<<k))<<"\n";
    cout<<"Invert kth bit: "<< (a^(1<<k))<<"\n";
    cout<<"Sets all 1 bits to 0 except last one: "<< (a&(-a))<<"\n";
    cout<<"Inverts all bits after last 1 bit: "<< (a|(a-1))<<"\n";
    cout<<"If sums of powers of 2: "<< ((a&(a-1))==0)<<"\n";


    // subsets of a set x
    int b1 = 0;
    int x = 14;
    cout<<"set "<<bitset<N> (x)<<"\n";
    int count = 0;
    do{
        count ++;
        cout<<bitset<N> (b1)<<"\n";
    }while(b1=(b1-x)&x);
    cout<<"no of subsets: "<<count<<endl;

    

    return 0;
}