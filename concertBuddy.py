from flask import Flask, jsonify
from flask_restx import Api, reqparse, Resource

from app_json_utils import AppJsonEncoder
from user import User
from event import Event
from hobby import Hobby
import app as my_app


cbuddy_app = Flask(__name__)
cbuddy_app.json_encoder = AppJsonEncoder
cbuddy_api = Api(cbuddy_app)

# User parser
user_parser = reqparse.RequestParser()
user_parser.add_argument('nickname', type = str, required = True)
user_parser.add_argument('email', type = str, required = True)
user_parser.add_argument('password', type = str, required = True)
user_parser.add_argument('gender', type = str, required = False)
user_parser.add_argument('birth_date', type = str, required = False)
user_parser.add_argument('country', type = str, required = False)
user_parser.add_argument('description', type = str, required = False)

edit_user_parser = reqparse.RequestParser()
edit_user_parser.add_argument('gender', type = str, required = False)
edit_user_parser.add_argument('birth_date', type = str, required = False)
edit_user_parser.add_argument('country', type = str, required = False)
edit_user_parser.add_argument('description', type = str, required = False)

register_user_parser = reqparse.RequestParser()
register_user_parser.add_argument('nickname', type = str, required = True)
register_user_parser.add_argument('email', type = str, required = True)
register_user_parser.add_argument('password', type = str, required = True)

login_user_parser = reqparse.RequestParser()
login_user_parser.add_argument('email', type = str, required = True)
login_user_parser.add_argument('password', type = str, required = True)


# Event parser
event_parser = reqparse.RequestParser()
event_parser.add_argument('name', type = str, required = True)
event_parser.add_argument('date', type = str, required = True)
event_parser.add_argument('place', type = str, required = True)
event_parser.add_argument('description', type = str, required = False)


# Hobby parser
hobby_parser = reqparse.RequestParser()
hobby_parser.add_argument('name', type = str, required = True)
hobby_parser.add_argument('description', type = str, required = False)


# APIs for user
@cbuddy_api.route('/user')
class AddUserAPI(Resource):
    @cbuddy_api.doc(parser = user_parser)
    # Add a user
    def post(self):
        """
        Insert a user through API to database.
        :return: The inserted user object
        """
        # get the post parameters
        args = user_parser.parse_args()

        # Create a new user object
        new_user = User(args['nickname'], args['email'], args['password'],
                        args['gender'],args['birth_date'], args['country'], args['description'])
        user = my_app.addUser(new_user)

        return jsonify(user)



@cbuddy_api.route('/user/<user_id>')
class UserIdAPI(Resource):
    # Get specific user
    def get(self, user_id):
        """
        Get user from database based on the user's id
        :param user_id: The id of user we are looking for
        :return: The user object
        """
        get_user = my_app.getUser(user_id)
        return jsonify(get_user)

    # Remove specific user
    def delete(self, user_id):
        """
        Remove user from database based on the user's id
        :param user_id: The id of user we are looking for
        :return: A string message
        """
        message = my_app.removeUser(user_id)
        return jsonify(message)

    @cbuddy_api.doc(parser = edit_user_parser)
    def patch(self, user_id):
        """
        Edit user's optional attributes
        :param user_id: The id of user we are looking for
        :return: A string message
        """
        args = edit_user_parser.parse_args()

        message = my_app.updateUser(args['gender'],
                                    args['birth_date'], args['country'],
                                    args['description'], user_id)
        return jsonify(message)


@cbuddy_api.route('/users')
class AllUsersAPI(Resource):
    def get(self):
        """
        Get all the users in a user table
        :return: List of user objects
        """
        users = my_app.getUsers()
        return jsonify(users)


# Event
@cbuddy_api.route('/event')
class AddEventAPI(Resource):
    @cbuddy_api.doc(parser = event_parser)
    def post(self):
        """
        Insert an event through API to database.
        :return: Inserted event object
        """
        # get the post parameters
        args = event_parser.parse_args()

        # Create a new event object
        new_event = Event(args['name'], args['date'], args['place'], args['description'])
        event = my_app.addEvent(new_event)

        return jsonify(event)


@cbuddy_api.route('/event/<event_id>')
class EventIdAPI(Resource):
    def get(self, event_id):
        """
        Get event based on event's id
        :param event_id: An id of event we are looking for
        :return: Event object
        """
        get_event = my_app.getEvent(event_id)
        return jsonify(get_event)

    def delete(self, event_id):
        """
        Remove an event from database based on event's id
        :param event_id: An id of event we are looking for
        :return: String message
        """
        message = my_app.removeEvent(event_id)
        return jsonify(message)

    @cbuddy_api.doc(parser = event_parser)
    def patch(self, event_id):
        """
        Edit event based on event's id
        :param event_id: An id of event we are looking for
        :return: String message
        """
        args = event_parser.parse_args()

        message = my_app.updateEvent(args['name'], args['date'],
                                     args['place'], args['description'], event_id)
        return jsonify(message)


@cbuddy_api.route('/events')
class AllEventsAPI(Resource):
    def get(self):
        """
        Get all the events from event table
        :return: List of event objects
        """
        events = my_app.getEvents()
        return jsonify(events)


# Hobby
@cbuddy_api.route('/hobby')
class AddHobbyAPI(Resource):
    @cbuddy_api.doc(parser = hobby_parser)
    def post(self):
        """
        Insert a hobby through API to database.
        :return: Inserted hobby
        """
        # get the post parameters
        args = hobby_parser.parse_args()

        # Create a new hobby object
        new_hobby = Hobby(args['name'], args['description'])
        hobby = my_app.addHobby(new_hobby)

        return jsonify(hobby)


