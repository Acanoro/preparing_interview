from Stack import Stack
from utils import is_balanced


def main():
    stack = Stack()

    print(stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.peek())
    print(stack.pop())
    print(stack.size())
    print(stack.is_empty())

    print(is_balanced("(((([{}]))))"))
    print(is_balanced("[([])((([[[]]])))]{()}"))
    print(is_balanced("{{[()]}}"))
    print(is_balanced("}{"))
    print(is_balanced("{{[(])]}}"))
    print(is_balanced("[[{())}]"))


if __name__ == '__main__':
    main()
