"""
implement a program that prompts the user for their date of birth in YYYY-MM-DD format 
and then sings prints how old they are in minutes, rounded to the nearest integer, using 
English words instead of numerals, just like the song from Rent, without any and between words. 
Since a user might not know the time at which they were born, assume, for simplicity, that the 
user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also 
midnight. In other words, even if the user runs the program at noon, assume that it’s actually 
midnight, on the same date. 
"""
from datetime import date, datetime, timedelta  # Import necessary libraries
import inflect  # Import inflect library for number-to-word conversion

class AgeCalculator:
    @classmethod  # Declare a class method
    def calculate_age(cls):  # Method to calculate age
        try:
            birth_date_str = input("Date of birth (YYYY-MM-DD): ")  # Prompt user for birth date
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()  # Convert input string to date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")  # Handle invalid date format
            return

        current_date = date.today()  # Get current date
        age = current_date - birth_date  # Calculate age as a timedelta object

        minutes = age.total_seconds() / 60  # Convert age to minutes
        minutes = round(minutes)  # Round minutes to nearest integer

        print(cls.convert_to_words(minutes, "minute"))  # Print age in words

    @staticmethod  # Declare a static method
    def convert_to_words(number, unit):  # Method to convert number to words
        p = inflect.engine()  # Create an instance of the inflect engine

        if number == 1:
            return f"{p.number_to_words(number)} {unit}"  # Return singular form if number is 1
        else:
            return f"{p.number_to_words(number)} {p.plural(unit)}"  # Return plural form for other numbers

if __name__ == "__main__":
    AgeCalculator.calculate_age()  # Call the calculate_age() method from the AgeCalculator class
