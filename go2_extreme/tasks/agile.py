from .locomotion import Go2WalkEnvCfg
from isaaclab.managers import RewardTermCfg

class Go2JumpEnvCfg(Go2WalkEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.terrain.terrain_type = "pyramid_stairs"
        self.episode_length_s = 10.0
        self.rewards["jump_height"] = RewardTermCfg(weight=50.0, term="jump_apex")
        self.rewards["feet_air_time"] = RewardTermCfg(weight=2.0, term="air_time")

class Go2BackflipEnvCfg(Go2WalkEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.episode_length_s = 5.0
        self.rewards = {
            "flip_progress": RewardTermCfg(weight=1000.0, term="backflip_angle"),
            "forward_vel": RewardTermCfg(weight=10.0, term="track_lin_vel"),
            "torque_cost": RewardTermCfg(weight=-0.0001, term="torque"),
            "fall_penalty": RewardTermCfg(weight=-500.0, term="fall"),
        }