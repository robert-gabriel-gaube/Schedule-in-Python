from index import Appointment
import datetime as dt
import read_schedule
import create_appointment
import delete_appointment

appointment_list = read_schedule.main()
text = """
            create - Add a new appointment
            clear - Clear screen
            delete <text> - Deletes everything that containts text in the title or, if the title isn't specified all items will be deleted
            list - Lists every appointment
            exit - Exits program
            help - Shows commands
        """

while 1:
    command = input("Input command >>> ")
    if command == "create":
        create_appointment.main()
        appointment_list = read_schedule.main()

    elif command == "clear":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    # delete <title>
    elif command.find("delete") != -1:
        delete_appointment.main(appointment_list, command[7:])
        appointment_list = read_schedule.main()

    elif command == "list":
        print("\n\n\n")
        for appointment in appointment_list:
            print(appointment)
            print("-----------------------------------------------------------------------------------------")
        print("\n")

    elif command == "exit":
        break

    elif command == "help":
        print(text)

    else:
        print("Command unrecognized")
