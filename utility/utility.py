from datetime import datetime, timedelta


def difference_hours(time_start: str, time_end: str) -> int:
    difference = datetime.strptime(time_end, "%H%M") - datetime.strptime(time_start, "%H%M")
    return str(timedelta(minutes=difference.total_seconds() / 60))
    
