
// Problem is https://www.codechef.com/problems/MODE
// This solution explained at https://www.codechef.com/viewsolution/93477822

#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

const int INF = 1000000;

int n;


int main(){
    int t;
    // freopen("input.txt", "r", stdin);
    cin>>t;
    while(t--){
        vector <int> freq;
        int temp;
        cin>>n;
        vector <int> a;
        for (int i=0;i<n;i++){
            cin>>temp;
            a.push_back(temp);
        }
        sort(a.begin(),a.end());

        int i=0;
        while (i<n) {
            int no = upper_bound(a.begin(),a.end(), a[i]) - lower_bound(a.begin(),a.end(), a[i]);
            freq.push_back(no);
            i += no;
        }

        sort(freq.begin(), freq.end(), greater<int>());
        int no_freq = freq.size();

        int mf = freq[0];
        int nm = count(freq.begin(), freq.end(), mf);

        vector<int> freq_sum;
        int sum = 0;
        for (auto x:freq){
            sum += x;
            freq_sum.push_back(sum);
        }
        int result_arr[n];
        fill(result_arr, result_arr + n, -1);
        for(int i=1;i<=n/2;i++)
            if (i == nm) result_arr[i-1] = 0;
            else if (i < nm) result_arr[i-1] = min(i, nm - i);
            else {
                int result = INF;
                for (int k=min((int)(n/i), mf); k>=2; k--){
                    int positive = 0;
                    int negative = 0;
                    int index = upper_bound(freq.begin(), freq.end(), k, greater<int>()) - freq.begin();
                    if (index >= i){
                        positive = freq_sum[i-1] - i*k;
                        negative = 0;
                        if (index > i and freq[i]>=k) 
                            positive += (freq_sum[index-1] - freq_sum[i-1]) - (index-i)*(k-1);
                        
                    }
                    else{ // i>index
                        positive = freq_sum[index-1] - index * k;
                        if (i <= no_freq) negative = (i-index) * k - (freq_sum[i-1] - freq_sum[index-1]);
                        else negative = (i-index) * k - (freq_sum[no_freq-1] - freq_sum[index-1]);
                    }
                    if (positive >= negative) result = min(result, positive);
                    else result = min(result, positive + (negative - positive));
                }
                if (result == INF) result = -1;
                result_arr[i-1] = result;
            }
        result_arr[n-1] = n - no_freq;
        
        for(auto x: result_arr)
            cout<<x<<" ";
        cout<<"\n";

    }
    return 0;
}