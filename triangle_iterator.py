from typing import Iterator

# сделать итератор, который возвращает итераторы, которые генерируют числовые последовательности 1,2,3,...
# есть внешний итератор, который генерирует вложенные итераторы
# каждый следующий вложенный итератор генерирует последовательность длинны равной индексу этого итератора
# т.е. если переделать итераторы в списки, то получится такой двумерный список

l = [
    [],  # inner iterator number 1
    [1],  # inner iterator number 2
    [1, 2],  # inner iterator number 3
    [1, 2, 3],  # inner iterator number 4
    # ... and so on
]


# `count` is the number of iterators to generate, None for infinite number.
def triangle(count: int = None) -> Iterator[range]:
    """Generates a sequence of iterators of number of increasing length."""
    outer = 1
    while count is None or outer <= count:
        yield range(1, outer)
        outer += 1


list_compr = [list(inner_iterator) for inner_iterator in triangle(5)]
