from dataclasses import dataclass
from random import randint,choice


@dataclass
class Result:
    question : str
    answer : int 
    correct : bool
    


class Session:
    score : int = 0

    def __init__(self, nb_questions: int, operations: list[str], min: int, max: int) -> None:
        self.nb_questions : int = nb_questions
        self.operations : list[str] = operations
        self.min : int = min
        self.max : int = max
        self.results : list[Result] = []
        self._current : tuple[str, int] | None = None

    def create_questions(self) -> str | None:
        e1 : int = randint (self.min, self.max)
        e2 : int = randint (self.min, self.max)
        op : str = choice(self.operations)

        answer : int = 0
        question : str = str(e1) +" "+ str(op)+" "+ str(e2)

        if op == "+":
            answer = e1 + e2
        elif op == "-":
            answer = e1 - e2
        elif op == "*":
            answer = e1 * e2
        
        self._current = (question, answer)
        return question

        # Raise an exception in case of unadmitted operations

    def is_finished(self) -> bool:
        return len(self.results) >= self.nb_questions

    def check_answer(self, user_anwser : int) -> bool:
        if self._current is None:
            raise RuntimeError(f"")
        
        question, answer = self._current
        is_correct : bool = user_anwser == answer
        
        self.results.append(Result(question, user_anwser, is_correct))

        if is_correct:
            self.score += 1
        
        return is_correct