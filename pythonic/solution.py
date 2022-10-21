from pickle import NONE


def print_indices_and_elements(elements) -> None:
    for count, element in enumerate(elements):
        print(count,element)

def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [x for x in list(range(start,end+1)) if x % 2 == False]


def get_char_set_from(s: str) -> set[str]:
    return {l for l in s}


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {n: (n**(1/2)) for n in range(start,end+1) if int(n**(1/2)+0.5)**2 == n }


def filter_even_from(numbers: list[int]) -> list[int]:
    return [x for x in numbers if x % 2 == False]


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1

def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [-1 if x%2==1 else x for x in numbers if x%5==0]

def str_lengths(strings: list[str]) -> list[int]:
    return [len(i) for i in strings]

def get_fibonacci_type(version: int) -> str:
    if version == 1:
        return 'generator'
    elif version == 2:
        return 'list'

def difference_between_fibonacci1_and_fibonacci2() -> str:
    return 'The Generator version is more efficient as it does not to store all the values in memory, On the other hand, in the list version, can be accessed in the memory and even reused.'



class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        # You can add more code here if you need
        self.iter = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.iter >= len(self.elements):
            raise StopIteration
        else:
            self.iter += 2
            return self.elements[self.iter-2]

def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    return (e1+e2+sum(others))/(2+len(others))


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    c = {**a, **b}
    d = {**b, **a}
    
    return sorted([k for k, vc in c.items() if vc != d[k]])


def print_out_in(*numbers) -> None:

    while len(numbers) > 1:
        a = numbers[0], numbers[-1]
        b,c = a
        print(b, c)
        numbers = numbers[1:-1]

    if numbers:
        print(numbers[0])
       


def append_range(start: int, end: int, step: int=1, to = None) -> list[int]:
    # You may add code here
    if to is None:
        to = []
    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value) -> bool:
    return value is None
