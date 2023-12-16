import sqlite3

conn = sqlite3.connect("quiz.sqlite")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS quiz")
cursor.execute("DROP TABLE IF EXISTS question")
cursor.execute("DROP TABLE IF EXISTS quiz_content")
conn.commit()

cursor.execute('''PRAGMA foreign_keys=on''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS quiz (id INTEGER PRIMARY KEY, name VARCHAR)''')
conn.commit()

# створити табличку запитання question в ній мають бути поля id, question, answer, wrong1, wrong2, wrong3

cursor.execute('''CREATE TABLE IF NOT EXISTS question (id INTEGER PRIMARY KEY, 
               question VARCHAR, 
                answer VARCHAR, 
               wrong1 VARCHAR,
               wrong2 VARCHAR,
               wrong3 VARCHAR
               )''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS quiz_content 
               (id INTEGER PRIMARY KEY, quiz_id INTEGER, question_id INTEGER, 
               FOREIGN KEY (quiz_id) REFERENCES quiz (id),
               FOREIGN KEY (question_id) REFERENCES question (id)
                 )''')
conn.commit()

quiz = [("My quiz 1",), ("my quiz 2",)]

cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quiz)
conn.commit()

question = [
            ('якесь запитання','vidpovid', "wrong1", "wrong2", 'wrong3',),
            ('якесь запитання','vidpovid', "wrong1", "wrong2", 'wrong3',)
            ]

cursor.executemany('''INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)''', question)
conn.commit()

quiz_content = [
  (1, 1,),
  (1, 2,),
]

cursor.executemany('''INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)''', quiz_content)
conn.commit()


def get_question(question_id, quiz_id):
  conn = sqlite3.connect("quiz.sqlite")
  cursor = conn.cursor()
  cursor.execute('''SELECT question.answer, question.question 
               FROM question, quiz_content 
               WHERE question.id == quiz_content.question_id 
               AND quiz_content.quiz_id == ?''', [1])
  data = cursor.fetchall()
  return data
  