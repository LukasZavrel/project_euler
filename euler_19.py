#%%
months = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
year = 1900
day = 0
sundays = 0
while year < 2001:
    for month, days in months.items():
        day = (day + days + (month == 2) * (year % 4 == 0) * (year != 1900)) % 7
        if day == 6:
            sundays += 1
    year += 1
year = 1900
day = 0
while year < 1901:
    for month, days in months.items():
        day = (day + days + (month == 2) * (year % 4 == 0) * (year != 1900)) % 7
        if day == 6:
            sundays -= 1
    year += 1


print(sundays)
