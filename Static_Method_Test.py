class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods without creating an instance of MathUtils
sum_result = MathUtils.add(5, 3)
product_result = MathUtils.multiply(4, 2)

print(f"Sum: {sum_result}")         # Output: Sum: 8
print(f"Product: {product_result}")  # Output: Product: 8