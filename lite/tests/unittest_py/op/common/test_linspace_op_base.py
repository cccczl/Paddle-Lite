# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
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

import sys
sys.path.append('..')

from program_config import TensorConfig, ProgramConfig, OpConfig, CxxConfig, TargetType, PrecisionType, DataLayoutType, Place
import numpy as np
from functools import partial
from typing import Optional, List, Callable, Dict, Any, Set
import unittest
import hypothesis
import hypothesis.strategies as st
from hypothesis import assume

def sample_program_configs(draw):
    start_id = draw(st.integers(min_value=0, max_value=5))
    stop_id = draw(st.integers(min_value=50, max_value=60))
    num_data = draw(st.integers(min_value=1, max_value=10))
    op_type_str = draw(st.sampled_from([5]))  #2:int 5:float, lite only support float

    def generate_start1(*args, **kwargs):
        return np.array([float(start_id)]).astype(np.float32)
    def generate_start2(*args, **kwargs):
        return np.array([int(start_id)]).astype(np.int32)
    def generate_stop1(*args, **kwargs):
        return np.array([float(stop_id)]).astype(np.float32)
    def generate_stop2(*args, **kwargs):
        return np.array([int(stop_id)]).astype(np.int32)
    def generate_num(*args, **kwargs):
        return np.array([int(num_data)]).astype(np.int32)
   
    build_ops = OpConfig(
        type = "linspace",
        inputs = {
            "Start" : ["start_data"],
            "Stop" : ["stop_data"],
            "Num" : ["num_data"],
            },
        outputs = {
            "Out": ["output_data"],
        },
        attrs = {"dtype" : int(op_type_str)})
    
    if op_type_str == 2 :
        program_config = ProgramConfig(
        ops=[build_ops],
        weights={},
        inputs={
            "start_data":
            TensorConfig(data_gen=partial(generate_start2)),
            "stop_data":
            TensorConfig(data_gen=partial(generate_stop2)),
            "num_data":
            TensorConfig(data_gen=partial(generate_num)),
        },
        outputs=["output_data"])
    elif op_type_str == 5 :
        program_config = ProgramConfig(
        ops=[build_ops],
        weights={},
        inputs={
            "start_data":
            TensorConfig(data_gen=partial(generate_start1)),
            "stop_data":
            TensorConfig(data_gen=partial(generate_stop1)),
            "num_data":
            TensorConfig(data_gen=partial(generate_num)),
        },
        outputs=["output_data"])
    return program_config
