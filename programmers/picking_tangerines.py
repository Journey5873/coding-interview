def solution(k, tangerine):
    answer = 0
    current = 0
    tan_dic = {}

    for t in tangerine:
        if t in tan_dic:
            tan_dic[t] += 1
        else:
            tan_dic[t] = 1
    
    sorted_tan = dict(sorted(tan_dic.items(), key=lambda x: x[1], reverse=True))
    
    for key in sorted_tan:
        if k > current:
            answer += 1
            current += sorted_tan[key]
        
        if current == k:
            break

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))