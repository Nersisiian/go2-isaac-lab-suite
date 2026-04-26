from .go2 import Go2Robot
from dataclasses import dataclass

@dataclass
class Go2ManipulatorRobot(Go2Robot):
    """Go2 with a 6-DOF manipulator mounted on the back."""

    # Additional joints
    arm_joint_names = [
        "arm_joint1", "arm_joint2", "arm_joint3",
        "arm_joint4", "arm_joint5", "arm_joint6",
    ]

    # Grasper end-effector
    has_gripper = True