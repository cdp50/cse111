# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter you gender (M or F): ")
    birthdate = input("Enter your birthdate (yyyy-MM-DD): ")
    weight = float(input("Enter your weight in U.S. pounds: "))
    height = float(input("Enter your height in U.S. inches: "))


    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthdate)
    lbtokg = kg_from_lb(weight)
    intocm = cm_from_in(height)
    bmi = body_mass_index(lbtokg,intocm)
    bmr = basal_metabolic_rate(gender, lbtokg, intocm, age)

    # Print the results for the user to see.
    print(f"Age (years): {age}")
    print(f"Weight (kg): {round(lbtokg,2)}")
    print(f"Height (cm): {round(intocm,1)}")
    print(f"Body mass intex: {round(bmi,1)}")
    print(f"Basal metabolic rate (kcal/day): {bmr}")
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = pounds * 0.45359237
    return kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = inches * 2.54
    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / height ** 2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    women = int(447.593 + 9.247 * weight + 3.098 * height - 4.330 * age)
    men = int(88.362 + 13.397 * weight + 4.799 * height - 5.677 * age)
    if gender == "f" or gender == "F":
        return women
    elif gender == "m" or gender == "M":
        return men
    else: return "Sorry you have to write gender by writing m or f you can also try with M or F"


# Call the main function so that
# this program will start executing.
main()                        