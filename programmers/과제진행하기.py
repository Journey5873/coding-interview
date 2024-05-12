from collections import deque

def convert_start_time(starttime):
    h, m = map(int, starttime.split(":"))
    return h*60 + m

def solution(plans):
    answer = []
    stack = []

    plans = [ (name, convert_start_time(start), int(playtime)) for name, start, playtime in plans]
    plans.sort(key=lambda x: x[1]) 

    for i in range(len(plans)):
        name, start, playtime = plans[i]

        if i == len(plans) - 1:
            answer.append(name)
            break

        if start + playtime > plans[i+1][1]:
            stack.append((name, (start + playtime) - plans[i+1][1]))
        else:
            answer.append(name)

            time = plans[i+1][1]  - (start + playtime) # 다음 과목까지 남은 시간
            while stack:
                left_name, left_time = stack.pop()
                if left_time <= time: # 밀린 과목이 다음 과목시간 보다 작거나 같을때
                    time -= left_time # 다음과목까지 남은시간에서 과목을 수행한 시간 만큼 빼주기
                    answer.append(left_name)
                elif start >= plans[i+1][1]:
                    stack.append((left_name, left_time))
                    break
        
    while stack:
        name, left_time = stack.pop()
        answer.append(name)

    return answer