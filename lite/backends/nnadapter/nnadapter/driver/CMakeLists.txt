# Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set(NNADAPTER_DEVICES CACHE INTERNAL "")

if(NNADAPTER_WITH_HUAWEI_KIRIN_NPU)
  add_subdirectory(huawei_kirin_npu)
endif()

if(NNADAPTER_WITH_HUAWEI_ASCEND_NPU)
  add_subdirectory(huawei_ascend_npu)
endif()

if(NNADAPTER_WITH_MEDIATEK_APU)
  add_subdirectory(mediatek_apu)
endif()

if(NNADAPTER_WITH_ROCKCHIP_NPU)
  add_subdirectory(rockchip_npu)
endif()

if(NNADAPTER_WITH_IMAGINATION_NNA)
  add_subdirectory(imagination_nna)
endif()

if(NNADAPTER_WITH_AMLOGIC_NPU)
  add_subdirectory(amlogic_npu)
endif()

if(NNADAPTER_WITH_CAMBRICON_MLU)
  add_subdirectory(cambricon_mlu)
endif()

if(NNADAPTER_WITH_VERISILICON_TIMVX)
  add_subdirectory(verisilicon_timvx)
endif()
