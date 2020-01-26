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
    builder.SetFlag('game_duration', 1000)
    builder.SetFlag('deterministic', False)
    builder.SetFlag('offsides', False)
    builder.SetFlag('end_episode_on_score', True)
    builder.SetFlag('end_episode_on_out_of_play', True)
    builder.SetFlag('end_episode_on_possession_change', True)

    builder.SetBallPosition(0.2617, -0.3190)

    builder.SetTeam(Team.e_Left)
    builder.AddPlayer(0.1730, 0.3857, e_PlayerRole_LM)
    builder.AddPlayer(0.3282, 0.0253, e_PlayerRole_CM)
    builder.AddPlayer(0.2306, -0.3513, e_PlayerRole_RM)
    builder.AddPlayer(0.4968, 0.2082, e_PlayerRole_CF)

    builder.SetTeam(Team.e_Right)
    builder.AddPlayer(0.9847, 0.0037, e_PlayerRole_GK)
    builder.AddPlayer(0.3681, -0.3755, e_PlayerRole_LB)
    builder.AddPlayer(0.6609, 0.0522, e_PlayerRole_CB)
    builder.AddPlayer(0.5456, 0.3911, e_PlayerRole_RB)
