class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []

        for i in range(1, n + 1):

            divisibleBy3 = i % 3 == 0
            divisibleBy5 = i % 5 == 0

            if divisibleBy3 and divisibleBy5:
                answer.append("FizzBuzz")

            elif divisibleBy3:
                answer.append("Fizz")

            elif divisibleBy5:
                answer.append("Buzz")

            else:
                answer.append(str(i))

        return answer