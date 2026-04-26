from omegaconf import DictConfig
from isaaclab.envs import ManagerBasedRLEnv

from .locomotion import Go2WalkEnvCfg
from .agile import Go2JumpEnvCfg, Go2BackflipEnvCfg
from .recovery import Go2RecoveryEnvCfg
from .manipulation import Go2ManipulateEnvCfg

def make_env(cfg: DictConfig) -> ManagerBasedRLEnv:
    """Factory to create environment from config."""
    task_name = cfg.get("name", "go2_walk")
    if task_name == "go2_walk":
        return ManagerBasedRLEnv(Go2WalkEnvCfg())
    elif task_name == "go2_jump":
        return ManagerBasedRLEnv(Go2JumpEnvCfg())
    elif task_name == "go2_backflip":
        return ManagerBasedRLEnv(Go2BackflipEnvCfg())
    elif task_name == "go2_recovery":
        return ManagerBasedRLEnv(Go2RecoveryEnvCfg())
    elif task_name == "go2_manipulate":
        return ManagerBasedRLEnv(Go2ManipulateEnvCfg())
    else:
        raise ValueError(f"Unknown task: {task_name}")