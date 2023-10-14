words = input().split()
palindrome = input()

palindrome_list = [element for element in words if element == element[::-1]]
palindrome_count = palindrome_list.count(palindrome)

print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")