# Hash Tables
Hash tables are what are internally used to implement hash maps, or in
Python, dictionaries. They map keys to values, allowing O(1) lookup time.

## Implementation
A simple implementation consists of an array of linked lists and a hash
function. The hash function allows us to turn an object into an integer,
which we then place in the right "bucket" of the hash table.

When we want to insert a key and value, we first:

1. Compute the key's hash code. 
2. Map the hash code to an index of the array using modular arithmetic.
3. Append the value to the linked list at that index.

Note: The reason we need to use linked lists is to deal with collisions.
Two keys can hash to the same number, which means they'll be stored in the
same "bucket".

When you want to get the value back, you repeat the process but in reverse.

## Performance
If the number of collisions is high, the worst case runtime is O(N). This
happens when all of the keys hash to the same value, so searching through
its linked list will take O(N) time. To avoid this, we want to avoid
collisions, keeping the lookup time close to O(1).

Alternately, we can implement the hash table using a balanced binary
search tree instead of with an array of linked lists. What are the pros
and cons of this approach?

Pros:
1. Using less space -- we don't need to allocate a large array.
2. We can iterate through the hash table in order if we want to.

Cons:
1. We have a lookup time of O(logN).

# ArrayList & Resizeable Arrays
In a lot of languages, arrays have a fixed size (like in Java). When we
run out of space, we have to make a new array and copy our items over.
Data structures that automatically do this are called ArrayLists.

## Implementation
Usually, when our array gets full, we double its size and copy the items
over. This provides the best theoretical performance.

Each doubling will take O(N) time, but it happens less and less frequently.

## Performance
Since ArrayLists are just wrappers around arrays, they still have O(1)
random access. Insertion is considered O(1) "amortized". "Amortized" means
that it isn't exactly O(1), because we occasionally have to resize the
array in O(N) time, but it's close enough to be considered O(1) because
this happens so rarely.

An example: Imagine you have an array with size N. How many elements do we
copy each time the capacity increases?

When we increase the array to K elements, the array was previously half the
size, so we needed to copy K/2 elements. To get to N=K, we had to copy
N/2 elements at the final increase, previously N/4, previously N/8, and
so on. This leads to the series 1 + 2 + ... + N/4 + N/2, whose sum is just
slightly under N.

This means the worst-case insertion is O(N), but the average case insertion
is O(1).

# StringBuilder
## Problem
Normally, concatenating strings is expensive, because strings are immutable.
Every time you concatenate a string, a copy is created. If you're
concatenating a lot of strings, these copies will only grow larger and
larger, taking more and more time. This can be very inefficient.

For n words, each of size x, each concatenation results in the following
series:

x + 2x + 3x + ... + nx

x(1 + 2 + 3 + ... + n)

Recall that the series 1 + 2 + ... n can be expressed as n(n+1)/2.

xn(n+1)/2

After removing the constants, we see that our total runtime ends up being
O(XN^2).

## Solution
To get around this problem, we just make a resizable array of all of the
strings, and append them as we go.
For example, if we want to concatenate 'abc', 'def', and 'ghi', we would
first add them to the array ['abc', 'def', 'ghi']. From this array, we now
know how large our resulting string has to be, and we can concatenate
them all in one go. This drops the runtime down to:

N time to add all of the strings

X * N time to concatenate them all

This results in an improved runtime of O(N + XN).
