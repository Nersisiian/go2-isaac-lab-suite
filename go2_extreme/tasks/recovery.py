from .locomotion import Go2WalkEnvCfg
from isaaclab.managers import RewardTermCfg

class Go2RecoveryEnvCfg(Go2WalkEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        # Start robot on its side or back
        self.initial_state = {"pos": (0,0,0.2), "rot": (0.7, 0, 0, 0.7)}  # tilted 90°
        self.rewards["upright"] = RewardTermCfg(weight=100.0, term="upright_orientation")
        self.rewards["stand_bonus"] = RewardTermCfg(weight=50.0, term="legs_on_ground")