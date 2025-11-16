import os
#1
# def create_folder(path):
#     os.mkdir(path)
# create_folder('/.venv/Lib')
#2
# def delete_folder(path):
#     os.rmdir(path)
# delete_folder('Z:\יד תשפו\רותן תמר\פיתון\pythonProject\ניסוי')
#3
def create_file(path):
    try:
        with open(path, 'x', encoding='utf-8') as f:
            pass
    except FileExistsError:
        print(f"The file '{path}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

create_file('Z:\\יד תשפו\\רותן תמר\\פיתון\\pythonProject\\ניסוי')
#4
def add_content(path,content,append=False):
    mode='a' if append else 'w'
    with open(path,mode)as aaa:
        aaa.write(content)

add_content("Z:\\יד תשפו\\רותן תמר\\פיתון\\pythonProject\\ניסוי\\aaa.txt","asdfghj",False)
#5
def remove_file(path):
        os.remove(path)

remove_file("Z:\\יד תשפו\\רותן תמר\\פיתון\\pythonProject\\ניסוי\\aaa.txt")
#6
def list_content(path):
    content = os.listdir(path)
    print(content)
list_content("Z:\\יד תשפו\\רותן תמר\\פיתון\\pythonProject\\ניסוי")
#7
def current_path():
    print(os.getcwd())
current_path()