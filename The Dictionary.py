# This was edited on 13/06/2026.

# WORDS - Keys 
# DEFINITIONS - Values
#KEY-VALUE Pairing

# The Dictionary in coding has three rules:
# 1. The keys must be unique.
# 2. The keys are immutable. 
# 3. The values can be anything. It can be a string, number, list or even another dictionary!

#Below are some coding examples of how dictionaries can be used in Python, starting with 'Empty Dictionary'

# Empty Dictionary
empty_dict = {}
empty_dict = dict()

# Filled Dictionary 
contacts = {

    "Alice": "198-23420-998",
    "Bob":"+122 98727 000",
    "Loni": "+44 91628 362",
   "Jackie": "+231 99999 676"

   }

#Dictionary Tracking 
a_gamer_profile = {

    "username": "ImAPro64",
    "level": 30,
    "is_online?": True, 
    "inventory": ["sword", "shield", "health_potion"]

}

user = {
    "name": "Loni",
    "role": "Developer"
}

# 1. The direct lookup way. 
# print(user)["name"])

# 2. The safer way.
print(user.get("name")) 


#Data Modification
hero = {

    "name": "Izuku",
    "bounty": "$10000",
    "gender": "male",
    "age": "16"

}

hero["bounty"] = "$9000"
hero["power_move"] = "Air Force!" # This will add the new key and value. 

print(hero) 
