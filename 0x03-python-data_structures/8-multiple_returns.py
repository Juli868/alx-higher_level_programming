#!/usr/bin/python3
def multiple_returns(sentence):
    answer = [1,2]
    answer[0] = len(sentence)
    answer[1] = sentence[0]
    return(tuple(answer))
