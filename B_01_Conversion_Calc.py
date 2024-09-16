distance_dict = {
    "centimetre": 100,
    "millimetre": 1000,
    "kilometre": 0.001,
    "metre": 1
}
mass_dict = {
    "milligram": 1000,
    "kilogram": 0.001,
    "gram": 1,
    "tonne": 0.000001
}
time_dict = {
    "day": 1,
    "minute": 1440,
    "second": 86400,
    "hour": 24,
    "week": ""
}
volume_dict = {
    "millilitre": 1000,
    "kilolitre": 0.001,
    "litre": 1
}

distance_measurements = ["m","cm","km","i"]
time_measurements = []

# generates headings (e.g: ----- Heading ----- )
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# displays instructions
def instructions():
    statement_generator(statement="Instructions", decoration="♦")
    print('''WELCOME TO THE ULTIMATE CONVERSION CALCULATOR.
- First type in the unit of measurement you'd like to convert, (days,metres,kilograms, etc)
- Next type in the second unit that you would like the converted result to be.
- Lastly type in how much of the first unit you are converting.''')


def float_check(question):

    error = f"please input a float number that is larger than zero."

    while True:

        response = input(question)
        if response == "xxx":
            return response
        try:
            # ask user for a number
            response = float(response)
            if response <= 0:
                print(error)
            else:
                return response
        # checks that number is valid
        except ValueError:
            print(error)


def get_unit_of_measurement(order):
    while True:
        response = input(f"{order} unit of Measurement: ").lower()

        # check for 'm' or the exit code
        if response == "xxx":
            print("Thank you for using the conversion calculator")
            return response
        elif response == "m":
            return response

        elif response in ["metre", "metres"]:
            return "metre"

        elif response in ["mm", "millimetres", "millimetre"]:
            return "millimetre"

        elif response in ["km", "kilometres", "kilometre"]:
            return "kilometre"

        elif response in ["cm", "centimetres", "centimetre"]:
            return "centimetre"

        elif response in ['hr', "hour", "hours"]:
            return "hour"

        elif response in ['minute', "minutes"]:
            return "minute"

        elif response in ["weeks", "week"]:
            return "week"

        elif response in ["second", "seconds", "s"]:
            return "second"

        elif response in ['days', 'day']:
            return "day"

        elif response in ['gram', 'grams', 'g']:
            return "gram"

        elif response in ['kilogram', 'kilograms', 'kg']:
            return "kilogram"

        elif response in ['kilolitre', 'kilolitres', 'kl']:
            return "kilolitre"

        elif response in ['millilitre', 'millilitres', 'ml']:
            return "millilitre"

        elif response in ['litre', 'litres', 'l']:
            return "litre"

        elif response in ['tonne', 'tonnes']:
            return "tonne"
        # if response invalid output error
        else:
            print("Please enter a valid unit of measurement")


# check if the response I is an image or an integer
def measurementcheck(unit):
    correct_file = input('''Press 1 to select metre, 2 to select milimetre 
or 3 to select minutes as your unit of measurement.''')
    if correct_file == "1":
        response = "metre"
    elif correct_file == "2":
        response = "millimetre"
    elif correct_file == "3":
        response = "minute"
    return response


def conversioncheck(unit):
    if unit in distance_dict:
        response = distance_dict
    elif unit in time_dict:
        response = time_dict
    elif unit in mass_dict:
        response = mass_dict
    elif unit in volume_dict:
        response = volume_dict

    return response


def convert(measurementdict, unit2, unit1):
    # multiply to get standard value
    multiply_by = measurementdict[unit2]
    standard = amount * multiply_by

    # divide to get desired value
    divide_by = measurementdict[unit1]
    response = standard / divide_by

    response = round(response, 12)

    return response

# main routine goes here

# asks if the user wants to see the instructions
want_instructions = input("\nPress <enter> to read the instructions or any key to continue ")

# if they press enter without typing anything extra, display instructions
if want_instructions == "":
    instructions()

print("\n")
while True:
    second_unit = ""
    first_unit = get_unit_of_measurement(order="First")
    if first_unit == "m":
        first_unit = measurementcheck(first_unit)
    elif first_unit == "xxx":
        break
    conversion = conversioncheck(first_unit)

    print(f"First unit of measurement selected is {first_unit}")

    while second_unit not in conversion:
        second_unit = get_unit_of_measurement(order="Second")
        if second_unit == "m":
            second_unit = measurementcheck(second_unit)
        if second_unit == first_unit:
            print("You cant convert the same unit to itself. ")
        if second_unit not in conversion:
            print(f"Your first unit of measurement ({first_unit}s) can not be converted to this.")
    print(f"Second unit of measurement selected is {second_unit}")
    amount = float_check(f"Number of {first_unit}s to convert to {second_unit}s: ")
    if amount == "xxx":
        print("Thank you for using the conversion calculator")
        break
    answer = convert(conversion, second_unit, first_unit)
    print(f"{amount} {first_unit}s is equal to {answer} {second_unit}s!\n")