# programming_dictionary = {
    # # # "Bug": "An error in a program that prevents the program from running as expected.",
    # "Function": "A piece of code that you can easily call over and over again.",
# }

# Retrieving items from dictionary
# print(programming_dictionary["Function"])

# Adding new items to dictionary
# programming_dictionary["Loop"] = "The action fo doing something over and over again."
# print(programming_dictionary)

# Create an empty dictionary.
# empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#------------------------------------------------------------------#
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades = {}
# for key in student_scores:
#     score = student_scores[key]
#     if score > 90:
#         student_grades[key] = "Outstanding"
#     elif score > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# print(student_grades)
#------------------------------------------------------------------#
####################################################################################################################


####################################################################################################################
'''
{
    key: [List],
    key2: {Dict},
}

[
    {
        key: [List],
        key2: {Dict},
    },
    {
        key: Value,
        key2: Value,
    }
]
'''
# Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# Nesting Lists and Dictionaries
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# Nesting Dictionary in Dictionary
# travel_log = {
#     "France": {
#         "cites_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     "Germany": {
#         "cites_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visited": 5
#     },
# }

# Nesting Dictionary in a List
# travel_log = [
#     {   
#         "country": "France", 
#         "cites_visited": ["Paris", "Lille", "Dijon"],
#         "total_visited": 12
#     },
#     {   
#         "country": "Germany",
#         "cites_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visited": 5
#     },
# ]
# print(travel_log[0]["cites_visited"])

#------------------------------------------------------------------#
# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# def add_new_country(country, visits, cities):
#     # new_country = {}
#     # new_country["country"] = country
#     # new_country["visits"] = visits
#     # new_country["cities"] = cities
#     # travel_log.append(new_country)
#     travel_log.append({
#         "country": country,
#         "visits": visits,
#         "cities": cities
#     })

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]

# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")
#------------------------------------------------------------------#

# **Secret Auction
####################################################################################################################
