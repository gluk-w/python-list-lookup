# TupleLookup
Wrapper for faster lookups in a tuple of objects/dictionaries.

## Why tuple instead of a list
Because tuples are immutable

```
from tuple_lookup import TupleLookup
cities = TupleLookup([
  {"id": 1, "country": "us", name: "Atlanta"},
  {"id": 2, "country": "us", name: "Miami"},
  {"id": 3, "country": "uk", name: "Britain"},
])

cities.index("id", lambda d: d['id'], True)
cities.index("country", lambda d: d['country'])

cities.lookup(id=1)
>>> [{"id": 1, "country": "us", name: "Atlanta"}]

cities.lookup(country="us")
>>> [{"id": 1, "country": "us", name: "Atlanta"}, {"id": 2, "country": "us", name: "Miami"}]

cities.lookup(id=2, country="uk")
>>> []
```
