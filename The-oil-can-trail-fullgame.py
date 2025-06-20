import random
import time

# Player state
player = {
    "battery": 100,
    "coolant": 2,
    "ammo": 1,
    "scrap": 3,
    "day": 1,
    "alive": True
}

# Encounters
encounters = [
    "drone_approach",
    "found_scrap",
    "cold_zone",
    "abandoned_weapon",
    "safe_day",
    "oil_leak",
    "friendly_drone"
]

def show_status():
    print(f"\nDay {player['day']} Status:")
    print(f"Battery: {player['battery']}% | Coolant: {player['coolant']} | Ammo: {player['ammo']} | Scrap: {player['scrap']}")

def encounter_drone():
    print("\n A Disassembly Drone is approaching!")
    print("1. Hide behind a car (safe, drains battery)")
    print("2. Fight with railgun (uses 1 ammo)")
    print("3. Use coolant to run away")
    print("4. Throw scrap metal to distract")

    while True:
        choice = input("Choose an action (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

    if choice == "1":
        player["battery"] -= 10
        print(" You hide and avoid detection. Battery drops by 10%.")
    elif choice == "2":
        if player["ammo"] > 0:
            player["ammo"] -= 1
            print(" You blast the drone. It's disabled for now.")
        else:
            print(" No ammo... the drone kills you.")
            player["alive"] = False
    elif choice == "3":
        if player["coolant"] > 0:
            player["coolant"] -= 1
            print(" You sprint away using coolant. You escaped!")
        else:
            print(" No coolant... the drone catches you.")
            player["alive"] = False
    elif choice == "4":
        if player["scrap"] > 0:
            player["scrap"] -= 1
            print(" You throw scrap to distract it. It works!")
        else:
            print(" No scrap to throw. You're done for.")
            player["alive"] = False

def found_scrap():
    gain = random.randint(1, 2)
    player["scrap"] += gain
    print(f"\n You found {gain} scrap metal!")

def cold_zone():
    print("\n You're in a freezing cold area. Battery drains faster.")
    player["battery"] -= 15
    if player["battery"] <= 0:
        print(" Battery fully drained... You shut down.")
        player["alive"] = False

def abandoned_weapon():
    print("\n You found an abandoned railgun with one cartridge.")
    player["ammo"] += 1

def safe_day():
    print("\n Nothing happens today. It's calm and quiet.")

def oil_leak():
    print("\n You sprung a slow oil leak. It makes everything harder.")
    player["battery"] -= 5
    player["scrap"] -= 1
    if player["scrap"] < 0:
        player["scrap"] = 0

def friendly_drone():
    print("\n You meet a strange drone. It gives you coolant and vanishes.")
    player["coolant"] += 1
    player["battery"] += 5
    if player["battery"] > 100:
        player["battery"] = 100

# Map encounters to functions
encounter_functions = {
    "drone_approach": encounter_drone,
    "found_scrap": found_scrap,
    "cold_zone": cold_zone,
    "abandoned_weapon": abandoned_weapon,
    "safe_day": safe_day,
    "oil_leak": oil_leak,
    "friendly_drone": friendly_drone
}

# Main Game Loop
while player["alive"] and player["day"] <= 15:
    show_status()
    event = random.choice(encounters)
    encounter_functions[event]()  # Run the encounter

    if player["alive"]:
        print("\n...Preparing for next day...\n")
        time.sleep(2)
        player["day"] += 1
    else:
        break

# Game Over Message
print("\n========================")
if player["alive"]:
    if player["battery"] >= 90 and player["ammo"] >= 1 and player["coolant"] >= 1:
        print("You not only survived—you became overpowered. The drones fear you now. CONGRATS YOU UNLOCKED THE SECRET ENDING YOU GET A CUSTOM WEBSITE!")
    else:
        print("You survived 15 days! Victory!")
    print("Thank you for playing! This was a game made by: imakecode. I fully coded this entire game. Thank you to Prof.Sir for supporting the idea.")
else:
    print("You did not survive. Game Over.")
    print("This has been a game by: imakecode")
print("========================")
