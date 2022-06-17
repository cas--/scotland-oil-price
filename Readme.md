# Current daily oil price

A small script to fetch current daily oil price via Boilerjuice.

It uses requests to `priceChart.inc.php` with query params:

### Area `a`

```
0: UK
1: UK
2: Northern Ireland
3: England
4: Scotland
5: Wales
```

### Days `d`

Price history for 'x' days

### Oil Type `ot`

```
1: Heating Oil
2: Red Diesel
```

### Unknown params

Other params included by the website requests but have unknown purpose.

* `c`
* `va`
* `ex`
