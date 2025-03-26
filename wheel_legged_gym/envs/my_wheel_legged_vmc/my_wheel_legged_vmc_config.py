
from wheel_legged_gym.envs.my_wheel_legged.my_wheel_legged_config import (
    MyWheelLeggedCfg,
    MyWheelLeggedCfgPPO,
)


class MyWheelLeggedVMCCfg(MyWheelLeggedCfg):
    class env(MyWheelLeggedCfg.env):
        num_privileged_obs = (
            MyWheelLeggedCfg.env.num_observations + 7 * 11 + 3 + 6 * 7 + 3 + 3
        )

    class control(MyWheelLeggedCfg.control):
        action_scale_theta = 0.5
        action_scale_l0 = 0.1
        action_scale_vel = 10.0

        l0_offset = 0.175
        feedforward_force = 40.0  # [N]

        kp_theta = 50.0  # [N*m/rad]
        kd_theta = 3.0  # [N*m*s/rad]
        kp_l0 = 900.0  # [N/m]
        kd_l0 = 20.0  # [N*s/m]

        # PD Drive parameters:
        stiffness = {"f0": 0.0, "f1": 0.0, "wheel": 0}  # [N*m/rad]
        damping = {"f0": 0.0, "f1": 0.0, "wheel": 0.5}  # [N*m*s/rad]

    class normalization(MyWheelLeggedCfg.normalization):
        class obs_scales(MyWheelLeggedCfg.normalization.obs_scales):
            l0 = 5.0
            l0_dot = 0.25

    class noise(MyWheelLeggedCfg.noise):
        class noise_scales(MyWheelLeggedCfg.noise.noise_scales):
            l0 = 0.02
            l0_dot = 0.1


class MyWheelLeggedVMCCfgPPO(MyWheelLeggedCfgPPO):

    class algorithm(MyWheelLeggedCfgPPO.algorithm):
        kl_decay = (
            MyWheelLeggedCfgPPO.algorithm.desired_kl - 0.002
        ) / MyWheelLeggedCfgPPO.runner.max_iterations

    class runner(MyWheelLeggedCfgPPO.runner):
        # logging
        experiment_name = "my_wheel_legged_vmc"
        max_iterations = 1000
