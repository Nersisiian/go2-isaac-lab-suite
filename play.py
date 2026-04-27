#!/usr/bin/env python3
"""
Play (visualize) a trained policy with high-quality rendering and video recording.
"""

import argparse
import torch
import numpy as np
import cv2
from omegaconf import OmegaConf
from isaaclab_rl.rsl_rl import RslRlVecEnvWrapper
from go2_extreme.tasks import make_env

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=str, required=True, help="Path to .pt policy file")
    parser.add_argument("--task", type=str, default="go2_walk", help="Task name")
    parser.add_argument("--rendering", action="store_true", help="Enable viewer")
    parser.add_argument("--num_episodes", type=int, default=1)
    parser.add_argument("--record_video", action="store_true", help="Save MP4 of first episode")
    parser.add_argument("--fps", type=int, default=30, help="Video frame rate")
    args = parser.parse_args()

    # Load config (simplified)
    from go2_extreme.tasks.locomotion import Go2WalkEnvCfg
    env_cfg = Go2WalkEnvCfg()
    # Enable RTX rendering if requested and available
    if args.rendering:
        env_cfg.sim.render_mode = "gui"
        env_cfg.sim.use_rtx = True       # RTX shadows/reflections
        env_cfg.sim.rendering_resolution = (1920, 1080)

    env = make_env(env_cfg)
    env = RslRlVecEnvWrapper(env)

    # Load policy
    actor_critic = torch.load(args.checkpoint, map_location="cpu")
    env.unwrapped.set_actor_critic(actor_critic)

    # Video recording
    video_writer = None
    if args.record_video:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter('demo_walk.mp4', fourcc, args.fps, (1920, 1080))

    obs = env.reset()
    for episode in range(args.num_episodes):
        step = 0
        while True:
            actions = actor_critic.act_inference(obs)
            obs, _, dones, _ = env.step(actions)

            # Capture frame if rendering and recording
            if args.rendering and args.record_video:
                # Note: env.render() returns RGB numpy array
                frame = env.render(mode="rgb_array")
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                video_writer.write(frame)

            step += 1
            if dones.any():
                obs = env.reset()
                break

    if video_writer:
        video_writer.release()
        print("Video saved to demo_walk.mp4")

if __name__ == "__main__":
    main()
