import random

from bke import MLAgent, is_winner, opponent, train, load, start, save, validate, RandomAgent, plot_validation, train_and_plot
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
random.seed(1)
my_agent = MyAgent()
   
random_agent = RandomAgent()
#train(my_agent, 3000)
#save(my_agent, 'MyAgent_3000')
train_and_plot(
agent=my_agent,
validation_agent=random_agent,
iterations=50,
trainings=100,
validations=1000)

my_agent = MyAgent(alpha=0.2, epsilon=0.8)

#my_agent = load('MyAgent_3000')
#my_agent.learning = False
 
#start(player_x=my_agent)

validation_agent = RandomAgent()

validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
plot_validation(validation_result)