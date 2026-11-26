from dataclasses import dataclass
from random import choice, randint


VALID_OPERATIONS = {"+", "-", "*"}


# A dataclass used to create the list of questions with the current calculation, the user input, the time to answer, if the user was right
@dataclass
class Result:
    question: str
    solution: int
    user_answer: int
    time: float
    correct: bool


# A class for the current session
class Session:
    # Set the score value to 0
    score: int = 0

    # Constructor of the class
    def __init__(
        self, nb_questions: int, operations: list[str], min: int, max: int
    ) -> None:
        if min > max:
            min, max = max, min

        if not operations or any(op not in VALID_OPERATIONS for op in operations):
            raise ValueError(f"Wrong operators given: {operations}")

        self.nb_questions: int = nb_questions
        self.operations = operations
        self.min: int = min
        self.max: int = max
        self.results: list[Result] = []
        self._current: tuple[str, int] | None = None

    # Create a new question and calculate its answer, store both in self._current and return the question string to the cli file
    def create_questions(self) -> str:
        # Get an integer between the min and max set by the user
        e1: int = randint(self.min, self.max)
        e2: int = randint(self.min, self.max)
        # Get a operation marker from the list provide by the user
        op: str = choice(self.operations)

        answer: int = 0
        # Transform and store as string the variables above
        question: str = str(e1) + " " + str(op) + " " + str(e2)

        # Select the correct calculation depening on the operation marker
        if op == "+":
            answer = e1 + e2
        elif op == "-":
            answer = e1 - e2
        elif op == "*":
            answer = e1 * e2

        self._current = (question, answer)
        return question

        # Reminder - Raise an exception in case of unadmitted operations

    # Check if the current number of question exceeds the number provided by the user and return it as a boolean
    def is_finished(self) -> bool:
        return len(self.results) >= self.nb_questions

    # Check if the user input is equal to the question answer and return it as a boolean
    def check_answer(self, user_anwser: int, question_time: float) -> bool:
        # If the program check a user input before a question were asked, raise an exception
        if self._current is None:
            raise RuntimeError(f"")

        question, answer = self._current
        is_correct: bool = user_anwser == answer
        real_question_time: float = question_time

        # If user answer wrong, add 5 seconds penalty
        if not is_correct:
            real_question_time += 5
        else:  # Increase score value if the user answer was correct
            self.score += 1

        # Add the result of this question to the list of existing questions
        self.results.append(
            Result(question, answer, user_anwser, real_question_time, is_correct)
        )

        return is_correct

    # Calculate the total time of the session
    def calculate_time(self) -> float:
        total_time: float = 0
        for result in self.results:
            total_time += result.time
        mean_time: float = total_time / len(
            self.results
        )  # Useless for now but might be used later
        return total_time
