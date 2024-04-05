class MathHelper:
    @staticmethod
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)


numbers = [10, 20, 30, 40, 50]
average = MathHelper.calculate_average(numbers)
print("Promedio:", average)
