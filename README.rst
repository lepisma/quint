quint
-----

*No hassle Q-learning library*

Quint is a minimal path finding library useful for discrete state scenarios

Usage
*****

* Install : ``pip install quint``
*	Import : ``from quint import quint``
*	Instantiate : ``model = quint(reward_matrix, gamma)`` (refer quint docstring for matrix structure)
* Override quint.act() to your own action function
*	Learn : ``model.learn(final_state, iterations)``
* Trace : ``model.find_optimum_path(from_state)``


MIT License

Copyright (C) 2014 Abhinav Tushar