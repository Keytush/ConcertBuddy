import concertBuddy_db as db
import user as u
import event as e
import hobby as h

# User
def addUser(user):
    db.openDatabase()
    user_id = db.insertUser(user)
    db.closeDatabase()
    user.id = user_id
    return user

def getUser(user_id):
    db.openDatabase()
    items = db.getUser(user_id)

    if not items:
        return f"User with ID {user_id} was not found"

    db.closeDatabase()
    return u.tupleToUser(items[0])

def getUsers():
    db.openDatabase()
    items = db.getUsers()

    if not items:
        return f"There are no users"

    db.closeDatabase()
    users = []
    for item in items:
        users.append(u.tupleToUser(item))
    return users

def removeUser(user_id):
    db.openDatabase()
    items = db.getUser(user_id)

    if not items:
        return f"User with ID {user_id} was not found"

    remove_user = u.tupleToUser(items[0])
    db.removeUser(remove_user.id)
    db.closeDatabase()
    return f"User with ID {user_id} was removed"

def updateUser(gender, birth_date, country, description, user_id):
    db.openDatabase()
    items = db.getUser(user_id)

    if not items:
        return f"User with ID {user_id} was not found"

    update_user = u.tupleToUser(items[0])
    db.updateUser(gender, birth_date, country, description, update_user.id)
    db.closeDatabase()
    return f"User with ID {user_id} was updated"


# Event
def addEvent(event):
    db.openDatabase()
    event_id = db.insertEvent(event)
    db.closeDatabase()
    event.id = event_id
    return event

def getEvent(event_id):
    db.openDatabase()
    items = db.getEvent(event_id)

    if not items:
        return f"Event with ID {event_id} was not found"

    db.closeDatabase()
    return e.tupleToEvent(items[0])

def getEvents():
    db.openDatabase()
    items = db.getEvents()

    if not items:
        return f"There are no events"

    db.closeDatabase()
    events = []
    for item in items:
        events.append(e.tupleToEvent(item))
    return events

def removeEvent(event_id):
    db.openDatabase()
    items = db.getEvent(event_id)

    if not items:
        return f"Event with ID {event_id} was not found"

    remove_event = e.tupleToEvent(items[0])
    db.removeEvent(remove_event.id)
    db.closeDatabase()
    return f"Event with ID {event_id} was removed"

def updateEvent(name, date, place, description, event_id):
    db.openDatabase()
    items = db.getEvent(event_id)

    if not items:
        return f"Event with ID {event_id} was not found"

    update_event = e.tupleToEvent(items[0])
    db.updateEvent(name, date, place, description, update_event.id)
    db.closeDatabase()
    return f"Event with ID {event_id} was updated"


# Hobby
def addHobby(hobby):
    db.openDatabase()
    hobby_id = db.insertHobby(hobby)
    db.closeDatabase()
    hobby.id = hobby_id
    return hobby

def getHobby(hobby_id):
    db.openDatabase()
    items = db.getHobby(hobby_id)

    if not items:
        return f"Hobby with ID {hobby_id} was not found"

    db.closeDatabase()
    return h.tupleToHobby(items[0])

def getHobbies():
    db.openDatabase()
    items = db.getHobbies()

    if not items:
        return f"There are no hobbies"

    db.closeDatabase()
    hobbies = []
    for item in items:
        hobbies.append(h.tupleToHobby(item))
    return hobbies

def removeHobby(hobby_id):
    db.openDatabase()
    items = db.getHobby(hobby_id)

    if not items:
        return f"Hobby with ID {hobby_id} was not found"

    remove_hobby = h.tupleToHobby(items[0])
    db.removeHobby(remove_hobby.id)
    db.closeDatabase()
    return f"Hobby with ID {hobby_id} was removed"

def updateHobby(name, description, hobby_id):
    db.openDatabase()
    items = db.getHobby(hobby_id)

    if not items:
        return f"Hobby with ID {hobby_id} was not found"

    update_hobby = h.tupleToHobby(items[0])
    db.updateHobby(name, description, update_hobby.id)
    db.closeDatabase()
    return f"Hobby with ID {hobby_id} was updated"


