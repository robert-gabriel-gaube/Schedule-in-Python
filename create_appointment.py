from index import Appointment
from index import valid_date


def main():
    print("Creating a new appointment....")

    # used for creating multiple appointments
    ok = ""

    while ok == "":
        # appointment information
        title = input("Input an appointment title\n>>>")
        date = input("\nInput the appointment's date (dd.mm.yyyy) \n>>>")

        # don't continue if an invalid date was inputted
        if not valid_date(date):
            print("\nInvalid date\n")
            continue
        description = input("\nInput the appointment's description\n>>>")

        # reformat title
        title = title.replace(" ", "|")

        # remove 0 from date eg. 01.02 -> 1.2
        if date[0] == '0':
            date = date[1:]
            if date[2] == '0':
                date = date[:2] + date[3:]

        elif date[3] == '0':
            date = date[:3] + date[4:]

        # input smt for stopping, leave empty otherwise
        ok = input("\n>>>")

        # new line
        print(" ")

        # write it to file
        f = open("schedule.txt", "a")
        f.write(title + " " + date + "\n" + description + "\n")

