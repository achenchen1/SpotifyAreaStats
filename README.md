# General Idea

- Wouldn't it be cool if you could tell what your friends or neighbourhood was listening to?

## Idea scratch space

I'd like to ideally create an app or a website (if only there was portmanteau of these two words) that allowed you to see what a particular country, state/province, county, city, neighborhood, etc. was listening to.

**Two things are immediately needed:**

1. A way to get user data from Spotify, and possibly other music services. (See: `prototype`)
2. A way to get user location
    - Android and Apple apps have libraries for this; I've used Android libraries for this and I've seen iOS apps do the same. (Obviously.)

Beyond that, a criteria has to be defined for the following:

### What categories of "music" should be displayed?

Artists? Albums? Songs? Artwork for these *may* be retrievable from [last.fm](last.fm).

### What's the criteria for ranking popularity?

Total listeners/listens is problematic - someone like Taylor Swift is going to pop up in almost every neighbourhood.

Is it worth evaluating popularity relative to other areas?

Is it worth weighting the value of a "play" relative to how many total plays a user has? (Perhaps using a logarithmic function.)

A good function should factor in the relative frequency of an artist for a given user, whilst not overly punishing a frequent listener.

