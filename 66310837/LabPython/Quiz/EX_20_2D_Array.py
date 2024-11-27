num_i, num_j = map(int, input().split(','))

result_list = [[i*j for j in range(num_j)] for i in range(num_i)]
print(result_list)