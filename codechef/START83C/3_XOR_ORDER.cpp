#include<bits/stdc++.h>

#define ios_base ::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;
int a,b,c;

int find_x(int x){
    cout<<x<<endl;
    if ((a^x < b^x) && (b^x < c^x)) return x;
    // else if ((a^x > c^x)|| (a^x > b^x)) return -1;
    // else if ((b^x > c^x)) return -1;
    else{
        x = x<<1;
        int no = find_x(x);
        if (no!= -1) return x;
        x = x+1;
        no = find_x(x);
        if (no!=-1) return x;
        return -1;
    }

}

int main(){
    a = 120;
    b = 122;
    c = 121;
    cout<<find_x(0);
    return 0;
}