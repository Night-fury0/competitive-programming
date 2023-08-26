#include<iostream>
#include<algorithm>
#include<string>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;


int main(){

    int t;
    freopen("6_DIGITOP_input.txt","r",stdin);
    cin>>t;
    while(t--){
        int n;
        long long k;
        string temp;
        cin>>n>>k;
        string a,b;
        getline(cin, a);
        getline(cin, b);
        bool flag = true;
        for (int i=0;i<a.size();i++)
            if ((a[i] == ' ' && b[i] != ' ') || (a[i] != ' ' && b[i] == ' ')) {flag = false; break;}
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        long long positive = 0, negative = 0, result = 0;
        for (char i='0';i<='9';i++){
            int counta = upper_bound(a.begin(),a.end(),i) - lower_bound(a.begin(),a.end(),i);
            int countb = upper_bound(b.begin(),b.end(),i) - lower_bound(b.begin(),b.end(),i);
            if (counta > countb) positive += counta-countb;
            else if (counta<countb) negative += countb-counta;
        }
        if (negative > positive) 
            result = negative;
        else result = negative + (positive - negative);
        if (flag && result <= k) cout<<"YES"<<"\n";
        else cout<<"NO"<<"\n";
    }
    return 0;
}