# def consecutive_sum_solutions(n):
#     solutions = []
#     for start in range(1, n):
#         total = 0
#         current_solution = []
#         for number in range(start, n + 1):
#             total += number
#             current_solution.append(number)
#             if total == n:
#                 if len(current_solution) >= 2:
#                     solutions.append(current_solution)
#                 break
#             if total > n:
#                 break
#     return solutions

if __name__ == "__main__":
    # print(consecutive_sum_solutions(15))
	...
