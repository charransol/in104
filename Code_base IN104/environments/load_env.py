__author__ = "Florence Carton"

import sys
from environments.EnvironmentGrid1D import EnvironmentGrid1D
from environments.EnvironmentGrid2D import EnvironmentGrid2D


def make_env(env_name, params):

	list_environments = {
	'EnvironmentGrid2D':EnvironmentGrid2D(params)
	}

	try:
		env = list_environments[env_name]
	except:
		print('env_name not found')
		sys.exit()

	return env

