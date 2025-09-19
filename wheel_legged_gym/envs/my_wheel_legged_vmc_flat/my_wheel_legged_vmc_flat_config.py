
from wheel_legged_gym.envs.my_wheel_legged_vmc.my_wheel_legged_vmc_config import (
    MyWheelLeggedVMCCfg,
    MyWheelLeggedVMCCfgPPO,
)


class MyWheelLeggedVMCFlatCfg(MyWheelLeggedVMCCfg):

    class terrain(MyWheelLeggedVMCCfg.terrain):
        mesh_type = "plane"


class MyWheelLeggedVMCFlatCfgPPO(MyWheelLeggedVMCCfgPPO):
    class runner(MyWheelLeggedVMCCfgPPO.runner):
        # logging
        experiment_name = "my_wheel_legged_vmc_flat"
        max_iterations = 2000
