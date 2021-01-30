from tabulate import tabulate


class Player:
    def __init__(self, name, sid):
        self.name = name
        self.sid = sid
        self.points = 0
        self.index = -1


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
