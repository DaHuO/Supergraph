'''
CodeJam 2016:
    Problem B. Revenge of the Pancakes
'''


class BancakeDish:

    def __init__(self, bancakes, number_of_flips=0):
        self.bancakes = bancakes
        self.number_of_bancakes = len(self.bancakes)
        self.number_of_flips = number_of_flips  # incase the dish had already been flipped when created

    def is_all_happy(self):
        return set(self.bancakes) == set(['+'])

    def is_all_sameside(self):
        return len(set(self.bancakes)) == 1

    def get_other_side(self, bancake):
        if bancake == '-':
            return '+'
        return '-'

    def flip_bancakes(self, depth):
        bancakes = self._flip_bancakes(self.bancakes[:depth]) + self.bancakes[depth:]
        return BancakeDish(bancakes, self.number_of_flips + 1)

    def _flip_bancakes(self, bancakes):
        return ''.join(map(self.get_other_side, list(bancakes)))

    def __str__(self):
        return self.bancakes


class Waiter:
    def __init__(self, bancakes=''):
        self.initial_dish = BancakeDish(bancakes)
        self.visited = set()

    def flip_dish_in_all_possible_levels(self, dish):
        new_dishes = map(dish.flip_bancakes, range(1, dish.number_of_bancakes + 1))
        new_unique_dishes = []

        for dish in new_dishes:
            if str(dish) not in self.visited:
                new_unique_dishes.append(dish)
                self.visited.add(str(dish))
        return new_unique_dishes

    def min_number_of_flips(self):
        '''returns minimum number of flips required to make all happy faces top'''
        queue = [self.initial_dish, ]
        while queue:
            dish = queue.pop()
            if dish.is_all_happy():
                return dish.number_of_flips
            else:
                queue = list(self.flip_dish_in_all_possible_levels(dish)) + queue


with open('B-small-attempt1.in') as input_file:
    dishes = map(lambda x: x[:-1], input_file.readlines()[1:])

output = []
for i, dish in enumerate(dishes, start=1):
    res = Waiter(dish).min_number_of_flips()
    output.append('Case #{}: {}\n'.format(i, res))

with open('b.out', mode='r+') as f:
    f.writelines(output)
