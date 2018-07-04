import datetime

day_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}
day_of_week_number = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}


def days_different(date: datetime, days):
    delta = datetime.timedelta(days=days)
    print(date - delta)


def week_difference(date: datetime, weeks):
    delta = datetime.timedelta(weeks=weeks)
    print(date - delta)


def different(date: datetime, weeks, weekday):
    print(date.weekday())
    days = weeks * 7 + date.weekday() - day_of_week_number[weekday]
    if days < 0:
        days += 7

    print(days)
    print(day_of_week[date.weekday()])


different(datetime.date(2018, 11, 8), 1, "Friday")