@cbuddy_api.route('/hobby/<hobby_id>')
class HobbyIdAPI(Resource):
    def get(self, hobby_id):
        """
        Get hobby based on hobby's id
        :param hobby_id: An id of hobby we are looking for
        :return: Hobby object
        """
        get_hobby = my_app.getHobby(hobby_id)
        return jsonify(get_hobby)

    def delete(self, hobby_id):
        """
        Remove hobby based on hobby's id
        :param hobby_id: An id of hobby we are looking for
        :return: String message
        """
        message = my_app.removeHobby(hobby_id)
        return jsonify(message)

    @cbuddy_api.doc(parser = hobby_parser)
    def patch(self, hobby_id):
        """
        Edit hobby based on hobby's id
        :param hobby_id: An id of hobby we are looking for
        :return: String message
        """
        args = hobby_parser.parse_args()
        message = my_app.updateHobby(args['name'], args['description'], hobby_id)
        return jsonify(message)


@cbuddy_api.route('/hobbies')
class AllHobbiesAPI(Resource):
    def get(self):
        """
        Get all hobbies from hobby list
        :return: List of hobby objects
        """
        hobbies = my_app.getHobbies()
        return jsonify(hobbies)


# Friends
@cbuddy_api.route('/user/<user_id>/befriend/<friend_id>')
class FriendAPI(Resource):
    def post(self, user_id, friend_id):
        """
        Insert a user's id and other user's id into friend relational table
        :param user_id: An id of logged-in user
        :param friend_id: An id of user, logged-in user wish to befriend
        :return: String message
        """
        message = my_app.addFriend(user_id, friend_id)
        return jsonify(message)

    def delete(self, user_id, friend_id):
        """
        Remove a user's id and other user's id into friend relational table
        :param user_id: An id of logged-in user
        :param friend_id: An id of user's friend
        :return: String message
        """
        message = my_app.removeFriend(user_id, friend_id)
        return jsonify(message)

    def get(self, user_id, friend_id):
        """
        Get a user's  friend based on both user's ids
        :param user_id: An id of logged-in user
        :param friend_id: An id of user's friend
        :return: User object, which is logged-in user's friend
        """
        friend = my_app.getFriend(user_id, friend_id)
        return jsonify(friend)


@cbuddy_api.route('/user/<user_id>/befriend/friends')
class FriendAPI(Resource):
    def get(self, user_id):
        """
        Get all user's  friends
        :param user_id: An id of logged-in user
        :return: List of user objects, which are logged-in user's friends
        """
        friends = my_app.getFriends(user_id)
        return jsonify(friends)


# User Event
@cbuddy_api.route('/user/<user_id>/attends/<event_id>')
class UserEventAPI(Resource):
    def post(self, user_id, event_id):
        message = my_app.addUserToEvent(user_id, event_id)
        return jsonify(message)

    def delete(self, user_id, event_id):
        message = my_app.removeUserFromEvent(user_id, event_id)
        return jsonify(message)

    def get(self, user_id, event_id):
        event = my_app.getEventInUser(user_id, event_id)
        return jsonify(event)


@cbuddy_api.route('/user/<user_id>/attends/events')
class UserEventsAPI(Resource):
    def get(self, user_id):
        events = my_app.getEventsInUser(user_id)
        return jsonify(events)


@cbuddy_api.route('/event/<event_id>/has/<user_id>')
class UserEventAPI(Resource):
    def get(self, event_id, user_id):
        user = my_app.getUserInEvent(user_id, event_id)
        return jsonify(user)


@cbuddy_api.route('/event/<event_id>/has/users')
class UsersEventAPI(Resource):
    def get(self, event_id):
        users = my_app.getUsersInEvent(event_id)
        return jsonify(users)


# @cbuddy_api.route('/event/<event_id>/has/users/<user_id>')
# class UsersEventAPI(Resource):
#     def get(self, event_id, user_id):
#         """
#         Get all the users in given event except the logged-in user
#         :param event_id:
#         :param user_id:
#         :return:
#         """
#         users = my_app.getUsersBasedOnHobbies(event_id, user_id)
#         return jsonify(users)


# User Hobby
@cbuddy_api.route('/user/<user_id>/has/<hobby_id>')
class UserHobbyAPI(Resource):
    def post(self, user_id, hobby_id):
        message = my_app.addHobbyToUser(user_id, hobby_id)
        return jsonify(message)

    def delete(self, user_id, hobby_id):
        message = my_app.removeHobbyFromUser(user_id, hobby_id)
        return jsonify(message)

    def get(self, user_id, hobby_id):
        hobby = my_app.getHobbyInUser(user_id, hobby_id)
        return jsonify(hobby)


@cbuddy_api.route('/user/<user_id>/has/hobbies')
class UserHobbiesAPI(Resource):
    def get(self, user_id):
        hobbies = my_app.getHobbiesInUser(user_id)
        return jsonify(hobbies)


# Other functionalities
# Register user
@cbuddy_api.route('/user/register')
class RegisterUserAPI(Resource):
    @cbuddy_api.doc(parser = register_user_parser)
    # Add a user
    def post(self):
        # get the post parameters
        args = register_user_parser.parse_args()

        # Create a new user object
        new_user = User(args['nickname'], args['email'], args['password'])
        user = my_app.registerUser(new_user)

        return jsonify(user)


# Log-in user
@cbuddy_api.route('/user/login')
class LoginUserAPI(Resource):
    @cbuddy_api.doc(parser = login_user_parser)
    # Add a user
    def get(self):
        # get the post parameters
        args = login_user_parser.parse_args()
        user = my_app.loginUser(args['email'], args['password'])
        return jsonify(user)



if __name__ == '__main__':
    cbuddy_app.run(debug=False, port=7890)