from listlookup import ListLookup


def test_lookups():
    cities = ListLookup([
        {"id": 1, "country": "us", "name": "Atlanta"},
        {"id": 2, "country": "us", "name": "Miami"},
        {"id": 3, "country": "uk", "name": "Britain"},
    ])

    cities.index("id", lambda d: d['id'], True)
    cities.index("country", lambda d: d['country'])

    assert list(cities.lookup(id=1, preserve_order=True)) == [
        {"id": 1, "country": "us", "name": "Atlanta"}
    ]

    assert list(cities.lookup(id=1, country="us", preserve_order=False)) == [
        {"id": 1, "country": "us", "name": "Atlanta"}
    ]

    assert list(cities.lookup(country="us", preserve_order=True)) == [
        {"id": 1, "country": "us", "name": "Atlanta"},
        {"id": 2, "country": "us", "name": "Miami"}
    ]

    assert list(cities.lookup(id=2, country="uk")) == []
