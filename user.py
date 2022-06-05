def tupleToUser(user_tuple):
    user = User(user_tuple[1], user_tuple[2], user_tuple[3],
                user_tuple[4], user_tuple[5], user_tuple[6], user_tuple[7])
    user.id = user_tuple[0]

    return user

def tupleToFriend(user_tuple):
    user = Friend(user_tuple[1], user_tuple[2], user_tuple[3],
                user_tuple[4], user_tuple[5], user_tuple[6], user_tuple[7], user_tuple[8])
    user.id = user_tuple[0]

    return user


class User:
    def __init__(self, nickname, email, password,
                 gender = None, birth_date = None,
                 country = None, description = None):
        self.id = None
        self.nickname = nickname
        self.email = email
        self.password = password

        self.gender = gender
        self.birth_date = birth_date
        self.country = country
        self.description = description

        # self.hobbies = []
        # self.friends = []


    def editProfile(self, gender, birth_date, country, description):
        self.gender = gender
        self.birth_date = birth_date
        self.country = country
        self.description = description

class Friend(User):
    def __init__(self, nickname, email, password,
                 gender=None, birth_date=None,
                 country=None, description=None, is_friend=False):
        self.is_friend = is_friend


