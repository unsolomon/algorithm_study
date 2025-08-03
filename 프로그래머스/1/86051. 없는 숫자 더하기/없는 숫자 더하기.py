def solution(numbers):
    # 0~9 전체 집합
    all_numbers = set(range(10))

    given_numbers = set(numbers)

    missing_numbers = all_numbers - given_numbers

    return sum(missing_numbers)
