
# Your task is to filter out every heading (i.e., Foundations, Relationship to statistics etc.) using a regular expression. To do so, please complement the below function, which should return a list of strings that contains the different headings as elements.
# You can identify the headings by using the leading and ending '==.'
# Design a regex-pattern with three groups, where groups one and three capture the '==' and group 2 captures the heading itself

import re

with open("data/practice.txt", "r") as file:
    wikipedia_article = file.read()
# INSPECT TEXT HERE.
# print(wikipedia_article)


def answer():
    # START YOUR CODE HERE.
    pattern = re.compile(r'(==|===)\s(([A-Za-z]+\s*)+)(==|===)', re.I)
    matches = pattern.finditer(wikipedia_article)
    match_list = list()
    for match in matches:
        match_list.append(match.group(2).strip())
    # RETURN YOUR ANSWER HERE.
    return match_list


# Checking Solution
assert type(answer()) == type([]), "Please return a list!"
assert type(answer()[0]) == type(
    str()), "The returned list should contain strings as elements!"
assert len(answer()) == 10, "Your results seem to be incomplete!"
assert "Foundations" in answer(), "Your results seem to be incomplete!"
assert "Modern usage" in answer(), "Your results seem to be incomplete!"
