users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

jonathans_twitter = users['Jonathan']['twitter']
print(jonathans_twitter)

# 2. Get Erik's hometown

eriks_hometown = users['Erik']['home_town']
print(eriks_hometown)

# 3. Get the list of Erik's lottery numbers

eriks_lottery_numbers = users['Erik']['lottery_numbers']
print(eriks_lottery_numbers)

# 4. Get the species of Avril's pet Monty

avrils_pet_monty_species = users['Avril']['pets'][0]
print(avrils_pet_monty_species)

# 5. Get the smallest of Erik's lottery numbers

smallest_erik_lottery_number = users['Erik']['lottery_numbers'][2]
print(smallest_erik_lottery_number)

# 6. Return an list of Avril's lottery numbers that are even

avrils_lottery_numbers = users['Avril']['lottery_numbers']
avrils_lottery_numbers.sort()
print(avrils_lottery_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

eriks_lottery_numbers.insert(5, 7)
print(eriks_lottery_numbers)

# 8. Change Erik's hometown to Edinburgh

users['Erik']['home_town'] = 'Edinbrugh'

# 9. Add a pet dog to Erik called "fluffy"

another_erik_pet = {
  "name": "spike",   
  "species": "dog",
}
users[Erik][pets].append(another_erik_pet)

# 10. Add another person to the users dictionary

users['Cammy'] = 

