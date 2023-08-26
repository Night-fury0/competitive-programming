From the Problem Statement, `A` wants to maximize its score while `B` wants to minimize `A`'s score.

Finding the most optimal move of `A` or `B` at a particular moment (& position) seems to be quite dynamic, so move of A will be related (or dependent) on what move`B` makes at each stage. (i.e `A` cannot simply go for the vertex (or city) with highest population in immediate move or choose the path which gives maximum sum of population at the end of some no. of moves).

Our objective is to find the score if both `A` and `B` play **optimally**.

The score can be defined as, <br>
`result = int(P[a-1] + pop_a > P[b-1] + pop_b)` where, <br>
`pop_a` is sum of populations of cities travelled by A. <br>
`pop_a` is sum of populations of cities travelled by B. <br>
`P[a-1]` is population of current city in which A is in. <br>
`P[b-1]` is population of current city in which B is in. <br>


All possible moves from a vertex (or city) `v` is stored in set `E[v]` where `E` is declared as a dictionary.

At any stage, `A` or `B` can move to a particular vertex (or city) if it was not in that vertex before, to keep track of it we have two lists `exclude_a` & `exclude_b` .

If `A` is in vertex `a` at any time, it can move only to vertices which are in `E[a]` that are not in `exclude_a`, this is represented as `E[a].difference(exclude_a)`, similarly `B` can move only to vertices in `E[b].difference(exclude_b)`.

Now at any stage if `A` or `B` cannot move to any vertex, the game will no longer go ahead, because score can be generated only if both `A` and `B` can make a move.

For a given move of `A` at any stage, `B` will make a move that causes the score to be minimum.

So lets take `A` moves to vertex `ai`, then the move `B` will make, will lead to minimum possible score. So if `B` moves to `bi` in `E[b].difference(exclude_b)`, the minimum score can be written as:

```
q_min = 10000   # any large number
for bi in E[b].difference(exclude_b):
    q_min = min(q_min, result + optimal_score(ai, bi, pop_a + P[a-1], pop_b + P[b-1], exclude_a[:] + [a], exclude_b[:] + [b]))
```

Here while passing the list through
So this `q_min` gives the most optimal move for `B` if `A` moves to `ai`. Now out of all possible moves that `A` can do for `ai` in `E[a].difference(exclude_a)`, we need to find which score is maximum, so we iterate through `ai` and find the maximum `q_min`.  



