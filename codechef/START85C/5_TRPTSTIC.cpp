#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;


int main(){

    int t;
    // freopen("input.txt","r",stdin);
    cin>>t;
    while(t--){
        int n,m;
        long long k, total_sum = 0;;
        cin>>n>>m>>k;
        int a[n][m];
        long long prefix_sum[n][m];
        bool zero_possible = false;
        for (int i=0;i<n;i++){
           long long row_sum = 0;
            for (int j=0;j<m;j++){
                cin>>a[i][j];
                if (a[i][j] >= k+1) zero_possible = true;
                row_sum += a[i][j];
                prefix_sum[i][j] = row_sum;
            }
            total_sum += row_sum;
        }
        for (int j=0;j<m;j++){
            long long col_sum = 0;
            for (int i=0;i<n;i++){
                col_sum += prefix_sum[i][j];
                prefix_sum[i][j] = col_sum;
            }
        }
        if (k+1 > total_sum) cout<<-1<<"\n";
        else if (zero_possible) cout<<0<<"\n";
        else{
            int result = max(n,m);
            for (int i=0;i<n;i++)
                for (int j=0;j<m;j++)
                    if (a[i][j]!=0){
                        result = min(result, max(max(max(i,n-i),j),m-j));
                        int x=0,y=result;
                        while (x+1!=y){
                            int d = (x+y)/2;
                            // calculate capacity for mentor at (i,j) with farthest distance d here
                            int up = i-d-1, down = i+d, left = j-d-1, right = j+d;
                            if (right>=m) right = m-1;
                            if (down>=n) down = n-1;
                            long long down_right = prefix_sum[down][right], up_right=0, up_left=0, down_left=0;
                            if (up>=0){ up_right = prefix_sum[up][right]; if (left>=0) up_left = prefix_sum[up][left];}
                            if (left>=0) { down_left = prefix_sum[down][left]; }
                            long long capacity = down_right - up_right - down_left + up_left;
                            // cout<<"capacity for ("<<i<<","<<j<<") for distance "<<d<<" is : "<<capacity<<"\n";
                            if (capacity >= k+1) { result = min(result,d); y = d;}
                            else x = d;
                        }
                    }
            cout<<result<<"\n";
        }

    }

}


