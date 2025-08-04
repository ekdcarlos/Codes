import matplotlib.pyplot as plt

# Euclidean Algorithm
def gcd_euclid(a, b):
    steps = 0
    while b != 0:
        a, b = b, a % b
        steps += 1
    return a, steps

# Conservative Integer Method
def gcd_conservative(a, b):
    steps = 0
    for i in range(min(a, b), 0, -1):
        steps += 1
        if a % i == 0 and b % i == 0:
            return i, steps
    return 1, steps

# Middle School Method (Prime factorization)
def gcd_middle_school(a, b):
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 1
        if n > 1:
            factors.append(n)
        return factors

    steps = 0
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    common_factors = []

    for f in set(factors_a):
        common_count = min(factors_a.count(f), factors_b.count(f))
        common_factors.extend([f] * common_count)
        steps += 1

    gcd_value = 1
    for f in common_factors:
        gcd_value *= f
        steps += 1
    return gcd_value, steps

# Main process
def compare_gcd_methods(a, b):
    # Compute GCD using different methods
    gcd_e, steps_e = gcd_euclid(a, b)
    gcd_c, steps_c = gcd_conservative(a, b)
    gcd_m, steps_m = gcd_middle_school(a, b)

    # Output results
    print(f"Euclidean Algorithm: GCD = {gcd_e}, Steps = {steps_e}")
    print(f"Conservative Method: GCD = {gcd_c}, Steps = {steps_c}")
    print(f"Middle School Method: GCD = {gcd_m}, Steps = {steps_m}")

    # Plotting efficiency
    methods = ['Euclid', 'Conservative', 'Middle School']
    steps = [steps_e, steps_c, steps_m]

    plt.figure(figsize=(8, 5))
    plt.bar(methods, steps, color=['skyblue', 'lightcoral', 'gold'])
    plt.title(f'GCD({a}, {b}) - Step Comparison of Methods')
    plt.ylabel('Number of Steps')
    plt.xlabel('Method')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Run the comparison
compare_gcd_methods(60, 24)