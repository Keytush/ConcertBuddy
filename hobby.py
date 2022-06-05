def tupleToHobby(hobby_tuple):
    hobby = Hobby(hobby_tuple[1], hobby_tuple[2])
    hobby.id = hobby_tuple[0]

    return hobby


class Hobby:
    def __init__(self, name, description):
        self.id = None
        self.name = name
        self.description = description

        # self.user = None


    def editHobby(self, name, description):
        self.name = name
        self.description = description
