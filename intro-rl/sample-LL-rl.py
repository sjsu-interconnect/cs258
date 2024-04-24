import gymnasium as gym
from ray.rllib.algorithms.ppo import PPOConfig

config = PPOConfig()
config = config.training(gamma=0.9, lr=0.01, kl_coeff=0.3, train_batch_size=128)
config = config.resources(num_gpus=0)
config = config.rollouts(num_rollout_workers=1)

# Build a Algorithm object from the config and run 1 training iteration.
algo = config.build(env="CartPole-v1")

for _ in range(50):
    algo.train()


env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()

total = 0
for _ in range(1000):
    action = algo.compute_single_action(observation)
    observation, reward, terminated, truncated, info = env.step(action)
    total += reward

    if terminated or truncated:
        observation, info = env.reset()
        print(total)
        total = 0