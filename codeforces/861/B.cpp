#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){
    int t;
    // freopen("input.txt", "r", stdin);
    cin>>t;
    while (t--){
        int n,m;
        cin>>n>>m;
        int a[n][m];
        for(int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                cin>>a[i][j];
            
        long long sum = 0;
        for (int i=0;i<m;i++){
            int b[n];
            for (int j=0;j<n;j++)
                b[j] = *(a[j]+i);
            sort(b,b+n, greater<int>());
            long long positive = n-1;
            long long negative = 0;
            long long result = 0;
            for (int j=0;j<n;j++){
                result += positive * b[j] - negative * b[j];
                positive--;
                negative++;
            }
            sum += result;

        }
        cout<<sum<<"\n";
    }
    return 0;    

}