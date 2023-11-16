import datetime


def validate_datetime(data: list):
    assert 3 <= len(data) <= 4
    date, time = data[0], data[1]
    validate_date(date)
    validate_time(time)
    if len(data) == 4:
        lat, long = data[2], data[3]
        validate_coords(lat, long)


def validate_date(date: str):
    # check if the format of date is right
    splitted_date = date.strip().split('.')
    assert len(splitted_date) == 3, 'Date is not in proper format'

    # check if date exists
    try:
        day, month, year = map(int, splitted_date)
        datetime.datetime(year=year, month=month, day=day)
    except ValueError:
        raise AssertionError('Date does not exist')


def validate_time(time : str):
    # check if the format of date is right
    splitted_time = time.strip().split(':')
    assert len(splitted_time) == 2

    # check if time is composed of integers
    try:
        hour, minute = map(int, splitted_time)
    except ValueError:
        raise AssertionError

    # check if time is correct
    assert 0 <= hour <= 23
    assert 0 <= minute <= 59


def validate_coords(lat: str, long: str):
    try:
        lat, long = map(float, (lat, long))
    except ValueError:
        raise AssertionError
    assert -90 <= lat <= 90
    assert -180 < long <= 180
