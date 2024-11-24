#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		vector<int> a(n);
		for (int i=0; i<n; i++) cin>>a[i];
		vector<int> b(n);
		for (int i=0; i<n; i++) cin>>b[i];

		// making pair
		vector<int> s(n);
		bool possible = false;
		for (int i=0; i<n; i++){
			int A = max(a[i],b[i]);
			auto prev = max_element(a.begin(), a.begin()+i);
			auto post = max_element(a.begin()+i+1, a.end());
			auto j = max_element(a.begin(), a.end());
			if (*prev > *post) j = prev; else j = post;
			int index = j - a.begin();
			//cout<<"if index "<<i<<" is chosen by A, B will choose index "<<index<<endl;
			int B = max(a[index],b[index]);
			if (A>B){
				possible = true;
				break;
			}
		}
		if (possible) cout<<"Yes"<<endl; else cout<<"No"<<endl;
	}
	return 0;
}
