# 1. Declare and assign the variables here:
Name_of_the_space_shuttle = 'Determination'
Shuttle_Speed_MPH = 17500
Distance_to_mars_km = 225000000
Distnace_to_the_moon_km= 384400
Miles_per_kilometer = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(Name_of_the_space_shuttle))
print(type(Shuttle_Speed_MPH))
print(type(Distance_to_mars_km))
print(type(Distnace_to_the_moon_km))
print(type(Miles_per_kilometer))
# Code your solution to exercises 3 and 4 here:
miles_to_mars = Distance_to_mars_km * Miles_per_kilometer
hours_to_mars = miles_to_mars / Shuttle_Speed_MPH
days_to_mars = hours_to_mars / 24
print(Name_of_the_space_shuttle, 'will take', days_to_mars, 'days to reach mars.')
# Code your solution to exercise 5 here
miles_to_moon = Distnace_to_the_moon_km * Miles_per_kilometer
hours_to_moon = miles_to_moon / Shuttle_Speed_MPH
days_to_moon = hours_to_moon / 24
print(Name_of_the_space_shuttle, 'will take', days_to_moon, 'days to reach moon.')