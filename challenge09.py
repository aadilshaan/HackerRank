# Find the Runner-Up Score!

num = int(input())
num_list = list(input().split())
if num == len(num_list):
    my_list = [int(i) for i in num_list]
    run_up = [run for run in my_list if run != max(my_list)]
    runner_up = max(run_up)
    print(runner_up)