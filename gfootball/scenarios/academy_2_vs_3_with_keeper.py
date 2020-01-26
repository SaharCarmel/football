# coding=utf-8
# Copyright 2019 Google LLC
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


from . import *


def build_scenario(builder):
    builder.SetFlag('game_duration', 400)
    builder.SetFlag('deterministic', False)
    builder.SetFlag('offsides', False)
    builder.SetFlag('end_episode_on_score', True)
    builder.SetFlag('end_episode_on_out_of_play', True)
    builder.SetFlag('end_episode_on_possession_change', True)

    builder.SetBallPosition(0.5589, 0.1544)

    builder.SetTeam(Team.e_Left)
    builder.AddPlayer(0.8694, -0.4051, e_PlayerRole_CF)
    builder.AddPlayer(0.6210, -0.0043, e_PlayerRole_CF)

    builder.SetTeam(Team.e_Right)
    builder.AddPlayer(0.9758, -0.0070, e_PlayerRole_GK)
    builder.AddPlayer(0.6786, -0.1765, e_PlayerRole_LB)
    builder.AddPlayer(0.7629, -0.0178, e_PlayerRole_CB)
    builder.AddPlayer(0.6919, 0.1678, e_PlayerRole_RB)
