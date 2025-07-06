# 1.  Turn the following snippet into a function:
#     numbers = [1,2,3,4,5]
#     squares = []
#     for n in numbers:
#         squares.append(n*n)
#     print(squares)
#     Requirements:
#     - Create def compute_squares(nums: list[int]) -> list[int]
#     - Add a docstring and type hints
#     - Call it on at least two different lists

def compute_squares(nums: list[int]) -> list[int]:
    return [n * n for n in nums]
if __name__ == "__main__":

    numbers1 = [1, 2, 3, 4,]
    squares1 = compute_squares(numbers1)
    print(squares1) 

    numbers2 = [3, 4, 5]
    squares2 = compute_squares(numbers2)
    print(squares2) 


