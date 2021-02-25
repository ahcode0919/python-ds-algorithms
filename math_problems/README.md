# Math

* [Count Primes](#count-primes)
* [Fizz Buzz](#fizz-buzz)
* [Moving Average](#moving-average)
* [Power of Three](#power-of-three)

## Count Primes

Count the number of prime numbers less than a non-negative number

Example

Input: 10

Output: 4

```python
def count_primes(number: int) -> int:
    is_prime = [True] * number

    for num in range(2, number):
        if not num * num < number:
            break
        if not is_prime[num]:
            continue

        num1 = num * num
        while num1 < number:
            is_prime[num1] = False
            num1 += num

    count = 0
    for index in range(2, number):
        if is_prime[index]:
            count += 1
    return count
```

## Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

```python
def fizz_buzz(iterations: int) -> List[str]:
    output = []

    if iterations and iterations < 0:
        return output

    for num in range(1, iterations + 1):
        three = num % 3 == 0
        five = num % 5 == 0
        if three and five:
            output.append('FizzBuzz')
        elif three:
            output.append('Fizz')
        elif five:
            output.append('Buzz')
        else:
            output.append(f'{num}')

    return output
```

## Moving Average

Create a class `MovingAverage` to calculate the average of a max amount of numbers (n).
Class should have a `.next(value: int)` method that returns the average after adding the new value.
The oldest values should be removed when adding new values once the max amount of numbers is reached.

```python
class MovingAverage:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.queue = deque()

    def next(self, number: int) -> float:
        self.queue.append(number)

        if len(self.queue) > self.max_size:
            self.queue.popleft()

        return sum(self.queue) / float(len(self.queue))
```

## Power of Three

Given an integer, write a function to determine if it is a power of three.

```python
def power_of_three(number: int) -> bool:
    int_32_max = 1162261467
    int_64_max = 4052555153018976267
    
    if maxsize > int_32_max:
        return number > 0 and int_64_max % number == 0
    return number > 0 and int_32_max % number == 0
```