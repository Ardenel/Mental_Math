# Mental_Math

**This is a Python project to train mental math**

## Requirements

Python 3.12 or higher.

## How to use

1. Clone the project on your computer

2. Create a venv: `python3 -m venv .venv` and activate it: `source .venv/bin/activate`

3. Install the project as editable: `pip install -e ".[dev]"`

4. Start the program with: `mentalmath` and the following options:
    - `-q / --questions X` - Replace X with the desired number of questions (*Default value: 1*)
    - `-o / --operations + - '*'` - You can enter one, two or three values between + , - and '*' (The '' are mandatory for the multiply) (*Default value: +*)
    - `-mi / --min X` - Replace X with the minimum possible value for the calculations (*Default value: 1*)
    - `-ma / --max X` - Replace X with the maximum possible value for the calculations (*Default value: 10*)

    *Exemple: `mentalmath -q 10 -o + - '*' -mi -10 -ma 10`*

5. A first question is displayed in the console, answer it as fast as possible, then the next one, and so on

6. Be careful, each wrong answer add 5 seconds penalty to your final time

7. At the end of your session, your score and time are displayed, as well as the solutions of your wrong answers


**Enjoy your brain training !**