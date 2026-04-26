from .locomotion import Go2WalkEnvCfg
from ..robots.go2_manipulator import Go2ManipulatorRobot

class Go2ManipulateEnvCfg(Go2WalkEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.robot = Go2ManipulatorRobot()
        # Add object of interest
        self.object_cfg = {
            "prim_path": "/World/cube",
            "size": (0.05, 0.05, 0.05),
            "mass": 0.1,
        }
        self.rewards["grasp"] = RewardTermCfg(weight=10.0, term="object_grasped")
        self.rewards["place"] = RewardTermCfg(weight=50.0, term="object_at_target")