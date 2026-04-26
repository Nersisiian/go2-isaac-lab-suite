import torch
from isaaclab.assets import RigidObject

def track_lin_vel(env):
    """Reward for matching desired linear velocity."""
    desired = env.command_manager.get_command("lin_vel")
    actual = env.robot.root_vel[:, :2]
    error = torch.norm(desired - actual, dim=1)
    return torch.exp(-error * 0.5)

def track_ang_vel(env):
    desired = env.command_manager.get_command("ang_vel_z")
    actual = env.robot.root_vel[:, 5]  # angular z
    error = torch.abs(desired - actual)
    return torch.exp(-error * 5.0)

def torque_cost(env):
    return torch.sum(env.robot.applied_torque ** 2, dim=1)

def alive(env):
    return torch.ones(env.num_envs, device=env.device)

def fall(env):
    """Penalty when robot base orientation is too tilted."""
    tilt = torch.abs(env.robot.root_quat[:, 1:3]) > 0.7  # pitch or roll > 45 deg
    return tilt.any(dim=1).float()

def jump_apex(env):
    """Reward for reaching high z-position (jump)."""
    z = env.robot.root_pos[:, 2]
    return torch.clamp(z - 0.4, min=0.0, max=0.6) * 10.0

def air_time(env):
    """Reward for having all feet off ground simultaneously."""
    contacts = env.sensors["contact_forces"].net_forces_z > 1.0
    air = ~contacts.any(dim=1)
    return air.float()

def backflip_angle(env):
    """Cumulative reward for achieving roll > 300° (backflip)."""
    roll = torch.atan2(2*(env.robot.root_quat[:,0]*env.robot.root_quat[:,1] +
                         env.robot.root_quat[:,2]*env.robot.root_quat[:,3]),
                       1 - 2*(env.robot.root_quat[:,1]**2 + env.robot.root_quat[:,2]**2))
    progress = torch.clamp(roll / (2*torch.pi), min=0.0, max=1.0)
    return progress

def upright_orientation(env):
    """Reward for being upright (recovery task)."""
    quat = env.robot.root_quat
    upright = torch.abs(quat[:, 0]) > 0.9  # w > 0.9 means almost identity quaternion
    return upright.float() * 100.0

def object_grasped(env):
    """Check if end-effector is close to object."""
    # simplified: distance between gripper and object
    gripper_pos = env.robot.body_pos[:, env.robot.arm_end_effector_idx]
    obj_pos = env.object.pos
    distance = torch.norm(gripper_pos - obj_pos, dim=1)
    return (distance < 0.02).float()

def object_at_target(env):
    """Reward for placing object on target zone."""
    obj_pos = env.object.pos
    target_pos = env.target_zone.pos
    distance_to_target = torch.norm(obj_pos - target_pos, dim=1)
    return torch.exp(-distance_to_target * 20.0)