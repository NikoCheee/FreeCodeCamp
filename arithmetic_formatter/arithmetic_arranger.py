def arithmetic_arranger(problems):
    first, second = [], []
    strips = []
    for problem in problems:
        splited = problem.split()
        if len(splited[0]) > len(splited[2]):
            first_val = f'  {splited[0]}'
            second_val = f'{splited[1]} ' + ' '*(len(splited[0]) - len(splited[2])) + f'{splited[2]}'
            first.append(first_val)
            second.append(second_val)
            strips.append(len(second_val)*'-')
        else:
            first_val = '  ' + ' '*(len(splited[2]) - len(splited[0])) + f'{splited[0]}'
            second_val = f'{splited[1]} ' + f'{splited[2]}'
            first.append(first_val)
            second.append(second_val)
            strips.append(len(first_val)*'-')

    a = '    '.join(val for val in first) + '\n'
    b = '    '.join(val for val in second) + '\n'
    c = '    '.join(val for val in strips) + '\n'

    arranged_problems = [a, b, c]
    # for i in arranged_problems:
    #     print(i)

    return arranged_problems

