#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

const int N = 1000001;
int first_pf[N];

int main(){
    int t;
    memset(first_pf, 0, sizeof(first_pf));
    // freopen("input.txt","r",stdin);
    for (int i=2;i*i<N;i++)
        if (first_pf[i]==0) 
            for (int j=i*i;j<N;j+=i) 
                { first_pf[j]=i; }
    
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        unordered_map <int,set<int>> pf_to_a;
        unordered_map <int,int> count;
        vector <int> a(n);
    	// organize numbers in sets corresponding to each prime factors
        for (int i=0;i<n;i++){
            int y;
            cin>>y;
            a[i] = y;
	        count[y]++;
            int temp = y;
            while(temp > 1){
                int j = first_pf[temp];
                if (j==0) j = temp;
                while (temp%j==0) temp/=j;
                pf_to_a[j].insert(y); 
            }   
        }
        sort(a.begin(), a.end());
        int q, no;
        cin>>q;
        while(q--){
            cin>>no;
            int to_remove = N+1; 
            while(count[*a.begin()] == 0) 
                a.erase(a.begin(),upper_bound(a.begin(),a.end(),*a.begin()));

            if (no==1)  to_remove = *a.begin();
            else{
                while(no>1){
                    int j = first_pf[no];
                    if (j==0) j = no;
                    while (no%j==0) no/=j;
                    while (!pf_to_a[j].empty() && count[*pf_to_a[j].begin()] == 0) 
                        pf_to_a[j].erase(pf_to_a[j].begin());
                    if (!pf_to_a[j].empty()) 
                        to_remove = min(to_remove, *pf_to_a[j].begin());
                }  
            }	

            if (to_remove == N+1)   to_remove = *a.begin();
            
            cout<<to_remove<<" ";
            count[to_remove]--;
            
        }
	cout<<"\n";
	}
}

