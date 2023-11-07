import datetime
class DateModifier:
    # adds "days" days to given date
    def addDays(dateString, days):
        date = DateModifier.numericDate(dateString)
        newDate = date + datetime.timedelta(days=days)
        newDateString = DateModifier.stringDate(newDate)
        return newDateString

    # adds "weeks" weeks to given date
    def addWeeks(dateString, weeks):
        return DateModifier.addDays(dateString, weeks * 7)

    # convert string format (6 June 2021) to numeric format
    def numericDate(date):
        return datetime.datetime.strptime(date, '%d %B %Y')
    
    # convert numeric format to string format (6 June 2021)
    def stringDate(date):
        return date.strftime('%d %B %Y')

    # convert full date format (Sunday 6th of June 2021) to string format (6 June 2021)
    def parseDate(date):
        words = date.split()
        day = words[1].rstrip("stndrdth")
        month = words[3]
        year = words[4]
        parsedDate = f"{day} {month} {year}"
        return parsedDate