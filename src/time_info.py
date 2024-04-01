import datetime

def return_current_time():
    now = datetime.datetime.now()

    formatted_hour = str(now.hour).zfill(2)
    formatted_minute = str(now.minute).zfill(2)
    formatted_second = str(now.second).zfill(2)

    return f"{formatted_hour}:{formatted_minute}:{formatted_second}"