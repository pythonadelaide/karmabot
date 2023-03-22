from datetime import datetime

from freezegun import freeze_time

from karmabot.commands.age import meetup_age


@freeze_time(datetime(2017, 8, 23))
def test_pybites_age():
    expected = "Adelaide Python Meetup is 119 days old"
    assert meetup_age() == expected
