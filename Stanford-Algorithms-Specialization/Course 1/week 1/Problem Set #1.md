1. 3-way-Merge Sort : Suppose that instead of dividing in half at each step of Merge Sort, you divide into thirds, sort each third, and finally combine all of them using a three-way merge subroutine. What is the overall asymptotic running time of this algorithm? (Hint: Note that the merge step can still be implemented in `O(n)` time.)

   - [ ] n(log(n))<sup>2</sup>
   - [x] n(log(n))
   - [ ] n<sup>2</sup>log(n)
   - [ ] n

2. You are given functions `f` and `g` such that `f(n)=O(g(n))`. Is f(n)*log<sub>2</sub>(f(n)<sup>c</sup>) = O(g(n)*log<sub>2</sub>(g(n)))(Here `c` is some positive constant.) You should assume that `f` and `g` are nondecreasing and always bigger than 1.

   - [ ] False
   - [x] True
   - [ ] Sometimes yes, sometimes no, depending on the functions `f` and `g`
   - [ ] Sometimes yes, sometimes no, depending on the constant `c`

3. Assume again two (positive) nondecreasing functions `f` and `g` such that `f(n)=O(g(n))`. Is 2<sup>f(n)</sup>=O(2<sup>g(n)</sup>) (Multiple answers may be correct, you should check all of those that apply.)

   - [x] Yes if `f(n)≤g(n)` for all sufficiently large `n`
   - [x] Sometimes yes, sometimes no (depending on `f` and `g`)
   - [ ] Never
   - [ ] Always

4. k-way-Merge Sort. Suppose you are given `k` sorted arrays, each with `n` elements, and you want to combine them into a single array of `kn` elements. Consider the following approach. Using the merge subroutine taught in lecture, you merge the first 2 arrays, then merge the 3<sup>rd</sup> given array with this merged version of the first two arrays, then merge the 4<sup>th</sup> given array with the merged version of the first three arrays, and so on until you merge in the final (k<sup>th</sup>) input array. What is the running time taken by this successive merging algorithm, as a function of `k` and `n`? (Optional: can you think of a faster way to do the k-way merge procedure ?)

   - [ ] θ(nk)
   - [ ] θ(n<sup>2</sup>k)
   - [ ] θ(nlog(k))
   - [x] θ(nk<sup>2</sup>)

5. Arrange the following functions in increasing order of growth rate (with `g(n)`) following `f(n)` in your list if and only if `f(n)=O(g(n))`.

   a)2<sup>log(n)</sup>  
   b)2<sup>2log(n)</sup>  
   c)n<sup>5/2</sup>  
   d)2<sup>n<sup>2</sup></sup>  
   e)n<sup>2 log(n)</sup>

   Answer:

   ```
   aecbd
   ```
