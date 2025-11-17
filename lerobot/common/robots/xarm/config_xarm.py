# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass, field
from lerobot.common.cameras.camera import CameraConfig
from ..config import RobotConfig


@RobotConfig.register_subclass("xarm_end_effector")
@dataclass
class XarmEndEffectorConfig(RobotConfig):
    # Port to connect to the arm
    ip: str = "192.168.1.193"
    save_effort: bool = False
    limit_joints: bool = False
    dof: int = 6
    use_gripper: bool = False  # add gripper control option
    # cameras
    cameras: dict[str, CameraConfig] = field(default_factory=dict)


# Xarm6 version
@RobotConfig.register_subclass("xarm6_end_effector")
@dataclass
class Xarm6EndEffectorConfig(RobotConfig):
    # Port to connect to the arm
    ip: str = "192.168.1.235"
    save_effort: bool = False
    limit_joints: bool = False
    dof: int = 6
    use_gripper: bool = True  # add gripper control option
    # cameras
    cameras: dict[str, CameraConfig] = field(default_factory=dict)



# UF850 HIL version
@RobotConfig.register_subclass("uf850_end_effector_hil")
@dataclass
class HILXarmUF850EndEffectorConfig(RobotConfig):
    # Port to connect to the arm
    ip: str = "192.168.1.234"  # UF850 IP address
    save_effort: bool = False
    limit_joints: bool = False
    dof: int = 6
    use_gripper: bool = False  # add gripper control option
    act_features: str = "xyz_delta" # "xyz_delta" "xyzrpy_delta" "joints" "initial"

    linear_gain: float = 4.0
    angular_gain: float = 6.0
    max_angular_acc: float = 8.0
    
    # Home position joint angles (in degrees, will be converted to radians)
    home_position_6dof: list[float] = field(default_factory=lambda: [0, 0, 0, 0, 0, 0])
    
    # Default bounds for the end-effector position (in meters)
    end_effector_bounds: dict[str, list[float]] = field(
        default_factory=lambda: {
            "min": [-1.0, -1.0, -1.0],  # min x, y, z (`m`)
            "max": [ 1.0,  1.0,  1.0],  # max x, y, z (`m`)
        }
    )
    max_gripper_pos: int = 1
    # cameras
    cameras: dict[str, CameraConfig] = field(default_factory=dict)

    def __post_init__(self):
        """Validate configuration values after initialization."""
        valid_features = ["xyz_delta", "xyzrpy_delta", "joints", "from_initial"]
        if self.act_features not in valid_features:
            raise ValueError(f"act_features must be one of {valid_features}, got {self.act_features}")



# Lite6 HIL version
@RobotConfig.register_subclass("lite6_end_effector_hil")
@dataclass
class HILXarmEndEffectorConfig(RobotConfig):
    # Port to connect to the arm
    ip: str = "192.168.1.193"  # Lite6 IP address
    save_effort: bool = False
    limit_joints: bool = False
    dof: int = 6
    use_gripper: bool = False  # add gripper control option
    act_features: str = "xyz_delta" # "xyz_delta" "xyzrpy_delta" "joints" "initial"

    linear_gain: float = 4.0
    angular_gain: float = 6.0
    max_angular_acc: float = 8.0
    
    # Home position joint angles (in degrees, will be converted to radians)
    home_position_6dof: list[float] = field(default_factory=lambda: [0, 0, 1.57, 0, 1.57, 0])
    
    # Default bounds for the end-effector position (in meters)
    end_effector_bounds: dict[str, list[float]] = field(
        default_factory=lambda: {
            "min": [-1.0, -1.0, -1.0],  # min x, y, z (`m`)
            "max": [ 1.0,  1.0,  1.0],  # max x, y, z (`m`)
        }
    )
    max_gripper_pos: int = 1
    # cameras
    cameras: dict[str, CameraConfig] = field(default_factory=dict)

    def __post_init__(self):
        """Validate configuration values after initialization."""
        valid_features = ["xyz_delta", "xyzrpy_delta", "joints", "from_initial"]
        if self.act_features not in valid_features:
            raise ValueError(f"act_features must be one of {valid_features}, got {self.act_features}")



# Xarm6 HIL version
@RobotConfig.register_subclass("xarm6_end_effector_hil")
@dataclass
class HILXarm6EndEffectorConfig(RobotConfig):
    # Port to connect to the arm
    ip: str = "192.168.1.235"  # Xarm6 IP address
    save_effort: bool = False
    limit_joints: bool = False
    dof: int = 6
    use_gripper: bool = True  # add gripper control option
    # Interpret home position entries as degrees when True (default behavior)
    use_degrees: bool = True
    act_features: str = "xyz_delta" # "xyz_delta" "xyzrpy_delta" "joints" "initial"

    linear_gain: float = 4.0
    angular_gain: float = 6.0
    max_angular_acc: float = 8.0
    
    # Home position joint angles (in degrees, will be converted to radians)
    home_position_6dof: list[float] = field(default_factory=lambda: [0, 0, -90, 0, 90, 0])
    
    # Default bounds for the end-effector position (in meters)
    end_effector_bounds: dict[str, list[float]] = field(
        default_factory=lambda: {
            "min": [-1.0, -1.0, -1.0],  # min x, y, z (`m`)
            "max": [ 1.0,  1.0,  1.0],  # max x, y, z (`m`)
        }
    )
    max_gripper_pos: int = 1
    # cameras
    cameras: dict[str, CameraConfig] = field(default_factory=dict)

    def __post_init__(self):
        """Validate configuration values after initialization."""
        valid_features = ["xyz_delta", "xyzrpy_delta", "joints", "from_initial"]
        if self.act_features not in valid_features:
            raise ValueError(f"act_features must be one of {valid_features}, got {self.act_features}")



# Xarm7 HIL version
@RobotConfig.register_subclass("xarm7_end_effector_hil")
@dataclass
class HILXarm7EndEffectorConfig(RobotConfig):
    # Port to connect to the arm
    ip: str = "192.168.1.196"   # Xarm7 IP address
    save_effort: bool = False
    limit_joints: bool = False
    dof: int = 7
    act_features: str = "xyz_delta" # "xyz_delta" "xyzrpy_delta" "joints" "initial"

    linear_gain: float = 4.0
    angular_gain: float = 6.0
    max_angular_acc: float = 8.0
    
    # Home position joint angles (in degrees, will be converted to radians)
    home_position_7dof: list[float] = field(default_factory=lambda: [0, -45, 0, 30, 0, 75, 0])
    
    # Default bounds for the end-effector position (in meters)
    end_effector_bounds: dict[str, list[float]] = field(
        default_factory=lambda: {
            "min": [-1.0, -1.0, -1.0],  # min x, y, z (`m`)
            "max": [ 1.0,  1.0,  1.0],  # max x, y, z (`m`)
        }
    )
    max_gripper_pos: int = 1
    # cameras
    cameras: dict[str, CameraConfig] = field(default_factory=dict)

    def __post_init__(self):
        """Validate configuration values after initialization."""
        valid_features = ["xyz_delta", "xyzrpy_delta", "joints", "from_initial"]
        if self.act_features not in valid_features:
            raise ValueError(f"act_features must be one of {valid_features}, got {self.act_features}")