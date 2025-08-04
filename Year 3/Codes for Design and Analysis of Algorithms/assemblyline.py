def assembly_line_dp(a, t, e, x):
    """
    Solves the Assembly Line Scheduling problem using Dynamic Programming.
    Shows the four DP steps clearly.
    """
    n = len(a[0])  # number of stations

    # Step 2: Define the DP table
    f1 = [0] * n  # Time to reach station i on line 1
    f2 = [0] * n  # Time to reach station i on line 2

    # Step 1: Characterize Optimal Substructure
    # Base cases (entry + first station time)
    f1[0] = e[0] + a[0][0]
    f2[0] = e[1] + a[1][0]
    print(f"Initial time: f1[0] = {f1[0]}, f2[0] = {f2[0]}")

    # Step 3: Fill the table
    for i in range(1, n):
        f1[i] = min(f1[i-1] + a[0][i], f2[i-1] + t[1][i] + a[0][i])
        f2[i] = min(f2[i-1] + a[1][i], f1[i-1] + t[0][i] + a[1][i])
        print(f"Station {i+1}: f1[{i}] = {f1[i]}, f2[{i}] = {f2[i]}")

    # Step 4: Construct the optimal solution (final exit)
    total_time_line1 = f1[-1] + x[0]
    total_time_line2 = f2[-1] + x[1]
    min_time = min(total_time_line1, total_time_line2)
    best_line = 1 if total_time_line1 <= total_time_line2 else 2

    print(f"\nFinal time with exit: Line 1 = {total_time_line1}, Line 2 = {total_time_line2}")
    print(f"Minimum total time: {min_time} (Exit from Line {best_line})")

    return min_time, f1, f2, best_line


# --- Sample Values (Classic Problem) ---

# Processing times at stations
a = [
    [7, 9, 3, 4, 8, 4],  # Line 1
    [8, 5, 6, 4, 5, 7]   # Line 2
]

# Transfer times between lines
t = [
    [0, 2, 3, 1, 3, 4],  # From Line 1 to Line 2
    [0, 2, 1, 2, 2, 1]   # From Line 2 to Line 1
]

# Entry times for lines
e = [2, 4]

# Exit times for lines
x = [3, 2]

# Run the algorithm
min_time, f1_result, f2_result, last_line = assembly_line_dp(a, t, e, x)