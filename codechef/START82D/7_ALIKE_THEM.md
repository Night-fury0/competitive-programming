Given an array `A` of size `N`. `A'` is formed by shifting elements according to indexes stored in array `P`.
We need to find the no. of possible ways in which a given integer `M` can fill the zeroes in `A` such that `A'` has all elements same.

Each zero can take `M` values (1 to `M`). 

First we count the no. of zeroes in `A` using `no_zero = a.count(0)`.

Let `count` be the no. of **distinct** zeroes in `A'`.

There are four cases:
1. `A'` has more than one distinct non-zero element, in which case answer is zero.
2. No zeroes in `A'`, in which case, answer is M<sup>no_zero</sup> (if `A'` has more than one distinct non-zero element).
3. There are zeroes in `A'`, but there is also a non-zero element in `A'`. All zeroes in `A'`  can take only one value (the value of the non-zero element in `A'`) and the rest can take any value independently i.e M<sup>no_zero - count</sup>
4. There are only zeroes in `A'`. The no. of zeroes in `A'` will all have to take a single value (can be any of `M` values). The rest can take any values independently i.e M<sup>no_zero - count + 1</sup>


Now we need to find how many **distinct** zeroes appear in `A'`. To know that we form `A'` from `A` using statement. To avoid declaring a new array, we use same `A`.

`A[i] = A[P[i]-1]` 

Now that we have an element in `A'`, we see if its zero, but sometimes the zero can be coming from same position of original `A`. To count only **distict** zeroes we use condition `if P[i]-1 >= i:` (If the 0 was from an already set element, it is a repetition, hence we choose only those zeroes which does not come from previously set positions)

If there is more than one **distinct** non-zero element in `A'` then `A'` can never have all same elements. To know this we have flag `non_zero_flag` (to say if there is a non-zero element in `A'`) and `non_zero` (the non-zero element in `A'`)

In the same loop that we used to find `A'`'s elements, if it's the first non-zero element, we assign to `non_zero` and make `non_zero_flag = True`.
So if there is one more non-zero element identified in `A'`, it should be equal to the stored element in `non_zero`, if not our answer will be 0 (we use a variable `flag` to check this case).

We use the following statement to find the power of `M` in cases (2),(3),(4):

`power = no_zero - (count if non_zero_flag else count-1)`

Finally, to calculate power we avoid using `math.pow()` as the number could be very large and modulus operation can become heavy.

Since `X*Y mod Z = (X mod Z)*(Y mod Z)` we use a `while` loop to find the result.



 


