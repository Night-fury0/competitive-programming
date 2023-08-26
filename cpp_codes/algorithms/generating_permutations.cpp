#include<bits/stdc++.h>

#define ios_base :: sync_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

int n = 3;
vector <int> permutation;
bool chosen[3];


void generate_permutations(){
    if (permutation.size() == n) {
        for (auto x: permutation) cout<<x<<" ";
        cout<<"\n";
    }
    else{
        for (int i=1;i<=n;i++){
            if (chosen[i]) continue;
            chosen[i] = true;
            permutation.push_back(i);
            generate_permutations();
            chosen[i] = false;
            permutation.pop_back();
           
        }
    }
    
}


int main(){
    // method 1: using for loop over no. of elements in recursion`
    generate_permutations();
    cout<<endl;
    // method 2: using next_permutation()
    vector<int> permutation = {1,2,3};
    // next_permutation() returns 1 if next permutation exists else 0, the permutation is also changed; goes from ascending order to descending order of elements every time.
    do{
        for(auto x:permutation) cout<<x<<" "; cout<<"\n";
    }while(next_permutation(permutation.begin(), permutation.end()));
    


    return 0;
}