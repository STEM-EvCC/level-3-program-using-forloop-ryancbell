mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Counts total number of space missions
countTotal = 0
for totalMissions in mission_names:
    # Goes through the whole list
    countTotal += 1

print("Total number of missions: " + str(countTotal))

# Counts Total number of mission success
countSuccess = 0
for success in mission_success:
    if success is True:
        countSuccess += 1

print("Number of successful missions: " + str(countSuccess))

# Calculates the success rate of the missions
# (number of successful missions / total number of missions) * 100

totalRate = 0
for successRate in mission_success:
    totalRate += 1

successRate = (countSuccess / totalRate) * 100
print("Success Rate: " + str(f"{successRate:.2f}%"))


# Prints off names of missions launched before 2000
for names, years in zip(mission_names, mission_years):
     if years < 2000:
         print(names + " " + str(years))
