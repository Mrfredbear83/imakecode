import random
import time  # Added to control pacing between days

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
    "safe_day"
]

def show_status():
    print(f"\nDay {player['day']} Status:")
    print(f"Battery: {player['battery']}% | Coolant: {player['coolant']} | Ammo: {player['ammo']} | Scrap: {player['scrap']}")
    
def encounter_drone():
    print("\n A Disassembly Drone is approaching!")
    print("1. Hide behind a car (safe, drains battery)", flush=True)  # line 28
    print("2. Fight with railgun (uses 1 ammo)", flush=True)         # line 30
    print("3. Use coolant to run away", flush=True)                   # line 31
    print("4. Throw scrap metal to distract", flush=True)
    choice = input("Choose an action (1-4): ")
    
    # rest of the function unchanged...


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
    else:
        print(" Uh oh... You hesitate and get caught.")
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

# Map encounters to functions
encounter_functions = {
    "drone_approach": encounter_drone,
    "found_scrap": found_scrap,
    "cold_zone": cold_zone,
    "abandoned_weapon": abandoned_weapon,
    "safe_day": safe_day
}

# Main Game Loop
while player["alive"] and player["day"] <= 10:
    show_status()
    event = random.choice(encounters)
    encounter_functions[event]()  # Run the encounter

    if player["alive"]:
        print("\n...Preparing for next day...\n")
        time.sleep(2)  # Pause for 2 seconds before next day
        player["day"] += 1
    else:
        break

# Game Over Message
print("\n========================")
if player["alive"]:
    print("You survived 10 days! Victory!")
    print("Thank you for playing! This was a game made by: imakecode. I fully coded this entire game. Thank you to Prof.Sir for supporting the idea.")
else:
    print("You did not survive. Game Over.")
    print("This has been a game by: imakecode")
print("========================")
