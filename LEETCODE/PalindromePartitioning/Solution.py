def is_palindrome(s):
    return s == s[::-1]

def palindrome_partitions(s):
    result = []
    def backtrack(start, path):
        if start == len(s):
            result.append(path.copy())
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()
    backtrack(0, [])
    return result

def test_solution():
    s = "aab"
    expected_output = [["a", "a", "b"], ["aa", "b"]]
    assert palindrome_partitions(s) == expected_output, f"Expected {expected_output}, but got {palindrome_partitions(s)}"
    s = "racecar"
    expected_output = [["r", "aceca", "r"], ["racecar"]]
    assert palindrome_partitions(s) == expected_output, f"Expected {expected_output}, but got {palindrome_partitions(s)}"
    s = "bbb"
    expected_output = [["b", "b", "b"], ["bb", "b"], ["b", "bb"], ["bbb"]]
    assert palindrome_partitions(s) == expected_output, f"Expected {expected_output}, but got {palindrome_partitions(s)}"

if __name__ == "__main__":
    test_solution()
    print("Test passed!")