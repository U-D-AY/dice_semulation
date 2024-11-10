import random

dice_act = {
    1: (" ┌─────────┐",
        " │         │",
        " │    ●    │",
        " │         │",
        " └─────────┘"),

    2: (" ┌─────────┐",
        " │ ●       │",
        " │         │",
        " │       ● │",
        " └─────────┘"),
    3: (" ┌─────────┐",
        " │ ●       │",
        " │    ●    │",
        " │      ●  │",
        " └─────────┘"),
    4: (" ┌─────────┐",
        " │ ●     ● │",
        " │         │",
        " │ ●     ● │",
        " └─────────┘"),
    5: (" ┌─────────┐",
        " │ ●     ● │",
        " │    ●    │",
        " │ ●     ● │",
        " └─────────┘"),
    6: (" ┌─────────┐",
        " │ ●  ●  ● │",
        " │         │",
        " │ ●  ●  ● │",
        " └─────────┘"),
}
def roll_dices():
        num_of_dice = int(input("How many dice ?(maximum 5):"))
        if num_of_dice <= 5:
            roll_dice(num_of_dice)
        else:
            print("maximum number of dies are 5...!\n\n")

            
def roll_dice(num):
    dice = [random.randint(1, 6) for _ in range(num)]

    print("\nUser rolls the dice:")
    for line in range(5):
        for die in dice:
            print(dice_act.get(die)[line], end=" ")
        print()

    total = sum(dice)
    print(f"Total: {total}\n")

    return dice

print("Welcome to the Roll Dice Event!")

while True:
    user_input = input("\nDo you want to roll the dice? (yes/no)\n: ").lower()
    if user_input == 'no':
        print("Thanks for participating! Goodbye.")
        break
    elif user_input != 'yes':
        print("\nInvalid input. Please enter 'yes' or 'no'.\n")
        continue

    dice = roll_dices()
