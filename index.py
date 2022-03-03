class Appointment:
    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description

    def __str__(self):
        str_date = str(self.date[0]) + '.' + str(self.date[1]) + '.' + str(self.date[2])
        text = f"\nTitle: {self.name}\nDate: {str_date}\nDescription: {self.description}"
        return text

    def date_string(self):
        return str(self.date[0]) + '.' + str(self.date[1]) + '.' + str(self.date[2])


def valid_date(s):
    date_split = s.split('.')
    if len(date_split) != 3:
        return False
    try:
        day = int(date_split[0])
        month = int(date_split[1])
        year = int(date_split[2])
        if day > 31 or month > 12 or year < 2021:
            return False
        return True
    except:
        return False
