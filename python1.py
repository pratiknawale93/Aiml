print("hello world")

def print_butterfly(n):
    # 1. Upper half of the butterfly
    for i in range(1, n + 1):
        # Left wing stars
        print("*" * i, end="")
        
        # Center spaces
        spaces = 2 * (n - i)
        print(" " * spaces, end="")
        
        # Right wing stars
        print("*" * i)

    # 2. Lower half of the butterfly
    for i in range(n, 0, -1):
        # Left wing stars
        print("*" * i, end="")
        
        # Center spaces
        spaces = 2 * (n - i)
        print(" " * spaces, end="")
        
        # Right wing stars
        print("*" * i)

# Set the size (n is the height of each half)
size = 5
print_butterfly(size)

