A permututation of length `n` contains numbers 1 to `n` exactly once. We need to find a permutation `P`. When we give a permutation `Q`, `P` is rearranged according to `Q` to form `P'` (P bar). P'<sub>i</sub> is output if P'<sub>i</sub> is maximum in `P'` till `i`, which means the last element in array response of a query is largest element in the permutation `P`. 

To form the next query `Q` such that we continuously get the next largest numbers, we keep assigning the position of next largest element towards the end in descending order. So for each query `Q` we can get the next largest element in `P`.

Once we find the largest element in query, the next time, we look for last but one element in query response `a`. This is accomplished using `trials` variable as it is incremented for each query from value 0. So `-trial-1` gives the position in query response which is of our interest to find the next largest element.

Total no. of elements in `P` is `n`, in `n-1` queries we can find position of largest `n-1` numbers in `P`, the only number remaining will be `1`. 

Input of result `1` or `-1` is important, as in multiple test cases, the next `n` should not be confused with the `result`.


Example: <br>
1 <br>
7 <br>
&nbsp;&nbsp;&nbsp;&nbsp;? 1 2 3 4 5 6 7  <br>
3 1 2 7 <br>
&nbsp;&nbsp;&nbsp;&nbsp;? 1 2 3 4 5 6 7 <br>
3 1 2 7 <br>
&nbsp;&nbsp;&nbsp;&nbsp;? 1 3 4 5 6 2 7 <br>
4 1 2 6 7 <br>
&nbsp;&nbsp;&nbsp;&nbsp;? 1 4 5 6 3 2 7 <br>
6 1 2 4 5 6 7 <br>
&nbsp;&nbsp;&nbsp;&nbsp;? 1 4 5 6 3 2 7 <br>
6 1 2 4 5 6 7 <br>
&nbsp;&nbsp;&nbsp;&nbsp;? 1 5 4 6 3 2 7 <br>
7 1 2 3 4 5 6 7  <br>
&nbsp;&nbsp;&nbsp;&nbsp;! 1 6 5 3 2 4 7 <br>
1