import unittest

# Create a test suite
suite = unittest.TestLoader().discover('.', pattern='*_tests.py')

# Run the test suite
unittest.TextTestRunner().run(suite)
