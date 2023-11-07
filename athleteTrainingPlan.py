import math
from dateModifier import DateModifier
from printer import Printer
class AthleteTrainingPlan:
    # Generate whole plan
    def generatePlan(numberOfWeeks, startDate):
        Printer.printWeek(1, "Test", startDate)
        Printer.printWeek(2, "Test", DateModifier.addWeeks(startDate, 1))
        AthleteTrainingPlan.generateMainBlockWeeks(3, numberOfWeeks - 4, DateModifier.addWeeks(startDate,  2))
        Printer.printWeek(numberOfWeeks - 1, "Taper", DateModifier.addWeeks(startDate, numberOfWeeks - 2))
        Printer.printWeek(numberOfWeeks, "Race", DateModifier.addWeeks(startDate, numberOfWeeks - 1))

    # Generate plan for the main block weeks
    def generateMainBlockWeeks(weekNumber, numberOfWeeks, startDate):
        mainWeekTypes = ["Recovery", "Build1", "Build2", "Key"]
        startIndex = 0
        # add filler week if (9, 13, 17 ,...)
        if numberOfWeeks % 4 == 1:
            Printer.printWeek(weekNumber, "Filler", startDate)
            weekNumber += 1
            startDate = DateModifier.addWeeks(startDate, 1)
            numberOfWeeks -= 1
        # test weeks take place of  “recovery” & “build 1” week (in the first main block) if (10, 14, 18 ,...)
        elif numberOfWeeks % 4 == 2:
            startIndex = 2
        # second test week take place of  “recovery” week (in the first main block) if (11, 15, 19 ,...)
        elif numberOfWeeks % 4 == 3:
            startIndex = 1
        numberofRepeatedBlocks = math.ceil(numberOfWeeks / 4)
        Printer.printMainBlock(weekNumber, startDate, mainWeekTypes, numberofRepeatedBlocks, startIndex)
