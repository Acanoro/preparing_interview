from Stack import Stack


def is_balanced(sequence):
    stack = Stack()
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in matching_brackets.values():
            stack.push(char)
        elif char in matching_brackets.keys():
            if stack.is_empty() or stack.pop() != matching_brackets[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"
