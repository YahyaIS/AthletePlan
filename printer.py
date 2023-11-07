from dateModifier import DateModifier
class Printer:
    # Print program of main block weeks
    def printMainBlock(weekNumber, startDate, types, numberofRepeatedBlocks, startIndex):
        for i in range(numberofRepeatedBlocks):
            for j in range(startIndex, len(types)):
                Printer.printWeek(weekNumber, types[j], startDate)
                weekNumber += 1
                startDate = DateModifier.addWeeks(startDate, 1)
            startIndex = 0

    # Print program of one week
    def printWeek(weekNumber, type, startDate):
        startDay, startMonth, _ = startDate.split()
        endDay, endMonth, _ = DateModifier.addDays(startDate, 6).split()
        print(f"Week #{weekNumber} - {type} - from {int(startDay)} {startMonth} to {int(endDay)} {endMonth}")

