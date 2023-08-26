#include<bits/stdc++.h>

#define ios_base :: sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){
    int t;
    // freopen("6_SLAYS_input.txt","r",stdin);
    cin>>t;
    while(t--){
        int n,q, temp;
        cin>>n>>q;
        vector<int> a;
        for (int i=0;i<n;i++){
            cin>>temp;
            a.push_back(temp);
        }


        // for a given index i, what is the maximum distance can be travelled with Si
        int max_dist_with_Si[n];
        int max = a[0];
        for (int i=n-1;i>=0;i--){
            if (a[i] == max){
                max_dist_with_Si[i-1] = i;
            }
        }

    }
}