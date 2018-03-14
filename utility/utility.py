from datetime import datetime, timedelta


def difference_hours(time_start, time_end):
    difference = datetime.strptime(time_end.strftime("%H%M%S"), "%H%M%S") - datetime.strptime(time_start.strftime("%H%M%S"), "%H%M%S")
    return timedelta(minutes=difference.total_seconds() / 60)

def bank_of_hours(time_start, hour_entry, time_end, hour_exit):
   return str(difference_hours(time_start, hour_entry) + difference_hours(time_end, hour_exit))
