# Autotests for Alphabetical Counting Lab

import pytest
from Lab import count_words

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_number(string):
    clean_list = [x for x in string.split(" ") if len(x) > 0]
    return clean_list[1]

def get_line(string, letter):
    start = string.find(letter)
    if start < 0:
        return None
    end = string.find("\n", start)
    return string[start:end]

def test_letter_counts(capsys):
    count_words()
    captured = capsys.readouterr().out

    letters = ["A", "C", "S", "V", "X", "Z"]
    counts = ["7,152", "11,790", "14,122", "2,176", "90", "422"]

    for let, c in zip(letters, counts):
        let_pos = captured.find(let)
        assert let_pos >= 0, f"I'm not seeing the letter {let} in your printout. Did you capitalize it?"
        line_break = captured.find("\n", let_pos)
        line = captured[let_pos:line_break]
        num = get_number(line)
        if len(c) > 3:
            assert num.find(",") >= 0, f"{num} is large enough it should have a comma in it. Did you forget it?"
        assert num == c, f"The correct count for {let} should be {c} but you printed {num}."
   
def test_consistent_formatting(capsys):
    count_words()
    captured = capsys.readouterr().out

    A_line = get_line(captured, "A")
    for letter in alphabet:
        line = get_line(captured, letter)
        assert len(A_line) == len(line), f"The formatting on the {letter} line seems to diverge from the other lines."

