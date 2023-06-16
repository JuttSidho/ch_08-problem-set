import unittest
from jar import Jar  # Import the Jar class from the jar module

class JarTest(unittest.TestCase):
    def test_init(self):
        jar = Jar(10)  # Create a Jar object with capacity of 10
        self.assertEqual(jar.capacity, 10)  # Check if capacity is set correctly
        self.assertEqual(jar.cookies, 0)  # Check if initial number of cookies is 0

        with self.assertRaises(ValueError):
            Jar("capacity")  # Test initialization with invalid capacity (not an int)
        with self.assertRaises(ValueError):
            Jar(-5)  # Test initialization with invalid capacity (negative number)

    def test_str(self):
        jar = Jar(5)  # Create a Jar object with capacity of 5
        jar.cookies = 3  # Set the number of cookies in the jar to 3
        self.assertEqual(str(jar), "🍪🍪🍪")  # Check if str representation is correct

        jar.cookies = 0  # Set the number of cookies in the jar to 0
        self.assertEqual(str(jar), "")  # Check if str representation is correct for empty jar

    def test_deposit(self):
        jar = Jar(5)  # Create a Jar object with capacity of 5
        jar.deposit(3)  # Deposit 3 cookies into the jar
        self.assertEqual(jar.cookies, 3)  # Check if the number of cookies is updated correctly

        with self.assertRaises(ValueError):
            jar.deposit("cookies")  # Test deposit with invalid input (not an int)
        with self.assertRaises(ValueError):
            jar.deposit(-2)  # Test deposit with negative number of cookies
        with self.assertRaises(ValueError):
            jar.deposit(5)  # Test deposit that exceeds the jar's capacity

    def test_withdraw(self):
        jar = Jar(5)  # Create a Jar object with capacity of 5
        jar.cookies = 4  # Set the number of cookies in the jar to 4
        jar.withdraw(2)  # Withdraw 2 cookies from the jar
        self.assertEqual(jar.cookies, 2)  # Check if the number of cookies is updated correctly

        with self.assertRaises(ValueError):
            jar.withdraw("cookies")  # Test withdraw with invalid input (not an int)
        with self.assertRaises(ValueError):
            jar.withdraw(-2)  # Test withdraw with negative number of cookies
        with self.assertRaises(ValueError):
            jar.withdraw(3)  # Test withdraw that exceeds the number of cookies in the jar

    def test_capacity(self):
        jar = Jar(7)  # Create a Jar object with capacity of 7
        self.assertEqual(jar.capacity(), 7)  # Check if the capacity method returns the correct value

    def test_size(self):
        jar = Jar(5)  # Create a Jar object with capacity of 5
        jar.cookies = 3  # Set the number of cookies in the jar to 3
        self.assertEqual(jar.size(), 3)  # Check if the size method returns the correct value

if __name__ == '__main__':
    unittest.main()  # Run the tests using the unittest framework
