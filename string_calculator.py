import re


def extract_numbers(numbers: str) -> list[int]:
    if numbers.startswith("//"):
        match = re.match(r"//\[(.+)\]\n(.*)", numbers)
        if match:
            delimiter, numbers = match.groups()
        else:
            delimiter, numbers = re.match(r"//(.+)\n(.*)", numbers).groups()
        numbers = numbers.replace(delimiter, ",")
    numbers = numbers.replace("\n", ",")
    return [int(n) for n in numbers.split(",")]


def add(numbers: str) -> int:
    if not numbers:
        return 0

    nums = extract_numbers(numbers)
    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
    return sum(n for n in nums if n <= 1000)
