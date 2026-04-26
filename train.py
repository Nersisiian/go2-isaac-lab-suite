import hydra
import torch
import wandb
from omegaconf import DictConfig, OmegaConf
from rsl_rl.algorithms import PPO
from rsl_rl.modules import ActorCritic
from rsl_rl.runners import OnPolicyRunner

from isaaclab_rl.rsl_rl import RslRlVecEnvWrapper
from go2_extreme.tasks import make_env

@hydra.main(version_base=None, config_path="configs", config_name="default")
def main(cfg: DictConfig):
    
    print(OmegaConf.to_yaml(cfg))

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    env_cfg = cfg.task.environment
    env = make_env(env_cfg)
    env = RslRlVecEnvWrapper(env)

    actor_critic = ActorCritic(
        num_obs=env.num_observations,
        num_actions=env.num_actions,
        **cfg.policy,
    ).to(device)

    algorithm = PPO(actor_critic, **cfg.algorithm)

    runner = OnPolicyRunner(env, algorithm, cfg.train, device=device)

    if cfg.wandb.enable:
        wandb.init(
            project=cfg.wandb.project,
            name=cfg.wandb.run_name,
            config=OmegaConf.to_container(cfg, resolve=True),
        )

    runner.learn(num_learning_iterations=cfg.train.max_iterations)

    # Save final policy
    torch.save(actor_critic.state_dict(), "policies/final_policy.pt")
    print("Training finished. Policy saved to policies/final_policy.pt")

if __name__ == "__main__":
    main()