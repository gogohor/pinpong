import sqlite3
from random import randint
 
db_name = 'quiz.sqlite'
conn = None
cursor = None
 
def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
 
def close():
    cursor.close()
    conn.close()
 
def do(query):
    cursor.execute(query)
    conn.commit()
 
def clear_db():
    ''' вбиває всі таблиці '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()
 
def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    
    do('''CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY, 
            name VARCHAR)''' 
    )
    do('''CREATE TABLE IF NOT EXISTS question (
                id INTEGER PRIMARY KEY, 
                question VARCHAR, 
                answer VARCHAR, 
                wrong1 VARCHAR, 
                wrong2 VARCHAR, 
                wrong3 VARCHAR)'''
    )
    do('''CREATE TABLE IF NOT EXISTS quiz_content (
                id INTEGER PRIMARY KEY,
                quiz_id INTEGER,
                question_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz (id),
                FOREIGN KEY (question_id) REFERENCES question (id) )'''
    )
    close()
 
def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()
 
def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')
 
def add_questions():
    questions = [
        ('Скільки місяців на рік мають 28 днів?', 'Всі', 'Один', 'Ні одного', 'Два'),
        ('Яким стане зелена скеля, якщо впаде в Червоне море?', 'Мокрою?', 'Червоною', 'Не зміниться', 'Фіолетовою'),
        ('Якою рукою краще розмішувати чай?', 'Ложкою', 'Правою', 'Лівою', 'Будь-якою'),
        ('Що не має довжини, глибини, ширини, висоти, а чи можна виміряти?', 'Час', 'Безглуздість', 'Море', 'Повітря'),
        ('Коли мережею можна витягти воду?', 'Коли вода замерзла', 'Коли немає риби', 'Коли спливла золота рибка', 'Коли мережа порвалася'),
        ('Що більше за слона і нічого не важить?', 'Тінь слона', 'Повітряна куля', 'Парашут', 'Хмара'),
        ('Що таке в кишені?', 'Кільце', 'Кулак', 'Дірка', 'Бублик')
    ]
    open()
    cursor.executemany('''INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    close()
 
def add_quiz():
    quizes = [
        ('Вікторина 1', ),
        ('Вікторина 2', ),
        ('Вікторина 3', ),
    ]
    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()
 
def add_links():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
    
    links=[[1,1], [1,2],[1,3],[1,4],[1,5],[2,1],[2,2],[2,3],[3,1]]

    for i in links:
        cursor.execute(query, [i[0], i[1]])
        conn.commit()
        
    close()
 
 
def get_question_after(last_id=0, vict_id=1):
    ''' повертає наступне питання після запитання з переданим id
     для першого запитання передається значення за замовчуванням
 '''
    open()
    query = '''
    SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content 
    WHERE quiz_content.question_id == question.id
    AND quiz_content.id > ? AND quiz_content.quiz_id == ? 
    ORDER BY quiz_content.id '''
    cursor.execute(query, [last_id, vict_id] )
 
    result = cursor.fetchone()
    close()
    return result 
 
def get_quises():
    query = 'SELECT * FROM quiz ORDER BY id'
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result
 
def get_quiz_count():
    ''' необов'язкова функція '''
    query = 'SELECT MAX(quiz_id) FROM quiz_content'
    open()
    cursor.execute(query)
    result = cursor.fetchone()
    close()
    return result
    
 
def get_random_quiz_id():
    query = 'SELECT quiz_id FROM quiz_content'
    open()
    cursor.execute(query)
    ids = cursor.fetchall()
    rand_num = randint(0, len(ids) - 1)
    rand_id = ids[rand_num][0]
    close()
    return rand_id
    
 
def check_answer(quest_id, answer):
    query = '''
        SELECT question.answer FROM quiz_content, question WHERE quiz_content.id = ? 
        AND quiz_content.question_id = question.id
    '''
    open()
    cursor.execute(query, str(quest_id))
    result = cursor.fetchone()
    close()
    if result is None:
        return False
    else:
        if result[0] == answer:
            return True
        else:
            return False

def main():
    clear_db()
    create()
    add_questions()
    add_quiz()
    show_tables()
    add_links()
    show_tables()
    # print(get_question_after(0, 3))
    # print(get_quiz_count())
    # print(get_random_quiz_id())
    pass
    
if __name__ == "__main__":
    main()
