"""
The main code implementing simple matrix Q-learning
"""

import numpy as np
import random

class quint:
	"""
	The class for creating a Q-learning system
	"""
	
	def __init__(self, reward_matrix, gamma, not_allowed_action = -1):
		"""
		Initializes a learner using the reward matrix
		
		Reward Matrix structure
		-----------------------
		Columns represent actions
		Rows represent states
		Values inside represent reward
		
		not_allowed_action reward value represent the action that are not allowed in the situation
		"""
		
		self.reward_matrix = reward_matrix
		self.gamma = gamma
		self.not_allowed_action = not_allowed_action
		self.q_matrix = np.zeros(reward_matrix.shape) # Setting all q values to 0
		
	def learn(self, goal_state, iterations):
		"""
		Learns the optimum path to goal_state and updates the q_matrix
		"""
		
		for x in range(iterations):
			initial_state = random.choice(range(self.reward_matrix.shape[0]))
			
			while initial_state != goal_state:
			# While we reach our goal
				actions = self.reward_matrix[initial_state]
				
				initial_action = random.choice(actions)
				
				while initial_action == self.not_allowed_action:
					initial_action = random.choice(actions)
				
				initial_action = np.where(actions == initial_action)[0][0]
					
				next_state = self.act(initial_state, initial_action)
				
				# update q matrix
				self.q_matrix[initial_state, initial_action] = self.reward_matrix[initial_state, initial_action] + self.gamma * self.max_q(next_state)
				
				initial_state = next_state
			
	def act(self, current_state, action):
		"""
		Performs action on current state and returns the resulting state
		
		* Assuming action number 'x' takes to state 'x'
		* Override this method to implement your own actions
		"""
		
		return action
		
	def max_q(self, state):
		"""
		Returns the maximum q value available in the given state considering all action
		"""
		
		max_q = 0
		
		actions = self.reward_matrix[state]
		for action_id in range(len(actions)):
			if actions[action_id] != self.not_allowed_action:
				if self.q_matrix[state, action_id] > max_q:
					max_q = self.q_matrix[state, action_id]
		
		return max_q
		
	def normalize(self):
		"""
		Normalizes the q values
		"""
		
		max_value = float(self.q_matrix.max())
		self.q_matrix /= max_value
		
	def find_optimum_path(self, state):
		"""
		Returns the actions (and corresponding states) to follow to reach goal_state from given state
		"""
		
		actions = []
		states = [state]
		
		while state != goal_state:
			action = np.where(self.q_matrix[state] == self.max_q(state))[0][0]
			actions.append(action)
			
			state = self.act(state, action)
			states.append(state)
			
		return actions, states