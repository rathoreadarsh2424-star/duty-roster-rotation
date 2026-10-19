def rotateRoster(names, k):
    """Rotate names to the right by k places."""
    n = len(names)
    k = k % n
    return names[-k:] + names[:-k] if k else names[:]


if __name__ == "__main__":
    names = ["A", "B", "C", "D", "E"]

    print(rotateRoster(names, 2))  # Expected: ['D', 'E', 'A', 'B', 'C']
    print(rotateRoster(names, 7))  # Expected: ['D', 'E', 'A', 'B', 'C']
