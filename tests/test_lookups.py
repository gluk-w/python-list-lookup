from listlookup import ListLookup

sample_list = [
    {"id": 1, "country": "us", "name": "Atlanta"},
    {"id": 2, "country": "us", "name": "Miami"},
    {"id": 3, "country": "uk", "name": "Britain"},
    {"id": 5, "country": "uk", "name": "Bermingham"},
    {"id": 4, "country": "ca", "name": "Barrie"},
]


def test_lookups():
    cities = ListLookup(sample_list)
    cities.index("id", lambda d: d['id'], unique=True)
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


def test_callable_lookup():
    cities = ListLookup(sample_list)
    cities.index('country', lambda d: d['country'])
    cities.index('name', lambda d: d['name'])

    callback_call_count = 0

    def lookup_starts_with(v):
        nonlocal callback_call_count
        callback_call_count += 1
        return v.startswith('B')

    result = list(cities.lookup(country='uk', name=lookup_starts_with))
    assert len(result) == 2
    assert result[0]['name'].startswith('B')
    assert result[1]['name'].startswith('B')
    assert callback_call_count == 2  #


def test_lookup_terminated():
    cities = ListLookup(sample_list)
    cities.index("id", lambda d: d['id'])
    cities.index("country", lambda d: d['country'])

    result = list(cities.lookup(id=2, country="xx"))
    assert len(result) == 0


def test_lookup_nothing_found():
    cities = ListLookup(sample_list)
    cities.index("id", lambda d: d['id'])
    cities.index("country", lambda d: d['country'])

    result = list(cities.lookup(country="xx"))
    assert len(result) == 0
