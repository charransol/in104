__author__ = "Florence Carton"
__credits__ = ["Florence Carton", "Freek Stulp", "Antonin Raffin"]


from params import default_params
from environments.load_env import make_env
from agents.load_agent import make_agent
import matplotlib.pyplot as pyplot

import argparse



def runEpisode(environment, agent, max_action_per_episode,render=False, debug= False):
    """Run one episode.

    Integrate the environment-agent loop until a terminal state is reached,
    or a maximum number of actions.

    Args:
        environment (Environment): An environment
        agent (Agent): An agent
        max_action_per_episode (int): Maximum number of actions before an episode
            is terminated.
        render (bool) : to display learning
        debug (bool) : display debug information

    Returns:
        The return of the episode, i.e. the sum over all the rewards.
    """

    # Initialize and first state
    state =  environment.reset()

    # Print output
    if debug:
        print(" INIT")

    # Get action for first step
    action = agent.start(state)

    is_done = False
    reward       = 0.0
    total_reward = 0.0
    num_actions  = 0

    while (not is_done) and (num_actions<max_action_per_episode):

        # To display 
        if render:
             environment.render()
        prev_state=state
        # Update the state, and get the reward and next state
        state,reward, is_done = environment.step(action)
    
        total_reward += reward

        # Print output
        if debug : 
            print("  r=",reward)    # Print reward
            print(" state=", state) # Print state
        

        # Get the next action for this state
        action = agent.step(reward,state,prev_state,action, is_done)

        num_actions += 1

    # if render:
    #     environment.render()
    
    return total_reward


# This is where the script will start executing
if __name__ == "__main__":

    params = default_params()

    parser = argparse.ArgumentParser()

    parser.add_argument("--render", help="True for display", default=True)

    parser.add_argument("--debug", help="True for display debug info", default=False)

    parser.add_argument("--env", help="get the environment")

    parser.add_argument("--agent", help="get the agent")

    args = parser.parse_args()

    if args.env != None:
        params['env'] = args.env

    if args.agent != None:
        params['agent'] = args.agent

    env_name = params['env']

    agent_name = params['agent']

    environment = make_env(env_name, params)

    params['num_states'] = environment.num_states
    params['num_actions'] = environment.num_actions


    agent = make_agent(agent_name, params)

    y_rewards = []
    nb_episode = []

    # Run episodes

    for episode in range(params['num_training_episodes']):
        if (episode%1000==0):    
            print("Episode ",episode,"starting.")

        render = args.render and episode % 1000 == 0 and episode!=0# to display every 100 episodes

        total_reward = runEpisode(environment, agent, 
                        params['max_action_per_episode'], 
                        render, args.debug)

        if env_name == 'EnvironmentDiscreteCartpole':
            agent.update(episode)

        y_rewards.append(total_reward)
        nb_episode.append(episode)
        #print (agent.q) #affiche les matrices 
        if (episode%1000==0):    
            print("Episode ",episode," done. Total reward: ",total_reward)
            print("_______________________________")

    environment.close()

    #Plot the learning curve
    pas=100
    ymoy=[]
    xmoy=[]
    for i in range(params['num_training_episodes']//pas-1):
        a=0
        m=0
        for k in range(pas):
            a=y_rewards[i*pas+k]
            m+=a
        m=m/pas
        ymoy.append(m)
        xmoy.append(nb_episode[pas*i])
    axes = pyplot.gca()
    axes.set_xlim([0, params['num_training_episodes']])
    axes.set_ylim([-100, max(y_rewards)])
    pyplot.plot(xmoy, ymoy)
    #pyplot.plot(nb_episode, y_rewards)
    pyplot.show()









    


	



