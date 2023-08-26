#include<bits/stdc++.h>

using namespace std;

int first_non_zero(vector<int> a){
    int i = 0, j = a.size(),non_zero = a.size();
    while(i+1!=j){
        int mid = (i+j)/2;
        if (a[mid] !=0 && mid<non_zero) { non_zero = mid; j=mid; }
        else if (non_zero != a.size()) j=mid;
        else{
            non_zero = i + first_non_zero((vector<int>){a.begin()+i,a.begin()+mid});
            if (non_zero == mid+1) non_zero = mid + 1 + first_non_zero((vector<int>){a.begin()+mid+1,a.begin()+j+1});

            break;
        }
    }
    return non_zero;

}


int main(){

    vector <int> a = {0,0,0,0,2,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0};
   cout<<first_non_zero(a);


}
