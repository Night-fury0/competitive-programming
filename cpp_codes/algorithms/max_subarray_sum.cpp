#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){

    int a[] = {-1,2,4,-3,5,2,-5,2};
    int sum = 0, max=0, mina=0, minb=0;
    int start = 0, end = 0, start1=0;
    for (int i=0;i<sizeof(a)/sizeof(a[0]);i++){
        sum += a[i];
        if (sum >= max){
            max = sum;
            start = start1;
            end = i;
            minb = mina;
        }
        if (sum < 0 && sum<mina) {mina = sum; start1 = i+1;}
    }
    cout<<"maximum subarray sum: "<<max-minb<<"\n";
    cout<<"from "<<start<<" to "<<end;

}
