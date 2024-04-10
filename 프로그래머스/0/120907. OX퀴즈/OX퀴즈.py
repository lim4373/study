def solutions(quizs):
    quizs = quizs.replace('=', '==')
    return eval(quizs)

def solution(quiz):
    return ["O" if solutions(quizs) else "X" for quizs in quiz]