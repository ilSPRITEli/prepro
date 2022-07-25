'''PrePro onsite'''
def drop():
    '''DropDrop'''
    grade = float(input())
    if grade < 1:
        print("I'm so sad.")
    elif grade < 2:
        sec = 4-grade
        print("%.2f" %sec)
    else:
        print("I'm so happy.")
drop()
