# Current daily oil price

A small script to fetch current daily oil price via Boilerjuice.

## Dependencies

* python3
* requests

Note: Using get_price_from_soup() will require BeautifulSoup and selenium.

## Run

```
$ python get_oil_price.py
114.69p

```

## Query params

Requests to `priceChart.inc.php` require the following query parameters

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
