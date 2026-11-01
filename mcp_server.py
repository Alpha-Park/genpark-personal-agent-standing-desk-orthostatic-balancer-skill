# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Standing Desk Orthostatic Balancer Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentStandingDeskOrthostaticBalancer

mcp = FastMCP("PersonalAgentStandingDeskOrthostaticBalancer")
client = PersonalAgentStandingDeskOrthostaticBalancer()

@mcp.tool()
def calculate_sit_stand_orthostatic_strain(
    sitting_minutes_daily: float,
    standing_minutes_daily: float,
    walking_minutes_daily: float = 30.0
) -> str:
    """Audits sit/stand balance, LPL suppression, and venous pooling risk."""
    import json
    return json.dumps(client.calculate_sit_stand_orthostatic_strain(
        sitting_minutes_daily, standing_minutes_daily, walking_minutes_daily
    ), indent=2)

@mcp.tool()
def generate_sit_stand_cadence_schedule(
    workday_start: str = "09:00",
    workday_end: str = "17:00"
) -> str:
    """Synthesizes a 30-minute cyclic Cornell 20-8-2 motorized desk adjustment schedule."""
    import json
    return json.dumps(client.generate_sit_stand_cadence_schedule(
        workday_start, workday_end
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
