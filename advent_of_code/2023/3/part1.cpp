#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	int rows = 140;
	int cols = 140; 
	vector<string> a(rows);
	long long total = 0;
	for (int i=0; i<rows; i++)
		cin>>a[i];
	for (int i=0; i<a.size();i++){
		int j = 0;
		int no = 0;
		bool neighbour = false;
		while (j < a[i].size()){
			if (isdigit(a[i][j])){
			 	no = no*10 + (a[i][j] - 48);
				if ( i-1 >= 0 && !isdigit(a[i-1][j]) && a[i-1][j]!='.' ) neighbour = true;
				if ( i+1 <a.size() && !isdigit(a[i+1][j]) && a[i+1][j]!='.' ) neighbour = true;
				if ( j-1 >=0 && !isdigit(a[i][j-1]) && a[i][j-1]!='.' ) neighbour = true;
				if ( j+1 <a[i].size() && !isdigit(a[i][j+1]) && a[i][j+1]!='.' ) neighbour = true;
				if ( i-1 >= 0 && j-1>=0 && !isdigit(a[i-1][j-1]) && a[i-1][j-1]!='.' ) neighbour = true;
				if ( i+1 <a.size() && j+1<a[i].size() && !isdigit(a[i+1][j+1]) && a[i+1][j+1]!='.' ) neighbour = true;
				if ( i-1 >= 0 && j+1<a[i].size() && !isdigit(a[i-1][j+1]) && a[i-1][j+1]!='.' ) neighbour = true;
				if ( i+1 < a.size() && j-1>=0 && !isdigit(a[i+1][j-1]) && a[i+1][j-1]!='.' ) neighbour = true;
			}
			else{
				if (no > 0 && neighbour){
					total += no;
					cout<<no<<" ";
				}
				no = 0;
				neighbour = false;
			}
			j++;
		}
		cout<<endl;
	}
	cout<<total;
}


