#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

bool solve(vector<int>a, int k, int n, int t){
    int no_jobs = 0;
    for (int i=0;i<n;i++) 
        no_jobs += t/a[i];
    if (no_jobs > k)
        return true;
    return false;
}

int main(){
    int n, k, temp;
    // n- no of machines
    // k- no of jobs to complete
    cin>>n>>k;

    // a- time taken for each machine to complete a job
    vector<int> a;
    for(int i=0;i<n;i++){
        cin>>temp;
        a.push_back(temp);
    }
    // find min time to complete k jobs with n machines
    sort(a.begin(), a.end());
    int max_time = k*a[0];
    // given a time t, we can say the max no of jobs that can be completed by all machines together

    int b = max_time, d=b/2;
    while(d>=1){
        if (solve(a,k,n,b)){
            b-=d; 
            d/=2;
        }
        else{
            b+=d;
            d/=2;
        }
    }
    cout<<"min time needed to complete k jobs with given n machines: "<<b<<"\n";

}