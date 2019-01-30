
totalNeedHours          = 19
lastDays                = 15
learnHoursPerDay        = 2
learnHoursMustPerDay    = 0.5

def lastNeedHours(lastDays, learnHoursOneDay, TotalNeedHours):
    print("LastDays = ", lastDays, ", learnHoursOneDay = ", learnHoursOneDay, ", TotalNeedHours = ", TotalNeedHours)
    if TotalNeedHours <= 0 :
        return;
    lastNeedHours(lastDays - 1, learnHoursOneDay, TotalNeedHours - learnHoursOneDay)



def lastNeedHoursWithouthalf(lastDays, learnHoursOneDay, learnHoursMustOneDay, TotalNeedHours):
    if TotalNeedHours <= 0 :
        return;
    if (lastDays * learnHoursMustOneDay) >= TotalNeedHours:
        learnHoursOneDay = learnHoursMustOneDay;
    print("LastDays = ", lastDays, ", learnHoursOneDay = ", learnHoursOneDay, ", TotalNeedHours = ", TotalNeedHours)
    lastNeedHoursWithouthalf(lastDays - 1, learnHoursOneDay, learnHoursMustOneDay, TotalNeedHours - learnHoursOneDay)


lastNeedHours(lastDays, learnHoursPerDay, totalNeedHours)

print("-----------------------------------------------------")

lastNeedHoursWithouthalf(lastDays, learnHoursPerDay, learnHoursMustPerDay, totalNeedHours)