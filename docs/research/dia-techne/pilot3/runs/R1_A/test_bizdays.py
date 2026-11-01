import random
from datetime import date, timedelta

import numpy as np
import pytest

from bizdays import business_days_between

BASE = date(2026, 1, 1)


def numpy_ref(start, end, holidays=()):
    # busday_count counts [begin, end); shift both by one day to get (start, end].
    # Used only for start <= end: for a reversed range numpy counts -(end, begin],
    # which after the shift is not the mirror -(end, start] this function keeps.
    assert start <= end
    one = np.timedelta64(1, "D")
    return int(np.busday_count(np.datetime64(start) + one,
                               np.datetime64(end) + one,
                               holidays=[np.datetime64(h) for h in holidays]))


def brute(start, end, holidays=()):
    if end < start:
        return -brute(end, start, holidays)
    hs = set(holidays)
    return sum(1 for i in range(1, (end - start).days + 1)
               if (d := start + timedelta(days=i)).weekday() < 5 and d not in hs)


@pytest.mark.parametrize("start,end,holidays,expected", [
    # Mon 2026-11-02 .. Mon 2026-11-09: Tue-Fri + Mon = 5
    (date(2026, 11, 2), date(2026, 11, 9), [], 5),
    # holiday on Saturday must not reduce the count (was 4)
    (date(2026, 11, 2), date(2026, 11, 9), [date(2026, 11, 7)], 5),
    # same weekday holiday listed twice is subtracted once (was 3)
    (date(2026, 11, 2), date(2026, 11, 9), [date(2026, 11, 4)] * 2, 4),
    # reversed range with a holiday inside it (was -2: holiday ignored)
    (date(2026, 11, 6), date(2026, 11, 4), [date(2026, 11, 5)], -1),
    (date(2026, 11, 2), date(2026, 11, 2), [date(2026, 11, 2)], 0),
])
def test_cases(start, end, holidays, expected):
    assert business_days_between(start, end, holidays) == expected
    assert brute(start, end, holidays) == expected
    if start <= end:
        assert numpy_ref(start, end, holidays) == expected


def test_random_against_numpy_and_brute():
    rng = random.Random(20261031)
    for _ in range(20000):
        s = BASE + timedelta(days=rng.randrange(120))
        e = BASE + timedelta(days=rng.randrange(120))
        h = [BASE + timedelta(days=rng.randrange(130)) for _ in range(rng.randrange(6))]
        got = business_days_between(s, e, h)
        assert got == brute(s, e, h), (s, e, h)
        if s <= e:
            assert got == numpy_ref(s, e, h), (s, e, h)
        else:
            assert got == -business_days_between(e, s, h), (s, e, h)
