#!/usr/bin/env python3
"""
Evaluate policy over multiple episodes and report aggregated metrics.
"""

import argparse
import torch
import numpy as np
from tqdm import tqdm
from isaaclab_rl.rsl_rl import RslRlVecEnvWrapper
from go2_extreme.tasks import make_env
from go2_extreme.tasks.locomotion import Go2WalkEnvCfg

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--task", type=str, default="go2_walk")
    parser.add_argument("--num_episodes", type=int, default=50)
    args = parser.parse_args()

    env_cfg = Go2WalkEnvCfg()
    env = make_env(env_cfg)
    env = RslRlVecEnvWrapper(env)

    actor_critic = torch.load(args.checkpoint, map_location="cpu")
    env.unwrapped.set_actor_critic(actor_critic)

    episode_rewards = []
    for _ in tqdm(range(args.num_episodes)):
        obs = env.reset()
        done = False
        ep_reward = 0.0
        while not done:
            actions = actor_critic.act_inference(obs)
            obs, rewards, dones, _ = env.step(actions)
            ep_reward += rewards.mean().item()
            done = dones.any()
        episode_rewards.append(ep_reward)

    print(f"Mean reward over {args.num_episodes} episodes: {np.mean(episode_rewards):.2f} ± {np.std(episode_rewards):.2f}")

if __name__ == "__main__":
    main()