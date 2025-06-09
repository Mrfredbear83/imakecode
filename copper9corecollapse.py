core_time = 197  # 3 minutes 17 seconds

drones = {
    "MD-01": "ACTIVE (82%) at Sector 7G",
    "MD-02": "ACTIVE (0% ) error_absolute_solver ",
    "MD-03": "ACTIVE (64%) at Sector 4D",
    "MD-04": "MALFUNCTION (10%) at Sector 9F"
}

event_log = [
    "Power surge detected in Sector 9F",
    "Drone MD-02 went offline unexpectedly",
    "Core temperature rising",
    "External breach detected at perimeter 3A",
    "Manual override attempt failed"
]

def format_time(t):
    return f"{t//60:02}:{t%60:02}"

print("CORE OF COPPER 9 TERMINAL")
print("SYSTEM STATUS: CRITICAL - CORE COLLAPSE")
print(f"TIME TO FAILURE: {format_time(core_time)}\n")

while core_time > 0:
    cmd = input("> ").strip().lower()

    if cmd == "scan drones status":
        for d, s in drones.items():
            print(f"{d}: {s}")
    elif cmd == "log last 5 system events":
        for e in event_log[-5:]:
            print(f"- {e}")
    elif cmd == "emergency protocol activate":
        print("Emergency protocol activated. +60 seconds added.")
        core_time += 60
    elif cmd == "help":
        print("Commands: scan drones status, log last 5 system events, emergency protocol activate, help, exit")
    elif cmd == "exit":
        print("Exiting terminal.")
        break
    else:
        print("Unknown command. Type 'help'.")

    core_time -= 1
    print(f"Time to failure: {format_time(core_time)}\n")

if core_time <= 0:
    print("CRITICAL: Core of Copper 9 has collapsed. System shutting down.")
