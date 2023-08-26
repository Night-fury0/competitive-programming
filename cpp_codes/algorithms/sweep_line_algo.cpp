#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0)l

using namespace std;

int main(){
    int n, temp;
    freopen("sweep_line_algo_input.txt", "r", stdin);
    cin>>n;
    vector<int> entry, exit;
    for (int i=0;i<n;i++){
        cin>>temp;
        entry.push_back(temp);
        cin>>temp;
        exit.push_back(temp);
    }
    sort(entry.begin(), entry.end());
    sort(exit.begin(),exit.end());
    // cout<<"entry timings: ";
    // for (auto x: entry) cout<<x<<" ";
    // cout<<"\nexit timings: ";
    // for (auto x: exit) cout<<x<<" ";
    // cout<<"\n";
    int count=0;
    int count_max = 0;
    while (!entry.empty() && !exit.empty())
        if (entry[0] < exit[0]){
            count ++;
            if (count > count_max) count_max = count;
            entry.erase(entry.begin());
        }
        else{
            count--;
            exit.erase(exit.begin());
        }
    if (entry.size()) {
        count += entry.size();
        if (count_max < count){ count_max = count; }
        }

    cout<<"max no of people at same time in restaurant: "<<count_max;
    
}
