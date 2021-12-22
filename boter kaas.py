from bke import MLAgent, is_winner, opponent, train, load, start, save, validate, RandomAgent, plot_validation
 
 
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

winners = defaultdict(int)
validation_agent = RandomAgent()
for i in range(100):
    winner = start(player_x=my_agent, player_o=validation_agent, ui=HEADLESS)
    winners[winner] += 1
winners[PLAYER_X] = winners[PLAYER_X] / 100
winners[PLAYER_O] = winners[PLAYER_O] / 100
winners[None] = winners[None] / 100

validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
plot_validation(validation_result)