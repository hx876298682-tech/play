from datetime import date, timedelta
import argparse
import sys

import chinesecalendar as cc


def count_workdays(year: int, month: int) -> int:
    """Return number of working days in given month, considering Chinese holidays and adjusted weekends."""
    first_day = date(year, month, 1)
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)

    d = first_day
    workdays = 0
    while d < next_month:
        if cc.is_workday(d):
            workdays += 1
        d += timedelta(days=1)
    return workdays


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Count working days in Chinese calendar, including holidays and adjusted weekends")
    parser.add_argument("year", type=int, help="Year to calculate")
    parser.add_argument("-m", "--month", type=int, choices=range(1, 13), help="Optional month (1-12); calculate for entire year if omitted")
    args = parser.parse_args(argv)

    if args.month:
        print(f"{args.year}-{args.month:02d}: {count_workdays(args.year, args.month)} workdays")
    else:
        for m in range(1, 13):
            print(f"{args.year}-{m:02d}: {count_workdays(args.year, m)} workdays")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
