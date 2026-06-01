##This version of the program is designed to help people understand the basics
##of PC components and what each component serves to do within a computer


print("Welcome to PC Part Solution!")
print("This program explains basic PC components \n")

print("Choose a PC part to learn about:")
print("1. CPU")
print("2. GPU")
print("3. RAM")
print("4. SSD")
print("5. Motherboard")

choice = input("Enter 1, 2, 3, 4, 5:")

if choice == '1':
    print("\n CPU: The brain of the computer. It runs the instructions and handles general tasks")
elif choice == '2':
    print("\n GPU: The graphics card, it handles the visuals, gaming performance, and rendering")
elif choice == '3':
    print("\n RAM: Short-term memory. It helps your keep acitve programs ready quickly.")
elif choice == '4':
    print("\n SSD: Long-term storage. SSDs are much faster than traditional hard drives")
elif choice == '5':
    print("\n MotherBoard: Main circuit board which acts as the central hub that allows other hardware inside to process information")
else:
    print("\n Invalid choice. Try running the program again.")







