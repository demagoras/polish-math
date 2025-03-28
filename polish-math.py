import random

# Dictionary mapping numbers to Polish words
num_to_polish = {
    0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery",
    5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziewięć",
    10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście",
    14: "czternaście", 15: "piętnaście", 16: "szesnaście", 17: "siedemnaście",
    18: "osiemnaście", 19: "dziewiętnaście", 20: "dwadzieścia"
}

# Dictionary mapping operations to their Polish words with lambda functions
operators = {
    "plus": lambda a, b: a + b,
    "minus": lambda a, b: a - b,
    "razy": lambda a, b: a * b
}

# Function to generate a random math problem
def generate_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(list(operators.keys()))
    result = operators[operator](num1, num2)

    # Only convert to Polish if it's in the dictionary
    if result in num_to_polish:
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