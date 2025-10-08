def validate_stack_sequences(pushed, popped):
    '''реализация валидации последовательностей push/pop для стека'''
    stack = []
    pop_index = 0 

    for item in pushed:
        stack.append(item)
        while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1

    return len(stack) == 0