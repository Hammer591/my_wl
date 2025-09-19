
from wheel_legged_gym.envs.base.legged_robot_config import (
    LeggedRobotCfg,
    LeggedRobotCfgPPO,
)


class MyWheelLeggedCfg(LeggedRobotCfg):

    class init_state(LeggedRobotCfg.init_state):
        pos = [0.0, 0.0, 0.4]  # x,y,z [m]
        default_joint_angles = {  # target angles when action = 0.0
            "lf0_Joint": 0.0,
            "lf1_Joint": 0.0,
            "l_wheel_Joint": 0.0,
            "rf0_Joint": -0.0,
            "rf1_Joint": -0.0,
            "r_wheel_Joint": 0.0,
        }

    class control(LeggedRobotCfg.control):
        pos_action_scale = 0.5
        vel_action_scale = 10.0
        # PD Drive parameters:
        stiffness = {"f0": 40.0, "f1": 40.0, "wheel": 0}  # [N*m/rad]
        damping = {"f0": 1.0, "f1": 1.0, "wheel": 0.5}  # [N*m*s/rad]

    class asset(LeggedRobotCfg.asset):
        # file = "{WHEEL_LEGGED_GYM_ROOT_DIR}/resources/robots/a1_description/urdf/a1.urdf"
        file = "/home/hammer/Wheel-Legged-Gym/resources/robots/main2/urdf/main2.urdf"
        name = "MyWheelLegged"
        offset = 0.00
        l1 = 0.15
        l2 = 0.30
        penalize_contacts_on = ["lf", "rf", "base_link"]
        terminate_after_contacts_on = ["base_link"]
        self_collisions = 1  # 1 to disable, 0 to enable...bitwise filter
        flip_visual_attachments = False


class MyWheelLeggedCfgPPO(LeggedRobotCfgPPO):
    class runner(LeggedRobotCfgPPO.runner):
        # logging
        experiment_name = "my_wheel_legged"
        max_iterations = 2000
