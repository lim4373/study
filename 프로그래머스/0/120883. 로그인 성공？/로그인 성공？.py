def solution(id_pw, db):
    db_dict = {i[0]: i[1] for i in db}
    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"