# Friend
def addFriend(user_id, friend_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getUser(friend_id)
    if not items:
        return f"User with ID {friend_id} was not found"

    items = db.getFriend(user_id, friend_id)
    if items:
        return f"Already exists"

    db.insertFriend(user_id, friend_id)
    db.closeDatabase()
    return f"User with ID {friend_id} was added to your list of friends"

def removeFriend(user_id, friend_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getUser(friend_id)
    if not items:
        return f"User with ID {friend_id} was not found"

    db.removeFriend(user_id, friend_id)
    db.closeDatabase()
    return f"User with ID {friend_id} was removed from your list of friends"

def getFriend(user_id, friend_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getUser(friend_id)
    if not items:
        return f"User with ID {friend_id} was not found"

    friend = db.getFriend(user_id, friend_id)
    if not friend:
        return f"User with ID {friend_id} is not your friend"

    friend = u.tupleToUser(friend[0])

    db.closeDatabase()
    return friend

def getFriends(user_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getFriends(user_id)
    db.closeDatabase()
    if not items:
        return f"You don't have any friends"

    friends = []
    for item in items:
        friends.append(u.tupleToUser(item))

    return friends


# user event
def addUserToEvent(user_id, event_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getEvent(event_id)
    if not items:
        return f"Event with ID {event_id} was not found"

    items = db.getUserEvent(user_id, event_id)
    if items:
        return f"Already exists"

    db.insertUserEvent(user_id, event_id)
    db.closeDatabase()
    return f"User with ID {user_id} was added to event with ID{event_id}"

def removeUserFromEvent(user_id, event_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getEvent(event_id)
    if not items:
        return f"Event with ID {event_id} was not found"

    db.removeUserEvent(user_id, event_id)
    db.closeDatabase()
    return f"User with ID {user_id} was removed from event with ID {event_id}"

def getUserInEvent(user_id, event_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getEvent(event_id)
    if not items:
        return f"Event with ID {event_id} was not found"

    user_event = db.getUserEvent(user_id, event_id)
    if not user_event:
        return f"User with ID {user_id} is not in the event with ID {event_id}"

    user = u.tupleToUser(user_event[0])

    db.closeDatabase()
    return user


def getEventInUser(user_id, event_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getEvent(event_id)
    if not items:
        return f"Event with ID {event_id} was not found"

    event_user = db.getEventUser(user_id, event_id)
    if not event_user:
        return f"Event with ID {event_id} does not have the user with ID {user_id}"

    event = e.tupleToEvent(event_user[0])

    db.closeDatabase()
    return event

def getEventsInUser(user_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getUserEvents(user_id)
    db.closeDatabase()
    if not items:
        return f"You don't have any events"

    events = []
    for item in items:
        events.append(e.tupleToEvent(item))

    return events

def getUsersInEvent(event_id):
    db.openDatabase()
    items = db.getEvent(event_id)
    if not items:
        return f"Event with ID {event_id} was not found"

    items = db.getEventUsers(event_id)
    db.closeDatabase()
    if not items:
        return f"Event {event_id} does not contain any users"

    users = []
    for item in items:
        users.append(u.tupleToUser(item))

    return users


# user hobby
def addHobbyToUser(user_id, hobby_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getHobby(hobby_id)
    if not items:
        return f"Hobby with ID {hobby_id} was not found"

    items = db.getUserHobby(user_id, hobby_id)
    if items:
        return f"Already exists"

    db.insertUserHobby(user_id, hobby_id)
    db.closeDatabase()
    return f"Hobby with ID {hobby_id} was added to user with ID{user_id}"

def removeHobbyFromUser(user_id, hobby_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getHobby(hobby_id)
    if not items:
        return f"Hobby with ID {hobby_id} was not found"

    db.removeUserHobby(user_id, hobby_id)
    db.closeDatabase()
    return f"Hobby with ID {hobby_id} was removed from user with ID {user_id}"

def getHobbyInUser(user_id, hobby_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getHobby(hobby_id)
    if not items:
        return f"Hobby with ID {hobby_id} was not found"

    hobby_user = db.getUserHobby(user_id, hobby_id)
    if not hobby_user:
        return f"User with ID {user_id} does not have hobby with ID {hobby_id}"

    hobby = h.tupleToHobby(hobby_user[0])

    db.closeDatabase()
    return hobby

def getHobbiesInUser(user_id):
    db.openDatabase()
    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getUserHobbies(user_id)
    db.closeDatabase()
    if not items:
        return f"You don't have any hobbies"

    hobbies = []
    for item in items:
        hobbies.append(h.tupleToHobby(item))

    return hobbies


# Other functionalities
# Register user
def registerUser(user):
    db.openDatabase()
    items = db.checkRegisteredUser(user)
    if items:
        return f"User already exists"

    items = db.checkExistingNickname(user)
    if items:
        return f"Nickname {user.nickname} already exists"

    items = db.checkExistingEmail(user)
    if items:
        return f"Email {user.email} is already in use"

    user_id = db.registerUser(user)
    db.closeDatabase()
    user.id = user_id
    return user


# Log-in user
def loginUser(email, password):
    db.openDatabase()
    items = db.loginUser(email, password)
    db.closeDatabase()

    if not items:
        return f"Your email or password is incorrect"

    user = u.tupleToUser(items[0])
    return user

# Get all the users in given event except the logged-in user
def getUsersBasedOnHobbies(event_id, user_id):
    db.openDatabase()
    items = db.getEvent(event_id)
    if not items:
        return f"Event with ID {event_id} was not found"

    items = db.getUser(user_id)
    if not items:
        return f"User with ID {user_id} was not found"

    items = db.getUsersBasedOnHobbies(event_id, user_id)
    db.closeDatabase()
    if not items:
        return f"Event {event_id} does not contain any users"

    users = []
    for item in items:
        users.append(u.tupleToFriend(item))

    return users