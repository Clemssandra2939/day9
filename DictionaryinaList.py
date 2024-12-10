# Coding char-Dic in list 

travel_log = [
{
    "country" :"France",
    "total_visited": 12,
    "cities_visited" : ["Paris","Lille","Dijon"],    
}, 
{
    "country" :"Germany",
    "total_visited": 5,
    "cities_visited" :["Berlin","Hamburg","stuttgart"],        
},
]
# TODO: Write the function that will allow new country to be added to travel_log
def add_new_country(country_visited,total_visited,cities_visited):
    new_country = {} 
    new_country["country"] = country_visited
    new_country["total_visits"] = total_visited
    new_country["cities"] = cities_visited     
    travel_log.append(new_country)
    
add_new_country("Russia",2,["Moscow","Saint Peterburg"])
print(travel_log)
