import re


def extract_mul(pattern, string_input):
    """Calculate sum of muliplications in "mul(x,y)" matches.

    Args:
        pattern (re.compile pattern): compiled "mul(x,y)" pattern
        string_input (str): string to study
    """
    out = 0
    match = re.findall(pattern, string_input)

    for entry in match:
        numbers = list(map(int, entry[4:-1].split(",")))
        out += numbers[0] * numbers[1]

    return out


# Challenge 1
# identify mul(*,*) in the string and ignore everything else
# sum up all multiplication results

pattern_challenge_1 = re.compile(r"mul\(\d+,\d+\)")
entire_str = ""

with open("Day_3_input.txt") as f:
    for line in f:
        entire_str += line.strip()

print(extract_mul(pattern_challenge_1, entire_str))


# Challenge 2
# 1. find substrings starting with "do()" and stopping with "don't()"
# 2. until the first "do()", mul() is enabled

pattern_2 = re.compile(r"do\(\).*?don't\(\)")
pattern_do = re.compile(r"do\(\)")
pattern_dont = re.compile(r"don't\(\)")

match_iterator = re.finditer(pattern_2, entire_str)
output_challenge_2 = 0
search_on = True
start = True
k = 0

while search_on:
    # look at start before the first "do()"
    if start:
        match_do = re.search(pattern_do, entire_str)
        match_dont = re.search(pattern_dont, entire_str)

        if match_do.span()[0] < match_dont.span()[0]:
            first_str = entire_str[: match_do.span()[0]]
        else:
            first_str = entire_str[: match_dont.span()[0]]

        output_challenge_2 += extract_mul(pattern_challenge_1, first_str)
        start = False

    match_do = re.search(pattern_do, entire_str)
    entire_str = entire_str[match_do.span()[0] :]
    match_dont = re.search(pattern_dont, entire_str)

    # look at the end after last "don't()"
    if match_dont is None:
        last_str = entire_str
        output_challenge_2 += extract_mul(pattern_challenge_1, last_str)
        search_on = False
        break

    else:
        # calculate sums between "do()"" and "don't()"
        sub_str = entire_str[: match_dont.span()[1]]
        output_challenge_2 += extract_mul(pattern_challenge_1, sub_str)
        entire_str = entire_str[match_dont.span()[1] + 1 :]

print(output_challenge_2)
