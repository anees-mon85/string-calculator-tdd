def add(numbers: str) -> int:
    if not numbers:
        return 0
    numbers = numbers.replace("\n", ",")
    return sum(map(int, numbers.split(",")))
