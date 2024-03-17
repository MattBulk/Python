from MyFirstClass import *

class MyFirstInHer(MyFirstClass):

    def __init__(self, num_team, position, team_name):
        super().__init__(num_team, position)
        self.team_name = team_name

    def my_class_method(self):
        print('I override this method')