from athleteTrainingPlan import AthleteTrainingPlan
from dateModifier import DateModifier
def main():
    # Get input dates as "Sunday 6th of June 2021"  and convert it to "6 June 2021" format
    startDate = DateModifier.parseDate(input('Enter Plan Start Date: '))
    raceDate = DateModifier.parseDate(input('Enter Race Date: '))
    # Calculate number of weeks
    numberOfWeeks = ((DateModifier.numericDate(raceDate) - DateModifier.numericDate(startDate)).days + 1) / 7
    # Check if valid
    if numberOfWeeks < 8 or numberOfWeeks != int(numberOfWeeks):
        return print("Dates provided doesn't complete right number of weeks.")
    # Generate training plan
    AthleteTrainingPlan.generatePlan(int(numberOfWeeks), startDate)

if __name__=="__main__": 
    main() 


# "Sunday 6th of June 2021"
# "Saturday 14th of August 2021"