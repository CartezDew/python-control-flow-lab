# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()
    if letter in "aeiou":
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

# Call the function
check_letter()

def check_voting_eligibility():
    try:
        # Prompt the user for their age
        age = int(input("Please enter your age: "))
        
        # Validate age is not negative
        if age < 0:
            print("Invalid age. Age cannot be negative.")
            return  # Exit the function early
        
        # Set the voting age
        voting_age = 18
        
        # Check eligibility
        if age >= voting_age:
            print("You are eligible to vote!")
        else:
            print("You are not eligible to vote yet.")
    
    except ValueError:
        # Handles if user inputs something that isn't a number
        print("Invalid input. Please enter a valid number for your age.")

# Call the function
check_voting_eligibility()

def calculate_dog_years():
    try:
        # Prompt the user for the dog's age
        dog_age = int(input("Input a dog's age: "))
        
        # Validate the dog's age (can't be negative)
        if dog_age < 0:
            print("Invalid age. Age cannot be negative.")
            return
        
        # Calculate dog years
        if dog_age <= 2:
            dog_years = dog_age * 10
        else:
            dog_years = 20 + (dog_age - 2) * 7
        
        # Print the result
        print(f"The dog's age in dog years is {dog_years}.")
    
    except ValueError:
        # Handle if the input is not a valid integer
        print("Invalid input. Please enter a valid number.")

# Call the function
calculate_dog_years()

def weather_advice():
    # Ask the user if it is cold
    cold_input = input("Is it cold? (yes/no): ").strip().lower()
    # Ask the user if it is raining
    raining_input = input("Is it raining? (yes/no): ").strip().lower()

    # Convert responses to boolean values
    is_cold = cold_input == "yes"
    is_raining = raining_input == "yes"

    # Provide advice based on conditions
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    elif not is_cold and not is_raining:
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

# Call the function
weather_advice()

def determine_season():
    # Define the valid months in order
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    # Prompt for month
    month = input("Enter the month of the year (Jan - Dec): ").strip().title()
    
    # Validate month input
    if month not in months:
        print("Invalid month. Please enter a valid month abbreviation (e.g., Jan, Feb, Mar).")
        return

    # Prompt for day
    try:
        day = int(input("Enter the day of the month: "))
    except ValueError:
        print("Invalid day. Please enter a number.")
        return

    # Now determine the season
    if (month == "Dec" and day >= 21) or month in ("Jan", "Feb") or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or month in ("Apr", "May") or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or month in ("Jul", "Aug") or (month == "Sep" and day <= 21):
        season = "Summer"
    elif (month == "Sep" and day >= 22) or month in ("Oct", "Nov") or (month == "Dec" and day <= 20):
        season = "Fall"
    else:
        print("Invalid day for the given month.")
        return

    # Print result
    print(f"{month} {day} is in {season}.")

# Call the function
determine_season()
