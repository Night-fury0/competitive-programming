#include<bits/stdc++.h>

#define ios_base ::synch_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;



string solve(string s, int p, int q){
    int pos = 0;
    int neg = 0;
    for (int i=0; i<s.size(); i++)
        if (s[i] == 'a') continue;
        else{
            int pos1 = 123 - s[i];
            int neg1 = s[i] - 97;
            // if ((pos + pos1 <= p) && (neg + neg1 <= q) && (i+1 < s.size())){
                // s[i] = 'a';
                // s = s.substr(0,i+1) + min(solve(s.substr(i+1), p-pos-pos1, q-neg), solve(s.substr(i+1), p-pos, q-neg-neg1));
                // break;
            // }
            if (pos + pos1 <= p){
                s[i] = 'a';
                pos += pos1;
            }
            else if ((neg + neg1 <= q)){
                s[i] = 'a';
                neg += neg1;
            }
            else if (neg < q){
                s[i] = s[i] - (q-neg);
                neg = q;
            }
            else if (pos < p) continue;
            else break;
        }
    return s;
}


int main(){

    int t;
    // freopen("5_ROTMIN_input.txt", "r", stdin);
    cin>>t;
    while(t--){
        int n, p, q;
        cin>>n>>p>>q;
        string s;
        cin>>s;
        // cout<<s<<endl;
        int positive[n], negative[n];
        for (int i=0;i<n;i++){
            // if (s[i] == 'a') positive[i] = 0;
            positive[i] = 123 - s[i];
            negative[i] = s[i] - 97;
        }
        int beg = -1;
        int end = n;

        int pleft = p;
        int qleft = q;
        int possible = 0;

        while(beg+1!=end){
            // cout<<"begin "<<beg<<" end "<<end<<"\n";
            int mid = (beg + end)/2;
            vector<int> positive1 = vector<int>(positive, positive + mid+1);
            sort(positive1.begin(), positive1.end());
            vector<int> negative1 = vector<int>(negative, negative + mid+1);
            sort(negative1.begin(), negative1.end());
            int pi = 0;
            int qi = 0;
            int pos = 0;
            int neg = 0;
            // cout<<"positive1: ";
            // for(auto x: positive1) cout<<x<<" ";
            // cout<<"\nnegative1: ";
            // for(auto x: negative1) cout<<x<<" ";
            // cout<<"\n";
            while (pos<=p && neg<=q && pi+qi<mid+1){
                // cout<<"pi: "<<pi<<" qi: "<<qi<<endl;
                if (pos + positive1[pi] <= p && neg + negative1[qi] <= q){
                    if (positive1[pi] <= negative1[qi]) pos += positive1[pi++];
                    else neg += negative1[qi++];
                }
                else if (pos + positive1[pi]<=p) pos += positive1[pi++];
                else if (neg + negative1[qi]<=q) neg += negative1[qi++];
                else break;
            }
            if (pi + qi < mid + 1)   end = mid;
            else{
                beg = mid;
                possible = mid+1;
                pleft = p-pos;
                qleft = q-neg;
            }
        }
        // cout<<"'a' is possible only till position "<<possible<<" after that only p_left: "<<pleft<<" qleft: "<<qleft<<"\n";
        
        cout<<string(possible, 'a') + solve(s.substr(possible), pleft, qleft)<<"\n";
    }
    return 0;
}