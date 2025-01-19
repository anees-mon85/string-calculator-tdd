import re


def add(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiter, numbers = re.match(r"//(.+)\n(.*)", numbers).groups()
        numbers = numbers.replace(delimiter, ",")
    numbers = numbers.replace("\n", ",")
    return sum(map(int, numbers.split(",")))
