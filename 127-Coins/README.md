# ThinkNation Question Of The Week (Week 39, 2015)
[http://thinknation.ca/question-of-the-week/Coins](http://thinknation.ca/question-of-the-week/Coins)

## Question of the Week - Coins
Given a supply of coins of four arbitrary denominations (given as input) output the smallest number of coins it takes to create a value of 100, or 0 if this is impossible for the given coin values. You may assume there are no duplicate values and the values are always provided in ascending order.

Sample Input

```
7 31 46 90
```


Sample Output

```
4
```

## Usage and example

```
(qotw)macbook:coins joeyoung$ python coins.py <<< "7 31 46 90"
4
(qotw)macbook:coins joeyoung$ python coins.py <<< "46 67 82"
0
(qotw)macbook:coins joeyoung$ python coins.py <<< "1 17 33 40"
4
(qotw)macbook:coins joeyoung$ python coins.py <<< "3 13"
10
```