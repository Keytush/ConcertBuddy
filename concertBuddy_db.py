import sqlite3
global conn
global cur

def openDatabase():
    global conn
    global cur
    conn = sqlite3.connect('ConcertBuddy.db')
    cur = conn.cursor()

def closeDatabase():
    conn.commit()
    conn.close()


# User
def insertUser(user):
    cur.execute('INSERT INTO user ("nickname", "email", "password", "gender", '
                '"birth_date", "country", "description") '
                'VALUES(:nickname, :email, :password, :gender, '
                ':birth_date, :country, :description)',
                {'nickname': user.nickname, 'email': user.email, 'password': user.password,
                 "gender": user.gender, "birth_date": user.birth_date, "country": user.country,
                 "description": user.description})
    return cur.lastrowid

def getUser(user_id):
    cur.execute('SELECT * FROM user WHERE id=?', (user_id,))
    return cur.fetchall()

def removeUser(user_id):
    cur.execute('DELETE FROM user WHERE id=?', (user_id,))

def getUsers():
    cur.execute('SELECT * FROM user')
    return cur.fetchall()

def updateUser(gender, birth_date, country, description, user_id):
    cur.execute('UPDATE user '
                'SET gender=:gender, birth_date=:birth_date, country=:country, description=:description '
                'WHERE id=:id',
                {"gender": gender, "birth_date": birth_date, "country": country,
                 "description": description, "id": user_id})


# Event
def insertEvent(event):
    cur.execute('INSERT INTO event ("name", "date", "place", "description") '
                'VALUES(:name, :date, :place, :description)',
                {'name': event.name, 'date': event.date,
                 'place': event.place, 'description': event.description})
    return cur.lastrowid

def getEvent(event_id):
    cur.execute('SELECT * FROM event WHERE id=?', (event_id,))
    return cur.fetchall()

def removeEvent(event_id):
    cur.execute('DELETE FROM event WHERE id=?', (event_id,))

def getEvents():
    cur.execute('SELECT * FROM event')
    return cur.fetchall()

def updateEvent(name, date, place, description, event_id):
    cur.execute('UPDATE event '
                'SET name=:name, date=:date, place=:place, description=:description '
                'WHERE id=:id',
                {'name': name, 'date': date,
                 'place': place,
                 "description": description, "id": event_id})


# Hobby
def insertHobby(hobby):
    cur.execute('INSERT INTO hobby ("name", "description") '
                'VALUES(:name, :description)',
                {'name': hobby.name, 'description': hobby.description})
    return cur.lastrowid

def getHobby(hobby_id):
    cur.execute('SELECT * FROM hobby WHERE id=?', (hobby_id,))
    return cur.fetchall()

def removeHobby(hobby_id):
    cur.execute('DELETE FROM hobby WHERE id=?', (hobby_id,))

def getHobbies():
    cur.execute('SELECT * FROM hobby')
    return cur.fetchall()

def updateHobby(name, description, hobby_id):
    cur.execute('UPDATE hobby '
                'SET name=:name, description=:description '
                'WHERE id=:id',
                {'name': name, "description": description, "id": hobby_id})

# user friend
def insertFriend(user_id, friend_id):
    cur.execute('INSERT INTO friend ("user_id", "friend_id") '
                'VALUES(:user_id, :friend_id)',
                {'user_id': user_id, 'friend_id': friend_id})
    # return cur.lastrowid

def getFriend(user_id, friend_id):
    cur.execute('SELECT * FROM user '
                'JOIN friend ON user.id = friend.friend_id '
                'WHERE friend.user_id=? AND friend.friend_id=?', (user_id, friend_id,))
    return cur.fetchall()

def removeFriend(user_id, friend_id):
    cur.execute('DELETE FROM friend WHERE user_id=? AND friend_id=?', (user_id, friend_id,))

def getFriends(user_id):
    cur.execute('SELECT * FROM user '
                'JOIN friend ON user.id = friend.friend_id '
                'WHERE friend.user_id=?', (user_id,))
    return cur.fetchall()

# user event
def insertUserEvent(user_id, event_id):
    cur.execute('INSERT INTO user_event ("user_id", "event_id") '
                'VALUES(:user_id, :event_id)',
                {'user_id': user_id, 'event_id': event_id})

