#Nesting
travel_log = [
    {
    "country":"France",
    "visits" : 12,
    "cities" : ["Paris","Lille","Dijon"]},

    {
    "country" : "Germany",
    "visits" : 12,
    "cities":["Berlin","Hamburg","Stuttgart"],
    },
    ]


"""
travel_log2 = {
    "France" : {"Paris": 2,
                "Lille":3,
                "Dijon":4},
    "Germany": {"Berlin":2,
                "Hamburg":5,
                "Stuttgart":7},
}

travel_log3 ={
    {"country":"France",
    "cities_visited":["Paris","Lille","Dijon"],
     "total_visits": 20},

    {"country":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits":12}
}
"""

def add_new_country(country,num_of_visits,cities):
    new_dic = {}
    new_dic["country"] = country
    new_dic["visits"] = num_of_visits
    new_dic["cities"] = cities
    travel_log.append(new_dic)
    
    
   

add_new_country("Russia",2,["Moscow","Saint Petersbug"])
print(travel_log)