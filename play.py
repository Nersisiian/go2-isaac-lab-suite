#!/usr/bin/env python3
"""
Play (visualize) a trained policy.
"""

import argparse
import torch
from omegaconf import OmegaConf
from isaaclab_rl.rsl_rl import RslRlVecEnvWrapper
from go2_extreme.tasks import make_env

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=str, required=True, help="Path to .pt policy file")
    parser.add_argument("--task", type=str, default="go2_walk", help="Task name")
    parser.add_argument("--rendering", action="store_true", help="Enable viewer")
    parser.add_argument("--num_episodes", type=int, default=1)
    args = parser.parse_args()

    # Load config (simplified)
    from go2_extreme.tasks.locomotion import Go2WalkEnvCfg
    env_cfg = Go2WalkEnvCfg()
    env = make_env(env_cfg)
    env = RslRlVecEnvWrapper(env)

    # Load policy
    actor_critic = torch.load(args.checkpoint, map_location="cpu")
    env.unwrapped.set_actor_critic(actor_critic)

    # Play loop
    obs = env.reset()
    for _ in range(args.num_episodes * int(env_cfg.episode_length_s / env_cfg.dt)):
        actions = actor_critic.act_inference(obs)
        obs, _, dones, _ = env.step(actions)
        if dones.any():
            obs = env.reset()

    print("Done.")

if __name__ == "__main__":
    main()