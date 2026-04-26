from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.managers import EventTermCfg, ObservationGroupCfg, RewardTermCfg
from isaaclab.terrains import TerrainImporterCfg
from isaaclab.sensors import ContactSensorCfg, ImuCfg
from isaaclab.actuators import ActuatorNetCfg
from ..robots.go2 import Go2Robot

class Go2WalkEnvCfg(ManagerBasedRLEnvCfg):
    """Configuration for Go2 walking on flat ground."""

    def __post_init__(self):
        super().__post_init__()

        # Robot
        self.robot = Go2Robot()

        # Terrain
        self.terrain = TerrainImporterCfg(
            prim_path="/World/ground",
            terrain_type="plane",
            max_terrain_level=0,
        )

        # Sensors
        self.sensors = {
            "imu": ImuCfg(),
            "contact_forces": ContactSensorCfg(body_names=[f"{leg}_foot" for leg in ["FL","FR","RL","RR"]]),
        }

        # Observations (robot state)
        self.observations = {
            "policy": ObservationGroupCfg(
                sensors=["imu", "joint_pos", "joint_vel", "actions"],
                noise=0.02,
            ),
        }

        # Reward terms (weights defined in YAML)
        self.rewards = {
            "lin_vel_tracking": RewardTermCfg(weight=1.0, term="track_lin_vel"),
            "ang_vel_tracking": RewardTermCfg(weight=0.5, term="track_ang_vel"),
            "torque_cost": RewardTermCfg(weight=-0.0001, term="torque"),
            "alive_bonus": RewardTermCfg(weight=0.05, term="alive"),
            "fall_penalty": RewardTermCfg(weight=-100.0, term="fall"),
        }

        # Commands (desired velocities)
        self.commands = {
            "lin_vel_x": ( -0.5, 1.5 ),
            "lin_vel_y": ( -0.3, 0.3 ),
            "ang_vel_z": ( -0.5, 0.5 ),
        }

        self.episode_length_s = 20.0
        self.num_envs = 4096