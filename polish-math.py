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

# Function to generate a random math problem
def generate_problem() -> tuple[int, int, str, int, str, str, str]:
    # Random numbers between the first and last keys of num_to_polish
    num1 = random.choice(list(num_to_polish.keys()))
    num2 = random.choice(list(num_to_polish.keys()))
    operator = random.choice(list(operators.keys()))
    result = operators[operator](num1, num2)

    # Check if the result is within the valid range of known Polish words
    if min(num_to_polish) <= result <= max(num_to_polish):
        num1_polish = num_to_polish[num1]
        num2_polish = num_to_polish[num2]
        result_polish = num_to_polish[result]
    else:
        return generate_problem()

    return num1, num2, operator, result, num1_polish, num2_polish, result_polish

# Main loop for the quiz
while True:
    num1, num2, operator, result, num1_polish, num2_polish, result_polish = generate_problem()

    user_input = input(f"Ile to {num1_polish} {operator} {num2_polish}? ").strip().lower()

    if user_input == result_polish:
        print("Dobrze!")
    elif user_input == "koniec": # This Polish word means "end"
        break
    else:
        print("\n**** Źle! ****")
        print(f"Poprawna odpowiedź to: {result_polish} ({num1} {operator} {num2} = {result})")
        print("***************\n")