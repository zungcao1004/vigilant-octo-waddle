# How to Use

This project contains automated tests using Selenium. Follow the steps below to set up your environment and run the tests.

## Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Steps

### 1. Clone the repository

Open your terminal and clone the repository:

```
git clone https://github.com/zungcao1004/vigilant-octo-waddle.git
cd vigilant-octo-waddle/
```

### 2. Create a virtual environment
Create a virtual environment to isolate your project dependencies:

```
python -m venv venv
```

### 3. Activate the virtual environment

* On Windows:
```
venv\Scripts\activate
```

* On macOS/Linux:
```
source venv/bin/activate
```

### 4. Install requirements

Install the required packages using the `requirements.txt` file:
```
pip install -r requirements.txt
```

### 5. Run the tests

Run all the test files using the following command:
```
python -m unittest discover -s tests -p "*.py"
```

### 6. Deactivate the Virtual Environment (Optional)

After you’re done, you can deactivate the virtual environment:
```
deactivate
```
