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
    # Only subtract holidays that fall on a weekday inside the range, and count
    # each date once: a weekend holiday was never counted, and a repeated date
    # must not be subtracted twice.
    lo, hi = (start, end) if start <= end else (end, start)
    weekday_holidays = {h for h in holidays if lo < h <= hi and h.weekday() < 5}
    if start <= end:
        count -= len(weekday_holidays)
    else:
        count += len(weekday_holidays)
    return count
