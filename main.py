def hello():
return "Hello, World!"
def calculate_sum(a: int, b: int) -> int:
return a + b
if __name__ == "__main__":
print(hello())
print(f"Result: {calculate_sum(2, 3)}")
