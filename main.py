from pet import Pet

def main():
    # Create Lewis the goat 🐐
    pet_info = {"name": "Lewis", "type": "goat"}
    pet = Pet(pet_info["name"])

    # Add pet type dynamically 🐐
    pet.pet_type = pet_info["type"]

    # Displaying pet info 🎉
    print(f"🎉 You have a {pet.pet_type} named {pet.name}! 🐐🎉")

    # Feed the pet 🍽️
    pet.eat()
    print(f"{pet.name} is eating... 🍴")

    # Play with the pet 🏃‍♂️
    pet.play()
    print(f"{pet.name} is playing... 🐾")

    # Train the pet 🎓
    pet.train("jump")
    pet.train("headbutt")
    
    # Show tricks 🎩✨
    pet.show_tricks()  # Independent action
    
    # Show status 💖
    pet.get_status()   # Shows pet status: hunger, energy, happiness

    # Final message 🏁
    print(f"Thank you for spending time with {pet.name}! 🥰🐐")

# Start the main function 🚀
if __name__ == "__main__":
    main()
