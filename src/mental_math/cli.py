import argparse
import time

import mental_math.calculation_logic as calc


def main() -> None:
    # Declare a parser
    parser = argparse.ArgumentParser(
        prog="Mental_Math", description="A simple tool to train Mental Math"
    )
    # Add four arguments to configure the number of questions, the operations type available, the min and max calue of the numbers
    parser.add_argument(
        "-q",
        "--questions",
        type=int,
        action="store",
        default=1,
        help="Enter the number of questions (from 1 to 99)",
    )
    parser.add_argument(
        "-o",
        "--ops",
        "--operations",
        type=str,
        nargs="+",
        choices=["+", "-", "*"],
        action="store",
        default=["+"],
        help="Select the operations type you want (+ - *)",
    )
    parser.add_argument(
        "-mi",
        "--min",
        type=int,
        action="store",
        default=1,
        help="Enter the maximum number value for the calculations",
    )
    parser.add_argument(
        "-ma",
        "--max",
        type=int,
        action="store",
        default=10,
        help="Enter the maximum number value for the calculations",
    )

    args = parser.parse_args()

    # Create a mental math session
    session: calc.Session = calc.Session(args.questions, args.ops, args.min, args.max)
    # While the current number of questions is below the value asked by the user, print the question and get the answer
    while not session.is_finished():
        print(session.create_questions())
        start: float = time.perf_counter()
        answer = ask_int()
        end: float = time.perf_counter()
        # Print correct if correct or False instead
        print(
            "Correct !"
            if session.check_answer(answer, (end - start))
            else "False & 5s penalty"
        )
    print_end_session(session)


# Get the user input
def ask_int() -> int:
    while True:
        # Try to convert the user input as an integer or raise an Exception
        try:
            return int(input())
        except ValueError:
            print("Enter an integer value (or pass the questions writing: pass)")


# Print the end of the sessions
def print_end_session(session: calc.Session):
    total_time: float = session.calculate_time()  # Total time of the session
    time_string: str = ""  # Displayed string for time
    wrong = []  # List of incorrect user answer

    # Check if total time is above a hour, then return the remaining minutes
    if total_time >= 3600:
        hour = int(total_time / 3600)  # ou utiliser math.floor() si besoin
        total_time -= hour * 3600
        time_string += f"{hour}h "
    # Check if total time is above a minute, then return the remaining seconds
    if total_time >= 60:
        minute = int(total_time / 60)
        total_time -= minute * 60
        time_string += f"{minute}m "
    # Check if total time is above a second, then return the remaining time
    if total_time >= 1:
        second = int(total_time)
        total_time -= second
        time_string += f"{second}s "
    # The remaining time is multiply by a thousand to have the millisecond (and avoid having 0.XXX ms)
    time_string += f"{int(total_time * 1000)}ms"

    # Get the result index and the result and add it to the wrong list if user was wrong
    for i, result in enumerate(session.results, start=1):
        if not result.correct:
            wrong.append((i, result))

    # Print the score compared to the actual number of questions, the time and the solution only for the incorrect user answer
    print(f"Score : {session.score}/{len(session.results)}")
    print(f"Time: {time_string}")
    if wrong:
        print("\nSolutions:")
        for number, result in wrong:
            print(f"Question {number}: {result.solution}")


if __name__ == "__main__":
    main()
