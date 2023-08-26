#include<bits/stdc++.h>

using namespace std;

int main(){

    vector<int> a = {3,5,7,14,18,20,20};
    auto lw = lower_bound(a.begin(), a.end(),7);
    cout<<upper_bound(a.begin(),a.end(),25)-lw;
}

7
18 20 7 3 14 20 5


8
1 5 1 13 20 7 18 5