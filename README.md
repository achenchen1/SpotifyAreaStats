# General Idea
- Wouldn't it be cool if you could tell what your friends or neighbourhood was listening to?

## Idea scratch space:

I'd like to ideally create an app or a website (if only there was portmanteau of these two words) that allowed you to see what a particular country, state/province, county, city, neighborhood, etc. was listening to.

**Two things are immediately needed:**

1. A way to get user data from Spotify, and possibly other music services. (See: `prototype`)
2. A way to get user location
    * Android and Apple apps have libraries for this; I've used Android libraries for this and I've seen iOS apps do the same. (Obviously.)

Beyond that, a criteria has to be defined for the following:

### What categories of "music" should be displayed?
Artists? Albums? Songs? Artwork for these *may* be retrievable from [last.fm](last.fm).

### What's the criteria for ranking popularity?
Total listeners/listens is problematic - someone like Taylor Swift is going to pop up in almost every neighbourhood.

Is it worth evaluating popularity relative to other areas?

Is it worth weighting the value of a "play" relative to how many total plays a user has? (Perhaps using a logarithmic function.) 

#### Logarithm example exercise
Let's denote the number that we'll use to rank all of these artists as "points".
Let our weighting function be `ln(x+1)`, as a notion of how much "weight" their plays carry.

* If *Alice* listens to 100 songs in a month, then she gets a weighting of `ln(100+1)` which is approximately 4.61512052.
    * If 43/100 of those songs are from John Mayer, 27/100 of those songs are from Madison Cunningham, 19/100 of those songs are from Ed Sheeran, and the remaining 11/100 songs are from Jack Johnson, then John Mayer gets `43/100*4.61512052 = 1.98450182` points, Madison Cunningham gets 1.24608254 points, Ed Sheeran gets 0.876872899 points, and Jack Johnson gets 0.507663257 points.
* If *Bob* listens to 10 songs in a month, then he gets a weighting of `ln(10+1)` which is approximately 2.39789527.
    * Let's say 5 of those are Mac Miller songs, and 5 of those are songs from A Tribe Called Quest. Both of these artists get 1.19894763 points.

Here's the artists' points tabulated:

| Artist                    | Points        | Normalized    |
|---------------------------|---------------|---------------|
| John Mayer                | 1.98450182    | 3.909090909   |
| Madison Cunningham        | 1.24608254    | 2.454545455   |
| **Mac Miller**            | 1.19894763    | 2.361698666   |
| **A Tribe Called Quest**  | 1.19894763    | 2.361698666   |
| Ed Sheeran                | 0.876872899   | 1.727272727   |
| Jack Johnson              | 0.507663257   | 1             |

There's an argument to be made that Bob's artists' plays are counting for too much (which I agree with). Hence, a better "reward" function will need to be designed.

