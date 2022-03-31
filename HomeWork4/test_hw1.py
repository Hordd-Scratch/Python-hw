import pytest
from hw1 import make_filter, Filter


@pytest.mark.parametrize(
    "filter, data, expected_result",
    [(
            Filter(lambda a: a % 2 == 0,
                   lambda a: a > 0,
                   lambda a: isinstance(int, a)),
            range(100),
            [i * 2 for i in range(49)])
    ])
def test_class_filter(filter, data, expected_result):
    positive_even = filter
    positive_even.apply(data)
    assert positive_even == expected_result


@pytest.mark.parametrize(
    "filter, data, expected_result",
    [(
            make_filter(name='polly',
                        type='bird'),
            [{
                "name": "Bill",
                "last_name": "Gilbert",
                "occupation": "was here",
                "type": "person",
            }, {
                "is_dead": True,
                "kind": "parrot",
                "type": "bird",
                "name": "polly"
            }],
            [{
                "is_dead": True,
                "kind": "parrot",
                "type": "bird",
                "name": "polly"
            }]

    )])
def test_make_filter(filter, data, expected_result):
    assert make_filter() == expected_result
