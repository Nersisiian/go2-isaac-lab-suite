import torch
import numpy as np

def quat_to_rpy(quat):
    """Convert quaternion (w,x,y,z) to roll, pitch, yaw."""
    w, x, y, z = quat[:, 0], quat[:, 1], quat[:, 2], quat[:, 3]
    roll = torch.atan2(2.0*(w*x + y*z), 1.0 - 2.0*(x*x + y*y))
    pitch = torch.asin(torch.clamp(2.0*(w*y - z*x), -1.0, 1.0))
    yaw = torch.atan2(2.0*(w*z + x*y), 1.0 - 2.0*(y*y + z*z))
    return torch.stack([roll, pitch, yaw], dim=-1)

def compute_torques(target_pos, current_pos, kp, kd, current_vel):
    """PD controller for joint torques."""
    pos_error = target_pos - current_pos
    torque = kp * pos_error - kd * current_vel
    return torque