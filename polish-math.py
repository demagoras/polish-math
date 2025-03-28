import random
from typing import Callable

# Dictionary mapping numbers to Polish words
num_to_polish: dict[int, str] = {
    1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery",
    5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziewięć",
    10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście",
    14: "czternaście", 15: "piętnaście", 16: "szesnaście", 17: "siedemnaście",
    18: "osiemnaście", 19: "dziewiętnaście", 20: "dwadzieścia",
    30: "trzydzieści", 40: "czterdzieści", 50: "pięćdziesiąt",
    60: "sześćdziesiąt", 70: "siedemdziesiąt", 80: "osiemdziesiąt",
    90: "dziewięćdziesiąt", 100: "sto",
}

# Extend the dictionary for numbers 21-99 dynamically
num_to_polish.update({
    tens + ones: num_to_polish[tens] + " " + num_to_polish[ones]
    for tens in range(20, 100, 10) for ones in range(1, 10)
})

# Dictionary mapping operations to their Polish words with lambda functions
operators: dict[str, Callable[[int, int], int]] = {
    "plus": lambda a, b: a + b,
    "minus": lambda a, b: a - b,
    "razy": lambda a, b: a * b
}

def choose_difficulty() -> int:
    while True:
        try:
            max_num = int(input(f"Enter a number between {min(num_to_polish)} and {max(num_to_polish)}: ").strip())
            # Check if the number is within the valid range of num_to_polish
            if max_num < min(num_to_polish) or max_num > max(num_to_polish):
                print("Number must be between 1 and 100.")
                continue
            return max_num
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
# Function to generate a random math problem
def generate_problem(max_num: int) -> tuple[int, int, str, int, str, str, str]:
    while True:
        # Random numbers between the first and last keys of num_to_polish
        num1: int = random.randint(min(num_to_polish), max_num)
        num2: int = random.randint(min(num_to_polish), max_num)
        operator: str = random.choice(list(operators.keys()))
        result: int = operators[operator](num1, num2)

        # Check if the result is within the valid range of known Polish words
        if min(num_to_polish) <= result <= max_num:
            num1_polish: str = num_to_polish[num1]
            num2_polish: str = num_to_polish[num2]
            result_polish: str = num_to_polish[result]
            
            return num1, num2, operator, result, num1_polish, num2_polish, result_polish

# Function to start the quiz
def start_quiz() -> None:
    max_num: int = choose_difficulty()
    while True:
        # Generate a random math problem
        num1, num2, operator, result, num1_polish, num2_polish, result_polish = generate_problem(max_num)

        # Display the problem in Polish
        user_input = input(f"Ile to {num1_polish} {operator} {num2_polish}? ").strip().lower()

        # Check if the user input is correct or if they want to end the quiz
        if user_input == result_polish:
            print("Dobrze!")
        elif user_input == "koniec": # This Polish word means "end"
            break
        else:
            print("\n**** Źle! ****")
            print(f"Poprawna odpowiedź to: {result_polish} ({num1} {operator} {num2} = {result})")
            print("***************\n")

start_quiz()