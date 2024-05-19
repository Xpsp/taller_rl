import gymnasium as gym

env = gym.make('FrozenLake-v1', map_name='8x8', is_slippery=False, render_mode='human')
obs, _ = env.reset()
for _ in range(10):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, _ = env.step(action)
    env.render()
    if terminated or truncated:
        break