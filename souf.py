import json as j
def userDone():
    with open("username.txt", "r") as userD:
        try:
            user = j.load('username.txt')
        except Exception as e:
            print('Could not load username.txt','\nError:', e)
        finally:
            if 'username' not in user:
                return False
            else:
                return True