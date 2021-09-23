"""Choose Your Own Adventure - "Cooking for College Students"."""


points: int = 0
player: str = ""
PANCAKE_EMOJI: str = "\U0001F95E"
DREAMING_EMOJI: str = "\U0001F634"
BANANA_EMOJI: str = "\U0001F34C"
PEANUT_EMOJI: str = "\U0001F95C"
BUTTER_EMOJI: str = "\U0001F9C8"
THUMBS_UP_EMOJI: str = "\U0001F44D"
EGG_EMOJI: str = "\U0001F95A"
BREAD_EMOJI: str = "\U0001F35E"
OK_HAND_EMOJI: str = "\U0001F44C"


def main() -> None:
    greet()
    print("Choose option 1: A savory breakfast")
    print("Choose option 2: A sweet breakfast")
    print("Or choose option 3: Go back to sleep")
    option_choice: int = int(input("Enter the number of your option choice: "))
    print(" ")
    while option_choice < 1 or option_choice > 3:
        print("Invalid entry, try again.")
        option_choice: int = int(input("Enter the number of your option choice: "))
    if option_choice >= 1 and option_choice <= 2:
        if option_choice == 1:
            from random import randint
            eggs: int = randint(2, 7)
            savory_points: int = savory(eggs)
            global points
            change_points(points, savory_points)
        if option_choice == 2:
            sweet()
    else:
        goodbye()
    print(f"Hey {player}! It seems like you're getting full; choose whether to keep playing or finish the game.")
    will_play: str = input("Enter \"Keep playing\" to restart the game, or \"Finish\" to exit the game. ")
    if will_play == "Keep playing":
        main()
    else:
        print(f"You finished the game with {points} health points, good job!")
        print(f"Thanks for playing, {player}!")


def change_points(a: int, b: int) -> int:
    c = a + b
    global points
    points = c
    return points


def greet() -> None:
    print("Welcome to \"Cooking for College Students\"")
    global player
    player = input("Enter your name: ")
    print(" ")
    print(f"Hello {player}, you're a 20 year old college student, and you've just woken up on a Saturday at 1pm.")
    global points
    change_points(points, 10)
    print(f"You slept well, so you're starting off with {points} health points.")
    print("You feel hungry and want to eat breakfast. Do you...")
    print(" ")


def goodbye() -> None:
    print(f"You've chosen to go back to sleep. Sweet dreams, {player} {DREAMING_EMOJI}.")
    print(f"Game ended with {points} health points.")
    again: str = input("Type \"Wake up\" to play again, or \"End\" to exit the game. ")
    if again == "Wake up":
        change_points(points, -10)
        main()
    if again == "End":
        print(f"Goodbye, {player}!")


def savory(e: int) -> int:
    print(f"You chose a savory breakfast! You peek in your fridge to see a carton with {e} eggs left {EGG_EMOJI}, 7 health points per egg.")
    confident: bool = False
    while confident is False:
        cooking_eggs: int = int(input("How many eggs do you want to cook with? Please enter a number: "))
        while cooking_eggs < 0 or cooking_eggs > e:
            print("Invalid entry, try again.")
            cooking_eggs: int = int(input("How many eggs do you want to cook with? Please enter a number: "))
        if cooking_eggs == 0:
            you_sure: str = input("Are you sure you don't want to cook with eggs? Type \"Yes\" or \"No\". ")
            while you_sure != "Yes" and you_sure != "No":
                print("Invalid entry, try again.")
                you_sure: str = input("Are you sure you don't want to cook with eggs? Type \"Yes\" or \"No\". ")
            if you_sure == "Yes":
                confident = True
                print(f"You decided not to cook with eggs, but remembered that you have bread {BREAD_EMOJI}. After a moment, you decide to make toast, 5 health points.")
                print(f"Good thinking, {player}!")
            else:
                confident = False
            print("You make a single piece of toast! You would've made more, but that was your last slice of bread. You really need to start grocery shopping after class.")
            toast_points: int = 5
            s_points: int = 0 + toast_points
            print(f"You gained {s_points} health points from that meal!")
            finished: str = input("Enter \"Something else\" to make something else, or \"Finish eating\" to finish your meal. ")
            while finished != "Something else" and finished != "Finish eating":
                print("Invalid entry, try again.")
                finished: str = input("Enter \"Something else\" to make something else, or \"Finish eating\" to finish your meal. ")
            if finished == "Something else":
                sweet()
        else:
            egg_points: int = cooking_eggs * 7
            s_points: int = 0 + egg_points
            print(f"You grab the eggs and walk to the dorm kitchen. As you cook all {cooking_eggs} eggs in the one pan that you brought to college, you get hungrier.")
            print(f"Do you want to make toast too, or just eat the eggs? Your meal is currently worth {s_points} health points.")
            want_toast: str = input("Enter \"Toast\" to make toast too, or enter \"Just eggs\" to only eat the eggs. ")
            while want_toast != "Toast" and want_toast != "Just eggs":
                print("Invalid entry, try again.")
                want_toast: str = input("Enter \"Toast\" to make toast too, or enter \"Just eggs\" to only eat the eggs. ")
            if want_toast == "Just eggs":
                print("Great! Your eggs finished cooking and you added salt and pepper to taste.")
                eat_eggs: str = input("Do you want to eat your eggs, or save them for later and make something else? Enter \"Eat now\" to eat them now, or enter \"Save for later\" to make something else. ")
                while eat_eggs != "Eat now" and eat_eggs != "Save for later":
                    print("Invalid entry, try again.")
                    eat_eggs: str = input("Do you want to eat your eggs, or save them for later and make something else? Enter \"Eat now\" to eat them now, or enter \"Save for later\" to make something else. ")
                if eat_eggs == "Eat now":
                    print(f"Delicious! {OK_HAND_EMOJI}")
                    print(f"That meal was {s_points} health points! Do you want to make something else, or finish eating?")
                    something_else: str = input("Enter \"Something else\" to make something else, or \"Finish eating\" to finish your meal. ")
                    while something_else != "Something else" and something_else != "Finish eating":
                        print("Invalid entry, try again.")
                        something_else: str = input("Enter \"Something else\" to make something else, or \"Finish eating\" to finish your meal. ")
                    if something_else == "Something else":
                        sweet()
                    else:
                        print(f"Great! You gained {s_points} health points from your savory breakfast!")
                if eat_eggs == "Save for later":
                    sweet()
            else:
                print("You make a single piece of toast! You would've made more, but that was your last slice of bread. You really need to start grocery shopping after class.")
                toast_points: int = 5
                s_points = s_points + toast_points
                print(f"You gained {s_points} health points from that meal!")
                finished: str = input("Enter \"Something else\" to make something else, or \"Finish eating\" to finish your meal. ")
                while finished != "Something else" and finished != "Finish eating":
                    print("Invalid entry, try again.")
                    finished: str = input("Enter \"Something else\" to make something else, or \"Finish eating\" to finish your meal. ")
                if finished == "Something else":
                    sweet()
    e = s_points
    return e


