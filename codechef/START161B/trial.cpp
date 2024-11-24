#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){
	vector<int> a  = {1,2,3,4,5,6};
	auto prev = max_element(a.begin(), a.begin()+2);
	auto post = min_element(a.begin()+2, a.end());
	cout<<*prev;
	cout<<*post;

}
