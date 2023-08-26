Though there are many solutions explained for this problem, including this also here.

`a`, `b`, `c` are given 3 numbers. We need to find any `x` such that `a^x \< b^x \< c^x` where `^` is the bitwise exclusive OR operation. 

| X | Y | X^Y |
|---|---|-----|
| 1 | 1 |  0  |
| 1 | 0 |  1  |
| 0 | 1 |  1  |
| 0 | 0 |  0  |

We'll restrict `x` to binary length of maximum of `a`, `b`, `c`, as after that the numbers `a^x`, `b^x`, `c^x` just keep repeating i.e if we have `1` in binary `x` before `k`, all of `a`, `b`, `c` will have `0` at equivalent digit and all of `a^x`, `b^x`, `c^x` will just be added with 2<sup>k-1</sup> and there won't be any change in their relative values comparatively as till `x` less than equal to 2<sup>k-1</sup>.

We obtain each binary digit of `a`,`b`,`c` at respective positions and store it in list `status` as tuples.

Since there are only 3 numbers, the posible combinations of their respective digits will be 2<sup>3</sup> = 8.

i.e `(bit_a, bit_b, bit_c)` can be equal to only `(1,1,1)`, `(0,0,0)`, `(1,1,0)`, `(0,0,1)`, `(1,0,1)`, `(0,1,0)`, `(1,0,0)`, `(0,0,1)`.

Now we formulate binary digits of `x` for each corresponding binary digits of `a`,`b`,`c` such that this will happen : `a^x \< b^x \< c^x`.

First, we observe that `(0,0,0)` and `(1,1,1)` doesn't affect relative value of `a^x`, `b^x`, `c^x`, hence we consider it as an insignificant tuple (bit values).

The most significant binary digit is the leftmost digit. If we use 1 for the left most binary digit, that is larger number than filling all the remaining digits as 1 (similar to how in decimal 100 is always greater than any two digit number).

So we need to make sure that `c^x` gets a lead in the leftmost digit. So the first significant bit values should not be `(1,0,1)` or `(0,1,0)`. If it happens to be, then any `x` is not posssible. 

E.g: If `x` takes 1 for digit `(1,0,1)`, then `b` we will get `(0,1,0)` (bits of `a^x`,`b^x`,`c^x`) which means that `b` will be the largest, and `c` cannot become larger than `b` any other way. If `x` takes 0 for digit `(1,0,1)` then `b` cannot become larger than `a`, so `(1,0,1)`. Similarly for `(0,1,0)`.

Now if the first significant tuple is `(1,1,0)` or `(0,0,1)`, then it should make `a^x` = `b^x` \< `c^x`, so we just need to find the next significant tuple to make `a^x` less than `b^x` which is one of `[(1,0,0),(0,1,1), (1,0,1), (0,1,0)]` meanwhile `[(1,1,0),(0,0,1),(1,1,1),(0,0,0)]` doesn't make a difference.

Or if the first significant tuple is `(1,0,0)` or `(0,1,1)`, then it should make `a^x` \< `b^x` = `c^x` so we just need to find the next significant tuple to make `b^x` less than  `c^x` which is one of `[(1,1,0),(0,0,1), (1,0,1), (0,1,0)]`, meanwhile `[(1,0,0),(0,1,1),(1,1,1),(0,0,0)]` doesn't make any difference.

