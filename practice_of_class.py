

# 1. plan a tour in rangamati

# destination ="Rangamati"
# country="Bangaldesh"
# budget=10000
# days =3
# daiy_budget= days/budget 

#   what if i calculated the daily_budget for 10 people then we use the function:
# 1.we create the two function : get_daily_budget , Trip_type function


# def get_daily_budget(budget,days):
#     return budget/days

# def Trip_type(budget):
#     if budget>=10000:
#         return "God Trip"
#     return "Bad Trip"

# print(get_daily_budget(10000,3))
# print(Trip_type(5000))
 
#  tour e jawar por activity : activity onk type hoite pare : eating ,swimming, as different type of ativity and we should  readability te code then we create the blueprint that all ativity use the same blueprint:


AVAILABLE_ACTIVITY=[

    {
        "name":"Seafood",
        "type":"eating"
    },

    {
        "name":"swim at sea",
        "type":"swimming"

    }
]

class TripPlanner :

    def __init__(self,activity_type,budget,days):
        self.activity_type=activity_type
        self.budget=budget
        self.days=days


    def get_activity(self):
        return [activity["name"] for activity in AVAILABLE_ACTIVITY if self.activity_type==activity["type"]]

    
    def Trip_type(self):
       if self.budget>=10000:
        return "God Trip"
       return "Bad Trip"

    def get_daily_budget(self):
       return self.budget/self.days


trip1=TripPlanner("eating",10000,3)
print(trip1.get_activity())
print(trip1.Trip_type())
print(trip1.get_daily_budget())

