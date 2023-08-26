#include<bits/stdc++.h>

#define ios_base ::synch_with_stdio(false); cin.tie(0); cout.tie(0);

using namespace std;

long long MOD = 1000000007;

int main(){

    // deque to both push and pop in front and back, inefficient compared to vector, so use if specific need is there.
    deque <int> a (5,0);
    a.push_front(5);
    a.pop_front();
    for (auto x: a) cout<<x<<" ";
    cout<<"\n";

    // stack
    stack<int> s;
    s.push(4);
    s.push(5);
    s.pop();
    s.push(6);
    while(s.size() > 0){
        cout<<s.top()<<" ";
        s.pop();
    }
    cout<<"\n";

    // queue
    queue<int> q;
    q.push(2);
    q.push(5);
    q.pop();
    // q.back() is also available
    while(q.size()>0){
        cout<<q.front()<<" ";
        q.pop();
    }




    
}