def sweet() -> None:
    print(f"You chose a sweet breakfast! Looking around your dorm, you see leftover pancakes {PANCAKE_EMOJI}, 5 health points.")
    eat_more: bool = True
    while eat_more is True:
        print(f"Choose two out of three toppings, but choose wisely {player}!")
        print(f"Banana {BANANA_EMOJI}, 15 health points.")
        print(f"Peanut butter {PEANUT_EMOJI}, 10 health points.")
        print(f"Butter {BUTTER_EMOJI}, 0 health points.")
        pancakes: int = 5
        banana: int = 15
        peanut_butter: int = 10
        sweet_points: int = 0 + pancakes
        first_topping: str = input("Enter first topping choice: ")
        while first_topping != "Banana" and first_topping != "Peanut butter" and first_topping != "Butter":
            print("Invalid entry, try again.")
            first_topping: str = (input("Enter a first topping choice: "))
        if first_topping == "Banana":
            sweet_points = sweet_points + banana
        if first_topping == "Peanut butter":
            sweet_points = sweet_points + peanut_butter
        second_topping: str = input("Enter second topping choice: ")
        while second_topping != "Banana" and second_topping != "Peanut butter" and second_topping != "Butter":
            print("Invalid entry, try again.")
            second_topping: str = input("Enter second topping choice: ")
        while second_topping == first_topping:
            second_topping: str = input("Please choose a different second topping: ")
        if second_topping == "Banana":
            sweet_points = sweet_points + banana
        if second_topping == "Peanut butter":
            sweet_points = sweet_points + peanut_butter
        print(f"Cool choices! You selected {first_topping} and {second_topping} to put on your pancakes.")
        global points
        print(f"Do you want to eat this sweet breakfast or start over? You currently have {points} health points.")
        will_eat: str = input(f"Enter \"Eat\" to gain {sweet_points} health points from your dish; enter \"Start over\" to start over. ")
        while will_eat != "Eat" and will_eat != "Start over":
            print("Invalid entry, try again.")
            will_eat: str = input(f"Enter \"Eat\" to gain the {sweet_points} health points of your dish; enter \"Start over\" to start over. ")
        if will_eat == "Eat":
            print(f"Yum! {THUMBS_UP_EMOJI}")
            change_points(points, sweet_points)
            print(f"You have {points} health points! Do you want more pancakes, to eat something else, or to finish eating?")
            next_pancakes: str = input("Type \"Eat more\" to eat more pancakes, \"Something else\" to eat something else, or \"Finish\" to end the game. ")
            while next_pancakes != "Eat more" and next_pancakes != "Something else" and next_pancakes != "Finish":
                print("Invalid entry, try again.")
                next_pancakes: str = input("Type \"Eat more\" to eat more pancakes, \"Something else\" to eat something else, or \"Finish\" to end the game.")
            if next_pancakes != "Eat more":
                eat_more = False
                if next_pancakes == "Something else":
                    from random import randint
                    savory(randint(2, 7))
                else:
                    print(f"Goodbye, {player}!")
        else:
            eat_more = True

    
if __name__ == "__main__":
    main()