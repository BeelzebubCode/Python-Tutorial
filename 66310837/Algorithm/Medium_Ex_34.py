word = input().replace(",", "").replace(".", "").lower().split()

print("Spoiler detected!" if input().lower() in word else "No spoiler.")