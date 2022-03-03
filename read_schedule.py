import datetime as dt
from index import Appointment


def main():
    schedule = open("schedule.txt", "r")

    schedule_not_format = schedule.readlines()

    appointment_list = []

    # format schedule
    schedule_format = []

    for index in range(0, len(schedule_not_format), 2):
        # split title and date
        title_date = schedule_not_format[index].replace('\n', '').split()
        if len(title_date) < 2:
            break
        # split day month year
        date = title_date[1].split('.')

        description = schedule_not_format[index + 1].replace('\n', '')

        # create Appointment object
        appointment = Appointment(title_date[0].replace("|", " "), date, description)

        # append to appointments
        appointment_list.append(appointment)

    return appointment_list
