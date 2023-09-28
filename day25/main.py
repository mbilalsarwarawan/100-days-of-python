names=['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

new_names=[name.upper() for name in names if len(name)>5]
print(new_names)

numbers=[1,2,3,4,5]

squares= [n*n for n in numbers]
print(squares)

Numbers =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result=[n for n in Numbers if n%2==0]
print(result)


sentence ="What is the Airspeed Velocity of an Unladen Swallow?"
result1={word:len(word) for word in sentence.split()}
print(result1)

weather={
"Monday": 12,
"Tuesday": 14,
"Wednesday": 15,
"Thursday": 14,
"Friday": 21,
"Saturday": 22,
"Sunday": 24,}

f_weather={day:(temp*9/5)+32 for (day, temp) in weather.items()}
print(f_weather)