from datetime import date, timedelta


def business_days_between(start: date, end: date, holidays=()) -> int:
    """Count business days after `start` up to and including `end`.

    Weekends (Saturday, Sunday) and the given holidays are not business days.
    A holiday that falls on a weekend, or is listed more than once, is
    subtracted only once (or not at all if it is a weekend day).
    If `end` is before `start`, the result is the negated count from `end`
    to `start`, consistent with the no-holiday case.
    """
    if end < start:
        return -business_days_between(end, start, holidays)
    days = (end - start).days
    weeks, rem = divmod(days, 7)
    count = weeks * 5
    for i in range(1, rem + 1):
        if (start + timedelta(days=i)).weekday() < 5:
            count += 1
    count -= len({h for h in holidays if start < h <= end and h.weekday() < 5})
    return count
