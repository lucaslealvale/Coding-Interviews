def print_indices_and_elements(elements) -> None:
    for count, element in enumerate(elements):
        print(count,element)

def get_even_numbers_between(start: int, end: int) -> list[int]:
    #newlist = [expression for item in iterable if condition == True]
    #andrew this wrong?
    return [x for x in list(range(start,end+1)) if x % 2 == False]


def get_char_set_from(s: str) -> set[str]:
    #this test is failing
    return {l for l in s}


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {n: (n**(1/2)) for n in range(start,end+1) if int(n**(1/2)+0.5)**2 == n }


def filter_even_from(numbers: list[int]) -> list[int]:
    return [x for x in numbers if x % 2 == False]


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1

def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    # a list comprehension that returns a list of numbers that are multiples of 5
    return [-1 if x%2==1 else x for x in numbers if x%5==0]

def str_lengths(strings: list[str]) -> list[int]:
    return []

def get_fibonacci_type(version: int) -> str:
    return ''

def difference_between_fibonacci1_and_fibonacci2() -> str:
    return ''


class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        # You can add more code here if you need


def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    return -1


def keys_with_different_value() -> list[int]:
    return []


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        # You should add code here and remove the break
        break

    if numbers:
        # You should add code here
        pass


def append_range(start: int, end: int, step: int=1, to: list[int]=[]):
    # You may add code here

    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value == None
