from index import Appointment


def main(appointment_list, del_title):
    f = open("schedule.txt", "w")
    for appointment in appointment_list:

        # if the title doesn't match one of the appointments
        if appointment.name.find(del_title) == -1:
            new_name = appointment.name.replace(" ", "|")

            # Write it back in the file
            f.write(new_name + " " + appointment.date_string() + "\n")
            f.write(appointment.description + "\n")

        else:
            print("--Delete succesfull--")
