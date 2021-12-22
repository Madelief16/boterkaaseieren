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
    
print("1: train de computer \n 2: speel tegen een getrainde computer \n 3: je kan tegen ander persoon \n 4:kijk hoe goed die het doet \n Kies wat je wilt spelen:")
choice = input()

if choice == '1':
    my_agent = MyAgent()
    print("Wat vind jij een mooie naam voor je agent?")
    name = input()
    
    
if choice == '2':
     print("Tegenover welke agent zou je willen spelen? Op het moment dat je tegen de agent van dit programma wil spelen, vul in: agent1")
     play_agent = input()

     my_agent = load('playagent')
     my_agent.learning = False
     start(player_x=my_agent)

  
  
if choice == '3':
    start()
    
if choice == '4':
  random_agent = RandomAgent() 
  
  
  train(my_agent, 3000)
  save(my_agent, 'MyAgent_3000')
 
 
 
random.seed(1)
my_agent = MyAgent()
   
random_agent = RandomAgent()

my_agent = MyAgent(alpha=0.2, epsilon=0.8)


train_and_plot(
agent=my_agent,
validation_agent=random_agent,
iterations=50,
trainings=100,
validations=1000)




validation_agent = RandomAgent()

validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
plot_validation(validation_result)