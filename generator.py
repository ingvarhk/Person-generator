import random
print("Person generator 0.1")

def getRandomFromFile(path):
    try:
        f = open(path, "r", encoding="utf8")
    except:
        print("Could not find the file you are looking for: " + str(path))

    lines = f.readlines()
    f.close()
    
    return random.choice(lines)

def generate():
    print("generating...")
while True:
    print()
    
    name = getRandomFromFile("files\\Names.txt")
    age = random.randrange(1, 120)
    food = getRandomFromFile("files\\Food.txt")
    sport = getRandomFromFile("files\\Sports.txt")
    job = getRandomFromFile("files\\Jobs.txt")
    city = getRandomFromFile("files\\Cities.txt")
    personality = getRandomFromFile("files\\Personalities.txt")
    
    print("Name: " + name + "Age: " + str(age) + "\nFavorite food: " + food + "Personality: " + personality + "Lives: " + city + "Sport: " + sport + "Job: " + job)
    
    input("\nPress enter to generate a new person.")