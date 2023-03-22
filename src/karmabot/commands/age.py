from datetime import datetime

ADL_PYTHON_BORN = datetime(year=2017, month=4, day=26)


def meetup_age(**kwargs) -> str:
    """Print Adelaide Python Meetup age in days"""
    today = datetime.now()
    days_old = (today - ADL_PYTHON_BORN).days
    return f"Adelaide Python Meetup is {days_old} days old"
