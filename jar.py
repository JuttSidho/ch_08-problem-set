"""
Suppose that you’d like to implement a cookie jar in which to store cookies. 
In a file called jar.py, implement a class called Jar with these methods:

__init__ should initialize a cookie jar with the given capacity, which 
represents the maximum number of cookies that can fit in the cookie jar. 
If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
__str__ should return a str with 
 🍪, where 
 is the number of cookies in the cookie jar. For instance, if there are 3 
 cookies in the cookie jar, then str should return "🍪🍪🍪"
deposit should add n cookies to the cookie jar. If adding that many would exceed 
the cookie jar’s capacity, though, deposit should instead raise a ValueError.
withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t 
that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
capacity should return the cookie jar’s capacity.
size should return the number of cookies actually in the cookie jar.
"""
class Jar:
    def __init__(self, capacity):
        # Constructor method to initialize the cookie jar with a given capacity
        if not isinstance(capacity, int) or capacity < 0:
            # Check if the capacity is a non-negative integer, raise ValueError if not
            raise ValueError("Capacity must be a non-negative integer.")
        
        self.capacity = capacity
        self.cookies = 0
        # Initialize the instance variables: capacity represents the maximum number of cookies that can fit in the jar,
        # and cookies represents the current number of cookies in the jar

    def __str__(self):
        # String representation of the cookie jar
        return "🍪" * self.cookies
        # Return a string with the cookie emoji repeated self.cookies times, representing the number of cookies in the jar

    def deposit(self, n):
        # Method to add n cookies to the jar
        if not isinstance(n, int) or n < 0:
            # Check if the number of cookies to be deposited is a non-negative integer, raise ValueError if not
            raise ValueError("Number of cookies to deposit must be a non-negative integer.")
        
        if self.cookies + n > self.capacity:
            # Check if adding n cookies would exceed the jar's capacity, raise ValueError if so
            raise ValueError("Cookie jar capacity exceeded.")
        
        self.cookies += n
        # Increment the number of cookies in the jar by n

    def withdraw(self, n):
        # Method to remove n cookies from the jar
        if not isinstance(n, int) or n < 0:
            # Check if the number of cookies to be withdrawn is a non-negative integer, raise ValueError if not
            raise ValueError("Number of cookies to withdraw must be a non-negative integer.")
        
        if n > self.cookies:
            # Check if there are enough cookies in the jar to withdraw, raise ValueError if not
            raise ValueError("Not enough cookies in the jar.")
        
        self.cookies -= n
        # Decrement the number of cookies in the jar by n

    def capacity(self):
        # Method to get the jar's capacity
        return self.capacity
        # Return the capacity of the jar

    def size(self):
        # Method to get the number of cookies in the jar
        return self.cookies
        # Return the current number of cookies in the jar
