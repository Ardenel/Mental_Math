import pytest

from mental_math.calculation_logic import Session


# Checks that check_answer returns True only when the answer matches the stored solution.
@pytest.mark.parametrize(
    "user_answer, expected",
    [
        (4, True),  # correct answer
        (5, False),  # wrong answer
        (0, False),  # edge case: zero is a valid int but wrong here
        (-4, False),  # negative number, opposite of the solution
    ],
)
def test_check_answer(user_answer, expected):
    session = Session(1, ["+"], 1, 10)
    session._current = ("2 + 2", 4)
    assert session.check_answer(user_answer, 1.0) == expected


# Checks that both numbers of every generated question stay within [min, max].
@pytest.mark.parametrize(
    "min, max",
    [
        (1, 10),  # normal positive range
        (-10, 0),  # negative range
        (0, 0),  # single possible value
        (-10000, 10000),  # very large range
    ],
)
def test_numbers_within_bounds(min, max):
    session = Session(100, ["+"], min, max)
    for i in range(100):
        question = session.create_questions().split()
        e1 = int(question[0])
        e2 = int(question[2])
        assert e1 >= min
        assert e1 <= max
        assert e2 >= min
        assert e2 <= max


# Checks that min > max is silently swapped and numbers stay in the corrected range.
def test_min_greater_than_max_is_swapped():
    session = Session(100, ["+"], 1000, 10)
    for _ in range(100):
        a, _op, b = session.create_questions().split()
        assert 10 <= int(a) <= 1000
        assert 10 <= int(b) <= 1000


# Checks that generated questions only use the operators requested.
@pytest.mark.parametrize(
    "ops",
    [
        ["+"],  # addition only
        ["-"],  # subtraction only
        ["*"],  # multiplication only
        ["+", "-", "*"],  # all operators together
    ],
)
def test_valid_operations(ops):
    session = Session(50, ops, 1, 10)
    for _ in range(50):
        question = session.create_questions().split()
        assert question[1] in ops


# Checks that creating a Session with an invalid operator raises a ValueError.
@pytest.mark.parametrize(
    "ops",
    [
        ["/"],  # unsupported operator
        ["0"],  # digit instead of an operator
        ["a"],  # letter instead of an operator
        [""],  # empty string
        ["+", "/"],  # valid operator mixed with an invalid one
    ],
)
def test_invalid_operations(ops):
    with pytest.raises(ValueError):
        Session(1, ops, 1, 10)


# Checks that the stored solution matches the question that was displayed.
def test_stored_answer_match_question():
    session = Session(5, ["+"], 1, 10)

    for i in range(5):
        e1, _op, e2 = session.create_questions().split()
        result = int(e1) + int(e2)
        current = session._current
        assert current is not None
        assert current[1] == result


# Checks that answering before any question was created raises a RuntimeError.
def test_check_answer_before_create_question():
    session = Session(1, ["+"], 1, 10)
    session._current = None
    with pytest.raises(RuntimeError):
        session.check_answer(1, 1.0)


# Checks a full session with only correct answers: not finished until the end, then score is 3.
def test_correct_session_sequence():
    session = Session(3, ["+", "-"], 1, 10)

    for i in range(3):
        assert not session.is_finished()

        session.create_questions()
        current = session._current
        assert current is not None
        session.check_answer(current[1], 1.0)

    assert session.score == 3
    assert session.is_finished()
