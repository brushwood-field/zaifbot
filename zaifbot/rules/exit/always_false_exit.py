from zaifbot.rules.exit.base import Exit


class AlwaysFalseExit(Exit):
    def __init__(self, name=None):
        super().__init__(name=name)

    def can_exit(self, trade):
        return False
