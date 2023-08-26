According to problem statement, we have array `a` (of size `n`) given. We need to find no. of replacements to do in array `a` to get `i` no. of modes of for each `i` in `[1,N]`.

A mode is the most frequent occuring element. If an array is said to have 3 modes of mode frequency 2, it will be like `[1,1,2,2,3,3,4,5]` where `1`,`2`,`3` are the 3 modes and they occur 2 times each.

Lets take an example to understand. For eg. in an array of `a = [1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,7], n=16`. The frequency list will be `freq=[3,3,3,2,2,2,1]`, no. of modes `nm=3` and mode frequency `mf= 3`.

For `i=1`, we need to make 1 mode. it can be achieved by replacing any element in array `a` to one of 3 modes to make its frequency 4 i.e `freq` can be `[4,3,3,2,2,2]`, hence minimum no. of replacements is `1`.

For `i=2`, we need to make 2 modes. We already have 3 modes, we can remove (replace with a random no.) one element from one of the mode, to make the array have 2 modes. i.e `freq` can be `[3,3,2,2,2]`. hence `1`.

For `i=3`, we already have 3 modes, so `0`. 

For `i` less than no. of modes in given array (`nm`) we observe that, `i` modes can be formed by removing one element from each mode to get `i` or add one element to existing modes to get `i`. So we can calculate no. of modes for `i` less than `nm` by `min(i,nm-i)`.

For `i==nm`, its `0`. So we are only left with cases were `i` is greater than `nm`.

For `i=4`, `mf` can be maximum `n/i` i.e 4 in this case. And `mf` cannot be less than `2` as it will become `n` modes case, which is our last case. possible mode frequencies are 4,3,2. 

|freq   | 3 | 3 | 3 | 2 | 2 | 2 | 1 |no.|
|-------|---|---|---|---|---|---|---|---|
|i=4,k=4| +1| +1| +1| +2| - | - | - |=5 |
|i=4,k=3| 0 | 0 | 0 | +1| - | - | - |=1 |
|i=4,k=2| -1| -1| -1| 0 |-1*|-1*| - |=5 |
* not doing these can cause no. of modes to be more than 4 for `i=4, k=2`.
For `i=5`, we can have mode frequencies 3,2, as 16/5 ≈ 3.
|i=5,k=3| 0 | 0 | 0 | +1| +1| - | - |=2 |
|i=5,k=2| -1| -1| -1| 0 | 0 |-1*| - |=4 |
For `i=6`, mf of only 2 is possible, as 16/2 ≈ 2.
|i=6,k=2| -1| -1| -1| 0 | 0 | 0 | - |=3 |

For `i` greater than `n/2` till `i=n-1`, we cannot form such no. of modes. For `i=n`, we need to make all elements distinct, so keeping 1 in each frequency, we need to change everything else, so `n-len(freq)`.

One important case to handle is when `i` fall above where `k` might fit in `freq` (which we call as `index` in line 56). i.e

|freq   | 5 | 4 | 3 | 2 | 1 |no.|
|i=5,k=3| -2| -1| 0 | +1| +2|=3 |
Here we need to remove 3 elements and add 3 elements, the removed element can be modified and added needed addition, hence only 3 moves are needed, this can be written as: 
`positive + (negative - positive)`, 
where,
 `postitive` is sum of quantities greater than `k`
 `negative` is sum of quantities less than `k`
If `positive` is greater than `negative`, we only have `positive` changes to be made.

 We use array `freq_sum` to store sum of to `i` in descending (`freq`).