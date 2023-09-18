def solution(array, commands):
    answer = []
    for commands in commands:


        start_index = commands[0] - 1
        end_index = commands[1]
        answer_index = commands[2] - 1

        result = sorted(array[start_index:end_index])
        print(result)
        result=result[answer_index]
        print(result)
        answer.append(result)

    return answer

my_array = [1, 5, 2, 6, 3, 7, 4]
my_commands = [(2, 5, 3), (4, 4, 1), (1, 7, 3)]
result = solution(my_array, my_commands)
print(result)