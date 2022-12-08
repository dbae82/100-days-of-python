# 1. Create a greeting for your program.
# 2. Ask the user for the city they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line.

greeting = "Welcome to the Band Name Generator"
question1 = "What's the name of the city you grew up in?\n"
question2 = "What's your pet's name?\n"

print(greeting)

city = input(question1)
pet = input(question2)

print("Your band name could be " + city + " " + pet)