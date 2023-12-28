def solution(n, words):
    answer = [0,0]
    word_dic = {}

    for i in range(len(words)):
        if i == 0 :
            word_dic[words[i]] = True
            continue
        pre_word = words[i - 1]
        word = words[i]

        if word in word_dic or pre_word[-1] != word[0]:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1

            return answer

        word_dic[words[i]] = True

    return answer

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])