#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int max_string(string s, int n, char last){
    int count = 0;
    if (last == '1') count++;
    for (int i=1;i<n;i++){
        char last1 = s[i];
        if (s[i-1] !=last) {s[i] = '1'; count++;} else s[i] = '0';
        last = last1;
    }
    return count;
}
int main(){

    int t;
    // freopen("4_input.txt","r",stdin);
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        cout<<max(max_string(s,n,'0'), max_string(s,n,'1'))<<"\n";


    }
    return 0;
}