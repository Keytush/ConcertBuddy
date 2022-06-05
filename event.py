def tupleToEvent(event_tuple):
    event = Event(event_tuple[1], event_tuple[2], event_tuple[3], event_tuple[4])
    event.id = event_tuple[0]

    return event


class Event:
    def __init__(self, name, date, place, description):
        self.id = None
        self.name = name
        self.date = date
        self.place = place
        self.description = description

        # self.users = []


    def editEvent(self, name, date, place, description):
        self.name = name
        self.date = date
        self.place = place
        self.description = description
