#Exercise 0
fav_colours = ["red", "yellow", "orange", "black", "green"]
ages = [22, 20, 29, 22, 30]
coin_flip = ["heads", "tails", "heads", "heads", "tails"]
fav_artist = ["Drake", "Kendrick Lamar", "Big Sean"]

words_defs = {
    "semantic": "related to meaning in language or logic",
    "successful": "accomplishing an aim or purpose",
    "creative": "having good imagination or original ideas"
}

fav_movies = {
    "Inception": 2010,
    "The Hangover": 2009,
    "Avengers": 2019
}

cities = {
    "Toronto": 2.93,
    "Los Angeles": 4.0,
    "Manila": 12.8
}

names = {
    "Rachel": 23,
    "Edna": 60,
    "Jan": 29,
    "Steven": 40
}

#Exercise 1

#1.
print(coin_flip)

#2.
print(fav_colours[0])

#3.
(ages.sort())

#4.
(ages.append(0))

#5.
print(fav_movies["Inception"])

#Exercise 2

#1.
print(fav_colours[-1])

#2.
cities["Tokyo"] = 13.6

#3.
coin_flip.reverse()

#4.
print(cities["Toronto"])

#5.
print("I think {} is great.".format(fav_artist[0]))
print("I think {} is great.".format(fav_artist[1]))
print("I think {} is great.".format(fav_artist[2]))

#Exercise 3

#1.
print(fav_artist[0:2])

#2.
for key, val in fav_movies.items():
    print("{} came out in {}.".format(key, val))

#3.
print(list(reversed(sorted(ages))))

#4.
fav_movies["Beauty and the Beast"] = "1991", "2017"
print(fav_movies)

#Exercise 4

#1.
for age in ages:
    if age <25:
        print(age)

#2.
ages.sort()
print(ages[-1])

#3.
coin_flip.count("heads")
print(coin_flip)

#4.
(fav_artist.pop(2))
print(fav_artist)

#5.
cities["Tokyo"] = '10.2'
print(cities)

#Exercise 5

#1.
#print(sum(cities.values()))

#2. 
for names, ages in names.items():
    if ages >= 30:
        print("{} is old.".format(names))
    else: print("{} is young.".format(names))

#3.
print(fav_colours[-2:])

#4.
#for age in ages:
    #print(ages +1)


#5.
fav_colours.append("blue")
fav_colours.append("purple")
print(fav_colours)

#Exercise 6

#1.
listed_movies = {
    1999 : ["The Matrix", "Star Wars: Episode 1", "The Mummy"],
    2009 : ["Avatar", "Star Trek", "District 9"],
    2019 : ["How to Train Your Dragon 3", "Toy Story 4", "Star Wars: Episode 9"],
}

#2.
phone_buttons = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ["*",0,"#"]
]

#3.
country_info = [
    {
        "Country":"Canada",
        "Continent":"North America",
        "Island": False,
    },

    {
        "Country":"China",
        "Continent":"Asia",
        "Island": True,
    },

    {
        "Country":"Germany",
        "Continent":"Europe",
        "Island": False,
    },
]

#Exercise 7

#1.
for i in range(20):
    print("I will not skateboard in the halls")

#2.
my_list = []
for i in range(20):
    my_list.append("I will not skateboard in the halls")
print(my_list)

#3.
numbers_list = []
for i in range(1,51):
    numbers_list.append(i)
print(numbers_list)

#4.
total = 0
for num in numbers_list:
    total += num
print(total)

#5.
triple_list = []
for i in range(1,51):
    triple_list.append(i)
    triple_list.append(i)
    triple_list.append(i)
print(triple_list)

#6.
for country in country_info:
    if country["Island"] == False:
        print(country["Country"])

#Exercise 8
expenses_list = [45.50, 50.25, 300, 60.25, 30.15, 200, 150.35]
expenses_list2 = [233, 50.56, 60, 23.45, 43.34]



def calculate_expenses(list):
    total = 0
    for expense in list:
        total = total + expense
    return total

print(calculate_expenses(expenses_list))    
print(calculate_expenses(expenses_list2))    






















