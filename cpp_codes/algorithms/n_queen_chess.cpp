#include<bits/stdc++.h>

#define ios_base ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

const int n = 16 ;
int pos = 0;
bool board[n][n];

bool col[n];
bool diag1[n+n-1];
bool diag2[n+n-1];


void possible_moves(int j){
    if (j==n) pos++;
    else{
        for(int i=0;i<n;i++){
            if (col[i] || diag1[i+j] || diag2[i-j+n-1]) continue;
            col[i] = diag1[i+j] = diag2[i-j+n-1] = true;
            possible_moves(j+1);
            col[i] = diag1[i+j] = diag2[i-j+n-1] = false;

        }
    }
}


int main(){
    possible_moves(0);
    cout<<pos;
    return 0;
}
