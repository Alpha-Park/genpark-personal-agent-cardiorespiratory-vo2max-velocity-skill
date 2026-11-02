# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Cardiorespiratory VO2Max Velocity Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentCardiorespiratoryVo2MaxVelocity

mcp = FastMCP("PersonalAgentCardiorespiratoryVo2MaxVelocity")
client = PersonalAgentCardiorespiratoryVo2MaxVelocity()

@mcp.tool()
def estimate_vo2max_from_heart_rate_ratio(
    resting_hr_bpm: float = 58.0,
    max_hr_bpm: float = 182.0,
    age: int = 42,
    sex: str = "male"
) -> str:
    """Calculates VO2max via Uth heart rate ratio, fitness biological age, and mortality hazard ratio."""
    import json
    return json.dumps(client.estimate_vo2max_from_heart_rate_ratio(
        resting_hr_bpm, max_hr_bpm, age, sex
    ), indent=2)

@mcp.tool()
def estimate_vo2max_from_cooper_run(
    twelve_minute_distance_meters: float = 2750.0,
    bodyweight_kg: float = 75.0
) -> str:
    """Calculates VO2max and aerobic velocity (vVO2max) from Cooper 12-minute run distance."""
    import json
    return json.dumps(client.estimate_vo2max_from_cooper_run(
        twelve_minute_distance_meters, bodyweight_kg
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
