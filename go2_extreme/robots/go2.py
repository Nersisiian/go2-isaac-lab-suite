from dataclasses import dataclass
from isaaclab.assets import RigidObjectCfg, AssetBaseCfg
from isaaclab.sensors import ContactSensorCfg, ImuCfg
from isaaclab.actuators import ActuatorNetCfg

@dataclass
class Go2Robot:
    """Unitree Go2 quadruped robot configuration."""

    # URDF path (downloaded by scripts/download_go2_model.sh)
    usd_path: str = "go2_extreme/assets/go2.usd"

    # Joint names (12 actuated joints)
    joint_names = [
        "FL_hip_joint", "FL_thigh_joint", "FL_calf_joint",
        "FR_hip_joint", "FR_thigh_joint", "FR_calf_joint",
        "RL_hip_joint", "RL_thigh_joint", "RL_calf_joint",
        "RR_hip_joint", "RR_thigh_joint", "RR_calf_joint",
    ]

    # Actuator model (simplified PD)
    actuator_cfg = ActuatorNetCfg(
        joint_names=joint_names,
        stiffness=20.0,
        damping=0.5,
        effort_limit=33.5,
        velocity_limit=20.0,
    )

    # Sensors
    imu_cfg = ImuCfg()
    contact_sensor_cfg = ContactSensorCfg(
        body_names=["FL_foot", "FR_foot", "RL_foot", "RR_foot"],
        threshold=1.0,
    )