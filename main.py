# import unittest
#
# # Create a test suite
# suite = unittest.TestLoader().discover('.', pattern='*_tests.py')
#
# # Run the test suite
# unittest.TextTestRunner().run(suite)


import subprocess

# List of your test files
test_files = [
    "new_customer_tests.py",
    "new_account_tests.py",
    "deposit_tests.py",
    "withdraw_tests.py",
    "transfer_tests.py",
    "customized_transaction_tests.py",
    "logout_tests.py",
    # Add other test files as needed
]


# Function to run each test file
def run_tests():
    for test_file in test_files:
        print(f"Running {test_file}...")
        # Run the test file and capture the output
        result = subprocess.run(["python", test_file], capture_output=True, text=True)

        # Print the output of the test run
        print(result.stdout)
        if result.stderr:
            print(f"Error in {test_file}:")
            print(result.stderr)


if __name__ == "__main__":
    run_tests()
