# Gilded Rose Challenge

> by Fil Maj

# Overview of Approach

I spent ~40 minutes adding test cases to the scaffolding of the unit tests file
provided, just to cover existing functionality. I like to see passing tests
before I start meddling around in code, just to make sure I don't break anything
that already works. I like running tests and seeing "OK" at the end :)

I then spent a few minutes adding three test cases to cover the new
functionality required for conjured items (the last three cases in the unit test
file). Specifically covering that conjured items degrade by two every day, that
the quality degradation multiplier applies correctly to conjured items, and that
the quality floor of 0 also applies to conjured items. I ran the tests, and
surely enough, all three of these failed! That's ok: next up is to make them
pass.

I spent a several minutes adding a couple of sections to the existing code to get
the new conjured item tests to pass, and did so within the structure of the existing
cascade of `if`/`then`/`else`s in the original implementation. About an hour after
starting, I had a working solution passing all tests. Sweet...

But! I felt like the original implementation could be improved upon. I didn't
like the number of `if`s and how deeply nested they were. It was also a
code-smell for me to copy-paste the same two lines that increased conjured item
degradation in two sections of the code in my original implementation. This told
me I could refactor this a little bit.

After some thought, and re-reading the provided README a few times, I identified
a couple of repeating patterns we were modeling in this program:

- item `sell_in` always decrements (with the exception of Sulfuras)
- item `quality` always changes (with the exception of Sulfuras) - either up or
    down - and there exist several conditions in which the amount and direction
    of quality changing tweaks a little bit.

As such, I decided on modeling this behaviour by having a `quality_direction`
variable that represents a positive or negative multiplier applied to the
quality change, as well as a `quality_delta` variable that represents the amount
of quality change. In this way, in my opinion, we can more directly model the
constraints of the Gilded Rose system as laid out in the README by tweaking
these two values.

I spent the last 20 minutes or so writing up this overview, double-checking the
tests, adding a couple more boundary condition tests and double-checking the
comments in both the code and the tests.

# Further Considerations

One thing that dawned on me, right before my two hours were up, is that perhaps
conjured items could overlap with other item categories? For example, perhaps we
could have Conjured Aged Brie - would it then increase in quality at double the
rate of regular Aged Brie? Or Conjured Backstage Passes? If so, my solution
would not account for that but it wouldn't be much trouble to add this
functionality to the refactored code. Perhaps an exercise for the future!
