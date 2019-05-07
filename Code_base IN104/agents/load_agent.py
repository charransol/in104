__author__ = "Florence Carton"

import sys
from agents.Agentpassirandom import Agentpassirandom
from agents.Agentremontecarlo import Agentremontecarlo




def make_agent(agent_name, params):

	list_agent = {
	'Agentremontecarlo':Agentremontecarlo(params)
	}

	try:
		agent = list_agent[agent_name]
	except:
		print('agent_name not found')
		sys.exit()

	return agent

