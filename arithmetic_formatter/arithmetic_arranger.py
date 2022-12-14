def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        raise Exception('Error: Too many problems.')
    for problem in problems:
        for let in problem:
            if let.isalpha():
                raise Exception('Error: Numbers must only contain digits.')
        split = problem.split()
        if split[1] not in '+-':
            raise ValueError('Error: Operator must be "+" or "-".')
        if len(split[0]) > 4 or len(split[2]) > 4:
            raise Exception('Error: Numbers cannot be more than four digits.')

    first, second = [], []
    strips, answers = [], []
    for problem in problems:
        splited = problem.split()
        answers.append(int(splited[0]) + int(splited[2])) \
            if splited[1] == '+' else answers.append(int(splited[0]) - int(splited[2]))

        if len(splited[0]) > len(splited[2]):
            first_val = f'  {splited[0]}'
            second_val = f'{splited[1]} ' + ' ' * (len(splited[0]) - len(splited[2])) + f'{splited[2]}'
            first.append(first_val)
            second.append(second_val)
            strips.append(len(second_val) * '-')
        else:
            first_val = '  ' + ' ' * (len(splited[2]) - len(splited[0])) + f'{splited[0]}'
            second_val = f'{splited[1]} ' + f'{splited[2]}'
            first.append(first_val)
            second.append(second_val)
            strips.append(len(first_val) * '-')

    a = '    '.join(val for val in first) + '\n'
    b = '    '.join(val for val in second) + '\n'
    if not args:
        c = '    '.join(val for val in strips)
        return a + b + c

    if True in args:
        c = '    '.join(val for val in strips) + '\n'
        d = '    '.join((' ' * (len(strip) - len(str(val)))) + str(val) for val, strip in zip(answers, strips))
        return a + b + c + d
