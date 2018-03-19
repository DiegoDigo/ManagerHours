from datetime import datetime, timedelta


def difference_hours(time_start, time_end):
    difference = datetime.strptime(time_end, "%H%M%S") - datetime.strptime(time_start, "%H%M%S")
    return timedelta(minutes=difference.total_seconds() / 60)

def bank_of_hours(time_start, time_end):   
   return str(60 / timedelta(datetime.strptime('090000', "%H%M%S")) - difference_hours(time_start, time_end) )
