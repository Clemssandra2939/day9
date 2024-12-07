# Nesting Lists and Dictionaries

# {
#     key:[list],
#     key2:{Dict},
# }

# Using a list and a dictionary as a value nested on another dictionary{}

# Nesting
capitals ={
 "France":"Paris",
 "Germany":"Berlin",
}

# Nesting a list in a Dictionary
travel_log ={
    "France":["Paris","Lille","Dijon"], #here list is used to mention different state in france because a key should hae one value
    "Germany":["Berlin","Hamburg","stuttgart"],
}

# Nesting Dictionary in a Dictionary and make more easy to understand 

travel_log ={
    "France":{"cities_visited": ["Paris","Lille","Dijon"],"total_visited": 12}, #
    "Germany":{"cities_visited":["Berlin","Hamburg","stuttgart"],"total_visited": 5},
}

# Adding muitiple dictionaries in a list 
 
travel_log = [
    {
        "country" :"France",
        "cities_visited" : ["Paris","Lille","Dijon"],
        "total_visited": 12
    }, 
    {
        "country" :"Germany",
        "cities_visited" :["Berlin","Hamburg","stuttgart"],
        "total_visited": 5
    },
]
 