def add(numbers: str) -> int:
    if not numbers:
        return 0
    return sum(map(int, numbers.split(",")))
