import random
from sys import argv


def throw_dice(self, user_dice):
    # Initialize all variables
    self.user_dice = user_dice
    self.repet = 0
    self.return_val_throw = []

    while (self.repet != self.user_dice):
        # Throws a dice (1 - 6) and records the value in return_val_throw list
        # Then incroments the repet variable with one
        dice = random.randrange(1, 7)
        self.return_val_throw.append(dice)
        self.repet += 1

    # Returns return_val_throw
    return self.return_val_throw


def average(self, count_base):
    # Initialize all variables
    self.count_base = count_base
    self.return_val_average = 0

    # loops over all number un count_base and puts them in return_val_average
    for num in self.count_base:
        self.return_val_average += num

    # Devides return_val_average with length of count_base
    # Returns return_val_average
    self.return_val_average = self.return_val_average / len(self.count_base)
    return self.return_val_average


def counter(self, count_base, count_def):
    # Initialize all variables
    self.count_def = count_def
    self.count_base = count_base
    self.return_val_counter = 0

    # loops over all numbers in count_base and adds one to return_val_counter
    # If num is equal to count_def
    for num in self.count_base:
        if (num == self.count_def):
            self.return_val_counter += 1

    # Returns return_val_counter
    return self.return_val_counter


# A function to print the help page
def helpper():
    print("""
          -h shows help page

          -a gives you the average of all the trows

          -c ? takes a number and counts how many times it
               was in the data set
          """)


def main(arguments):
    # Checks if the user needs help
    # And if they do prints the arguments list
    try:
        arguments.index('-h')
        helpper()
        exit()
    except ValueError:
        pass

    averge = None
    count = None
    # Get the user input on how many times the dice will be thrown
    user_input = int(input("> "))
    # Gets the result from the throws
    results = throw_dice(main, user_input)

    # Gets the average result of the throws
    try:
        arguments.index('-a')
        averge = average(main, results)
    except ValueError:
        pass

    # Counts how many times a specific number had been thrown
    try:
        pos = arguments.index('-c')
        count = counter(main, results, int(arguments[pos + 1]))
    except ValueError:
        pass

    # Returns all results gotten above
    return results, averge, count


if __name__ == "__main__":
    try:
        # Runs the main function
        results, averge, count = main(argv)

        # Prints the results gotten from the main function
        print(f"results: {results}")
        if (averge is not None):
            print(f"average: {averge}, {averge * len(results)}")
        if (count is not None):
            print(f"count: {count}")
    except KeyboardInterrupt:
        print("\nUser stopped programe")
