# This file demonstrates work of population optimization algorithm. 
# It takes array of creatures with their scores, sort them by score and kills
# half of population. Creatures with higherscore are most likely to survive.
# However, the last creature do not have 100% chance to be killed and
# the first do not have 100% chance to survive


import time
import random


ITEMS_PER_LINE = 20  # required for output of population


def profiler(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()

        print('\/ Execution time: %f seconds \/' % (end - start))

        return result
    return wrapper


class Creature(object):
    def __init__(self):
        self.score = random.randrange(1000)
        self.is_dead = False

    def __str__(self):
        return '[ ]' if self.is_dead else '[■]'


class Population(list):
    def __init__(self, size=500):
        for i in range(size):
            self.append(Creature())

    def sort(self):
        self = sorted(self, key=lambda x: x.score)

    def __str__(self):
        output = ''

        for i, creature in enumerate(self):
            if i % ITEMS_PER_LINE == 0 and i > 0:
                output += '\n'
            output += str(creature)

        return output


@profiler
def optimize_population(population):
    population.sort()
    return iter_kill(population, len(population))


def iter_kill(population, size, elements_replaced=0):
    elements_to_replace = size / 2

    for i in range(size):
        if elements_replaced == elements_to_replace:
            return population

        if not population[-i - 1].is_dead and \
                i + 1 < random.randrange(size + 1):

            population[-i - 1].is_dead = True
            elements_replaced += 1

    return iter_kill(population, size, elements_replaced=elements_replaced)


if __name__ == '__main__':
    while True:
        population = Population()
        population = optimize_population(population)

        print(population)

        time.sleep(3)
