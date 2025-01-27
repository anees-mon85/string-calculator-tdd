import re


def extract_numbers(func):
    def wrapper(numbers):
        if not numbers:
            return func([])
        if numbers.startswith("//"):
            match = re.match(r"//(\[.*?\])\n(.*)", numbers)
            if match:
                delimiters, numbers = match.groups()
                delimiters = re.findall(r"\[(.*?)\]", delimiters)
                for delimiter in delimiters:
                    numbers = numbers.replace(delimiter, ",")
            else:
                delimiter, numbers = re.match(r"//(.+)\n(.*)", numbers).groups()
                numbers = numbers.replace(delimiter, ",")
        numbers = numbers.replace("\n", ",")
        nums = [int(n) for n in numbers.split(",")]
        return func(nums)

    return wrapper


@extract_numbers
def add(numbers: str) -> int:
    if not numbers:
        return 0

    negatives = [n for n in numbers if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
    return sum(n for n in numbers if n <= 1000)
