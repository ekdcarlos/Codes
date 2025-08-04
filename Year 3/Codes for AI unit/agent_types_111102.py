# Model-based Reflex Agent
# Maintains an internal model of the world and uses it to make decisions
class ModelBasedReflexAgent:
    def __init__(self):
        self.model = {'room': 'dirty', 'battery': 'full'}  # Internal world model
    
    def perceive(self, environment):
        self.model['room'] = environment['room_status']
        self.model['battery'] = environment['battery_status']
    
    def act(self):
        if self.model['room'] == 'dirty' and self.model['battery'] == 'full':
            return 'clean'
        elif self.model['battery'] == 'low':
            return 'charge'
        else:
            return 'idle'

# Goal-based Agent
# Makes decisions based on achieving a specific goal
class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal  # e.g., goal = {'destination': 'B'}
    
    def perceive(self, environment):
        self.current_state = environment['current_location']
    
    def act(self):
        if self.current_state != self.goal['destination']:
            return f'move_to_{self.goal["destination"]}'
        else:
            return 'stop'

# Utility-based Agent
# Chooses actions based on a utility function
class UtilityBasedAgent:
    def __init__(self):
        self.utilities = {
            'clean_and_rest': 0.9,
            'clean_and_move': 1.0,
            'rest': 0.5,
            'move': 0.3
        }
    
    def perceive(self, environment):
        self.room_status = environment['room_status']
        self.energy_level = environment['energy_level']
    
    def act(self):
        if self.room_status == 'dirty' and self.energy_level > 50:
            return max(['clean_and_rest', 'clean_and_move'], 
                      key=lambda x: self.utilities[x])
        elif self.energy_level <= 50:
            return 'rest'
        else:
            return 'move'

# Learning Agent
# Adapts behavior based on experience
class LearningAgent:
    def __init__(self):
        self.q_table = {}  # State-action value table
        self.learning_rate = 0.1
        self.discount_factor = 0.9
    
    def perceive(self, environment):
        self.state = environment['state']
        if self.state not in self.q_table:
            self.q_table[self.state] = {'action1': 0, 'action2': 0}
    
    def act(self):
        # Choose action with highest Q-value (epsilon-greedy simplified)
        return max(self.q_table[self.state], 
                  key=self.q_table[self.state].get)
    
    def learn(self, action, reward, next_state):
        if next_state not in self.q_table:
            self.q_table[next_state] = {'action1': 0, 'action2': 0}
        
        # Q-learning update rule
        current_q = self.q_table[self.state][action]
        max_next_q = max(self.q_table[next_state].values())
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * max_next_q - current_q
        )
        self.q_table[self.state][action] = new_q

# Example usage
if __name__ == "__main__":
    # Model-based Reflex Agent
    model_agent = ModelBasedReflexAgent()
    env = {'room_status': 'dirty', 'battery_status': 'full'}
    model_agent.perceive(env)
    print(f"Model-based Reflex Agent action: {model_agent.act()}")

    # Goal-based Agent
    goal_agent = GoalBasedAgent({'destination': 'B'})
    env = {'current_location': 'A'}
    goal_agent.perceive(env)
    print(f"Goal-based Agent action: {goal_agent.act()}")

    # Utility-based Agent
    utility_agent = UtilityBasedAgent()
    env = {'room_status': 'dirty', 'energy_level': 75}
    utility_agent.perceive(env)
    print(f"Utility-based Agent action: {utility_agent.act()}")

    # Learning Agent
    learning_agent = LearningAgent()
    env = {'state': 'state1'}
    learning_agent.perceive(env)
    action = learning_agent.act()
    learning_agent.learn(action, reward=1.0, next_state='state2')
    print(f"Learning Agent action: {action}, Q-table: {learning_agent.q_table}")