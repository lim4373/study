# def solution(s):
#     return s.isdigit() and len(s) in (4,6)

def solution(s):
    if len(s) == 4 or len(s) ==6:
        if s.isdigit()==True:
            return True
        else:
            return False
    else:
        return False
            