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
    in_shape = draw(st.lists(st.integers(
            min_value=1, max_value=10), min_size=4, max_size=4))
    alpha_data = draw(st.floats(min_value=0.1, max_value=0.9))
    threshold_data = draw(st.floats(min_value=0.5, max_value=0.9))
    scale_data = draw(st.floats(min_value=0.7, max_value=0.9))
    offset_data = draw(st.floats(min_value=0.01, max_value=0.1))

    op_type_str = draw(st.sampled_from(["hard_swish", "hard_sigmoid"]))

    def generate_input(*args, **kwargs):
        return 2 * np.random.random(in_shape).astype(np.float32) - 1
    def get_attr_np(op_type):
        attr = {}
        if op_type == "hard_swish":
            attr = {"threshold" : threshold_data, "scale" : scale_data, "offset" : offset_data}
        else:
            attr = {"slope" : scale_data, "offset" : offset_data}
        return attr
    
    build_ops = OpConfig(
        type = op_type_str,
        inputs = {
            "X" : ["input_data"],
            },
        outputs = {
            "Out": ["output_data"],
        },
        attrs = get_attr_np(op_type_str))
    program_config = ProgramConfig(
        ops=[build_ops],
        weights={},
        inputs={
            "input_data":
            TensorConfig(data_gen=partial(generate_input)),
        },
        outputs=["output_data"])
    return program_config
