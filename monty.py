import random

#Performs one iteration of the Monty Hall problem.
#"switch" represents whether or not the player has chosen to switch
def monty(switch: bool) -> bool:
    prizes = ["goat", "goat", "car"]
    doors = {}

    # Places prizes randomly behind doors
    random.shuffle(prizes)
    for i in range(3):
        doors[i] = prizes[i]

    # Player picks a random door to look behind
    choice = random.choice([0, 1, 2])

    # This is a dictionary containing the remaining choices
    remaining_doors = {i: doors[i] for i in doors if i != choice}

    # Ensure that Monty can only choose doors which contain a door
    remaining_keys = list(remaining_doors.keys())
    keys = [i for i in remaining_keys if remaining_doors[i] != "car"]
    montys_choice = random.choice(keys)

    #Perform the switch
    if switch:
        remaining_keys.remove(montys_choice)
        choice = remaining_keys[0]

    # Open the door and return whether or not the door has a car behind it.
    return prizes[choice] == "car"

if __name__ == "__main__":
    n = int(input("Input iterations: "))
    print("Performing simulation " + str(n) + " times for switching")

    # Perform n simulations where the player chooses to switch
    success = 0
    failure = 0
    progress = 0
        
    for i in range(n):
        if (monty(True)):
            success += 1
        else:
            failure += 1

        prev_progress = progress
        progress += 1 / n
        if ((prev_progress * 100) // 10 != (progress * 100) // 10):
            print("completed " + str(round(progress * 100, 0)) + "%")

    success = round(success, 2)
    failure = round(failure, 2)

    print("Switch success rate = " + str(success/(success + failure) * 100) + "%")

    # Perform n simulations where the player chooses to stay

    print("Performing simulation " + str(n) + " times for non-switching")

    success = 0
    failure = 0
    progress = 0
        
    for i in range(n):
        if (monty(False)):
            success += 1
        else:
            failure += 1

        prev_progress = progress
        progress += 1 / n
        if ((prev_progress * 100) // 10 != (progress * 100) // 10):
            print("completed " + str(round(progress * 100, 0)) + "%")

    success = round(success, 2)
    failure = round(failure, 2)

    print("Stay success rate = " + str(success/(success + failure) * 100) + "%")

    input()
