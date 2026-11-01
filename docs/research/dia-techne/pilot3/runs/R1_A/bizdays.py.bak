from datetime import date, timedelta


def business_days_between(start: date, end: date, holidays=()) -> int:
    """Count business days after `start` up to and including `end`.

    Weekends (Saturday, Sunday) and the given holidays are not business days.
    """
    days = (end - start).days
    weeks, rem = divmod(days, 7)
    count = weeks * 5
    for i in range(1, rem + 1):
        if (start + timedelta(days=i)).weekday() < 5:
            count += 1
    count -= sum(1 for h in holidays if start < h <= end)
    return count
