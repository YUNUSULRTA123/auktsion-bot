import sqlite3
    
# Создаем подключение к базе данных
connection = sqlite3.connect('movie.db')

# Создание курсора для выполнения SQL-запросов
cursor = connection.cursor()

cursor.execute("""SELECT  title, release_date FROM movies
WHERE release_date > '2008' AND release_date < '2010'
               """)

cursor.execute("""SELECT vote_average, title
FROM movies
ORDER BY vote_average""")

cursor.execute("""
SELECT vote_average, title
FROM movies
ORDER BY vote_average DESC
""")

cursor.execute("""SELECT * FROM movies
LIMIT 1""")

cursor.execute("""
SELECT title, release_date FROM movies
WHERE release_date > '2008' AND release_date < '2010'
ORDER BY RANDOM()
LIMIT 3
""")

cursor.execute("SELECT * FROM movies WHERE release_date>2015 OR vote_average>8")
cursor.execute("SELECT * FROM movies WHERE budget = 0")

cursor.execute("SELECT * FROM movies WHERE release_date BETWEEN '2015-01' AND '2015-02'")

cursor.execute("""
SELECT * FROM movies
WHERE tagline LIKE '%programmer%'""")

cursor.execute("""SELECT * FROM movies
WHERE title LIKE 'Harry%';""")

cursor.execute("""SELECT * FROM movies
WHERE director_id IN (4765, 5417);""")

cursor.execute("SELECT * FROM movies WHERE tagline IS NULL")

cursor.execute("SELECT * FROM movies LIMIT 10 OFFSET 100")

cursor.execute("SELECT * FROM movies LIMIT 1")

cursor.execute("SELECT * FROM movies WHERE popularity LIMIT 1")

cursor.execute("""
SELECT title, budget 
FROM movies
ORDER BY popularity DESC
LIMIT 1
""")

cursor.execute("""
SELECT title
FROM movies
WHERE strftime('%Y-%m', release_date) = '2009-12'
ORDER BY budget DESC
LIMIT 1
""")

cursor.execute("""
SELECT title
FROM movies
WHERE tagline LIKE '%The battle within.%'
""")

cursor.execute("""
SELECT title
FROM movies
WHERE release_date < '1980-01-01' AND vote_average > 8
ORDER BY vote_count DESC
LIMIT 1
""")

cursor.execute("""SELECT d.name AS director_name, MAX(m.release_date) AS last_release_date
FROM directors d
JOIN movies m ON d.id = m.director_id
GROUP BY d.name;
""")

cursor.execute("""SELECT d.name AS director_name, SUM(m.budget) AS total_budget
FROM directors d
JOIN movies m ON d.id = m.director_id
GROUP BY d.name;
""")

cursor.execute("""SELECT d.name AS director_name, COUNT(m.id) AS film_count
FROM directors d
LEFT JOIN movies m ON d.id = m.director_id
GROUP BY d.name;
""")

cursor.execute("""SELECT m.title, COUNT(mg.genre_id) AS genre_count
FROM movies m
LEFT JOIN movies_genres mg ON m.id = mg.movie_id
GROUP BY m.title;
""")

# Использование метода fetchall() для получения результатов
result = cursor.fetchall()

# Вывод результатов
for row in result:
    print(row)
    
# Закрываем соединение с базой данных после использования
connection.close()