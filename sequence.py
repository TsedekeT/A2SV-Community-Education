def restore_sequence(test_cases):
    results = []
    for n, b in test_cases:
        a = [0] * n  # Initialize the array for the restored sequence
        left, right = 0, n - 1  # Pointers to the current positions in b
        for i in range(n):
            if i % 2 == 0:
                a[i] = b[left]
                left += 1
            else:
                a[i] = b[right]
                right -= 1
        results.append(a)
    return results

# Read input
t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    b = list(map(int, input().strip().split()))
    test_cases.append((n, b))

# Process and output results
results = restore_sequence(test_cases)
for result in results:
    print(' '.join(map(str, result)))
