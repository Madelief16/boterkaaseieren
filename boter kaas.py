from bke import MLAgent, is_winner, opponent, train, load, start, save
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
my_agent = MyAgent()
train(my_agent, 3000)
save(my_agent, 'MyAgent_3000')


my_agent = load('MyAgent_3000')


my_agent.learning = False
 
start(player_x=my_agent)