def removeUserEvent(user_id, event_id):
    cur.execute('DELETE FROM user_event WHERE user_id=? AND event_id=?', (user_id, event_id,))

# returns user
def getUserEvent(user_id, event_id):
    cur.execute('SELECT * FROM user '
                'JOIN user_event ON user.id = user_event.user_id '
                'WHERE user_event.user_id=? AND user_event.event_id=?', (user_id, event_id,))
    return cur.fetchall()

# returns event
def getEventUser(user_id, event_id):
    cur.execute('SELECT * FROM event '
                'JOIN user_event ON event.id = user_event.event_id '
                'WHERE user_event.user_id=? AND user_event.event_id=?', (user_id, event_id,))
    return cur.fetchall()

# returns events
def getUserEvents(user_id):
    cur.execute('SELECT * FROM event '
                'JOIN user_event ON event.id = user_event.event_id '
                'WHERE user_event.user_id=?', (user_id,))
    return cur.fetchall()

# returns users
def getEventUsers(event_id):
    cur.execute('SELECT * FROM user '
                'JOIN user_event ON user.id = user_event.user_id '
                'WHERE user_event.event_id=?', (event_id,))
    return cur.fetchall()


# user hobby
def insertUserHobby(user_id, hobby_id):
    cur.execute('INSERT INTO user_hobby ("user_id", "hobby_id") '
                'VALUES(:user_id, :hobby_id)',
                {'user_id': user_id, 'hobby_id': hobby_id})

def removeUserHobby(user_id, hobby_id):
    cur.execute('DELETE FROM user_hobby WHERE user_id=? AND hobby_id=?', (user_id, hobby_id,))

# returns hobby
def getUserHobby(user_id, hobby_id):
    cur.execute('SELECT * FROM hobby '
                'JOIN user_hobby ON hobby.id = user_hobby.hobby_id '
                'WHERE user_hobby.user_id=? AND user_hobby.hobby_id=?', (user_id, hobby_id,))
    return cur.fetchall()

# returns hobbies
def getUserHobbies(user_id):
    cur.execute('SELECT * FROM hobby '
                'JOIN user_hobby ON hobby.id = user_hobby.hobby_id '
                'WHERE user_hobby.user_id=?', (user_id,))
    return cur.fetchall()


# Other functionalities
# Registration
def registerUser(user):
    cur.execute('INSERT OR IGNORE INTO user ("nickname", "email", "password") '
                'VALUES(:nickname, :email, :password)',
                {'nickname': user.nickname, 'email': user.email, 'password': user.password})
    return cur.lastrowid

# Check if the user exists for registration
def checkRegisteredUser(user):
    cur.execute('SELECT * FROM user WHERE nickname=? AND email=? AND password=?',
                (user.nickname, user.email, user.password,))
    return cur.fetchall()

def checkExistingNickname(user):
    cur.execute('SELECT * FROM user WHERE nickname=?',
                (user.nickname,))
    return cur.fetchall()

def checkExistingEmail(user):
    cur.execute('SELECT * FROM user WHERE email=?',
                (user.email,))
    return cur.fetchall()

# Log-in
def loginUser(email, password):
    cur.execute('SELECT * FROM user WHERE email=? AND password=?', (email, password,))
    return cur.fetchall()

# Show users based on hobbies in event
def getUsersBasedOnHobbies(event_id, user_id):
    cur.execute('SELECT *, (SELECT count(hobby_id) '
                'FROM (SELECT hobby_id '
                'FROM (SELECT hobby_id FROM user_hobby WHERE user_id =:user_id '
                'UNION ALL SELECT hobby_id FROM user_hobby WHERE user_id = u1.id) '
                'GROUP BY hobby_id HAVING count(hobby_id) > 1)) match_friend '
                'FROM user u1 '
                'JOIN user_event ON u1.id = user_event.user_id '
                'WHERE user_event.event_id=:event_id '
                'AND u1.id NOT IN (:user_id) '
                'ORDER BY match_friend DESC', {"user_id": user_id, "event_id": event_id})
    return cur.fetchall()

