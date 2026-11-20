player_name = input("Wat is jouw naam? ")
player_gold = 100
inventory = []
print(f"Welkom, {player_name}! Je begint je avontuur met {player_gold} gold.")

while True:
    print("\n=== Fantasy Item Shop ===")
    print(f"Speler: {player_name} | Gold: {player_gold}")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")
    
    choice = input("What would you like to do? ")
    
    match choice:
        case "1":
            price = 50
            item = "Sword"
            if player_gold >= price:
                player_gold -= price
                inventory.append(item)
                print(f"Gefeliciteerd! Je hebt een {item} gekocht.")
                print(f"Je hebt nog {player_gold} gold over.")
            else:
                print("Je hebt niet genoeg gold om dit item te kopen!")
                
        case "2":
            price = 40
            item = "Shield"
            if player_gold >= price:
                player_gold -= price
                inventory.append(item)
                print(f"Gefeliciteerd! Je hebt een {item} gekocht.")
                print(f"Je hebt nog {player_gold} gold over.")
            else:
                print("Je hebt niet genoeg gold om dit item te kopen!")
                
        case "3":
            price = 20
            item = "Potion"
            if player_gold >= price:
                player_gold -= price
                inventory.append(item)
                print(f"Gefeliciteerd! Je hebt een {item} gekocht.")
                print(f"Je hebt nog {player_gold} gold over.")
            else:
                print("Je hebt niet genoeg gold om dit item te kopen!")
                
        case "4":
            price = 60
            item = "Bow"
            if player_gold >= price:
                player_gold -= price
                inventory.append(item)
                print(f"Gefeliciteerd! Je hebt een {item} gekocht.")
                print(f"Je hebt nog {player_gold} gold over.")
            else:
                print("Je hebt niet genoeg gold om dit item te kopen!")
                
        case "5":
            print("\n=== Jouw Inventory ===")
            if not inventory:
                print("Your inventory is empty!")
            else:
                for item in inventory:
                    print(f"- {item}")
            print(f"Je hebt nog {player_gold} gold over.")
            
        case "6":
            print("Bedankt voor je bezoek aan de winkel! Tot ziens.")
            print(f"Je verlaat het spel met een totaal van {player_gold} gold.")
            break
            
        case _:
            print("Ongeldige keuze! Voer een getal in tussen 1 en 6.")