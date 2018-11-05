## Unit Quiz - Building on Hashing

#### First task

Sometimes we start with a hashing space that is too large or too small for our key set. In these instances we would like to be able to make `m` (our **hashspace** or the range of allowed hashed key values) larger to reduce collisions or smaller to save memory. To accomplish this you are going to add the following method to your data structure:

```java
//Updates m to the new value. Rehashes all keys
public void resize(int newM)
```

You may still ignore collisions.

#### Second task

It is time to resolve collisions. There are several different ways to do this, but I am going to encourage you to use "chaining." This means that all the keys that hash to the same value will be stored in a new data structure that starts at the appropriate index in the your main array. E.g.

| Array  |
|--------|
| []     |
| [K1, V1]     |
| []     |
| [K2, V2], [K3, V3]|
| []     |
| [K0, V0] |
| []     |


**Quick tips:**
- Given how data is stored in your dictionary, what is the easiest way to just expand that entry in your array?
- Make sure to update your `get`, `put`, and `remove` methods to account for this new behavior.

#### Third task

Modify your class to double the size of `m` when more than the total number of key-value pairs stored exceeds 80% of `m`.

#### Fourth task

Write a driver to make sure that your code works the way you expect it to. You may add 'getters' or modify your toString to aid in tests.
