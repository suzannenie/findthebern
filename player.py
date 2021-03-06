from tabulate import tabulate


class Player:
    def __init__(self, name, sid):
        self.name = name
        self.sid = sid
        self.points = 0
        self.index = -1

    def to_html(self):
        return "<p>You (" + self.name + ") have " + str(self.points) + " " \
                                                                "points</p><br>"


class Players:
    def __init__(self):
        # always sorted by points: highest to lowest
        self.players = []

    def insertPlayer(self, p):
        p.index = len(self.players)
        self.players.append(p)

    def checkIndices(self):
        for i, p in enumerate(self.players):
            if p.index != i:
                return False
        return True

    def removePlayer(self, p):
        for i in range(p.index + 1, len(self.players)):
            player = self.players[i]
            player.index -= 1
        removed = self.players.pop(p.index)
        assert(self.checkIndices())

    def reSort(self, winner):
        winner.points += 1
        i = winner.index
        while i > 0:
            prev = self.players[i - 1]
            if winner.points <= prev.points:
                break
            self.players[i - 1] = winner
            winner.index = i - 1
            self.players[i] = prev
            prev.index = i
            i -= 1
        assert self.checkIndices()

    def toTable(self):
        headers = ["rank", "name", "points"]
        table = [headers]
        end = min(len(self.players), 5)
        for i in range(end):
            l = [i+1, self.players[i].name, self.players[i].points]
            table.append(l)
        return tabulate(table, tablefmt='html')


class Solo:
    def __init__(self, name, date, time):
        self.name = name
        self.time = time
        self.date = date


class TopThree:
    def __init__(self):
        self.top = []

    def insert(self, solo):
        length = len(self.top)
        self.top.append(solo)
        i = length
        while i > 0:
            prev = self.top[i - 1]
            if solo.time >= prev.time:
                break
            self.top[i - 1] = solo
            self.top[i] = prev
            i -= 1
        if length == 3:
            self.top = self.top[:3]

    def toTable(self):
        headers = ["rank", "name", "date", "time"]
        table = [headers]
        end = min(len(self.top), 3)
        for i in range(end):
            l = [i+1, self.top[i].name, self.top[i].date, self.top[i].time]
            table.append(l)
        return tabulate(table, tablefmt='html')
