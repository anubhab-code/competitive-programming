def arithmetic_sequence_elements(a, r, n):
    return ', '.join(str(a + r*x) for x in range(n))