import random

# Integer Random Numbers
random.randrange(1, 10)  # 1 to 9; 10 excluded
random.randint(1, 10)    # 1 to 10; both included

print(random.randrange(1, 10))
print(random.randint(1, 10))


# Float Random Numbers
number = random.random()
print(number)

number2 = random.uniform(10.5, 20.5)
print(number2)

# Random Choice
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

# Random Shuffle
random.shuffle(fruits)
print(fruits)

# Random Sample
sample = random.sample(fruits, 2)
print(sample)

# Random Seed
random.seed(10)
print(random.random())

# Random Gaussian
gaussian_number = random.gauss(0, 1)  # mean=0, standard deviation=1
print(gaussian_number)