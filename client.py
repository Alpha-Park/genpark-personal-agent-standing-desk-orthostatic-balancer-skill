# -*- coding: utf-8 -*-
"""
Personal Agent Standing Desk Orthostatic Balancer Client
Zero-dependency Cornell 20-8-2 sit-stand-walk ergonomic ratio modeler, lower limb hydrostatic
venous pooling auditor, and dynamic motorized desk cadence scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentStandingDeskOrthostaticBalancer:
    """
    Balances sedentary sitting cardiovascular risk against prolonged orthostatic venous pooling,
    implementing the Cornell University 20-8-2 ergonomic ratio to maximize metabolic flux.
    """

    def calculate_sit_stand_orthostatic_strain(
        self,
        sitting_minutes_daily: float,
        standing_minutes_daily: float,
        walking_minutes_daily: float = 30.0
    ) -> Dict[str, Any]:
        """
        Audits daily posture duration, evaluating Lipoprotein Lipase (LPL) suppression from sitting
        versus lower extremity hydrostatic pressure and varicose vein strain from prolonged static standing.
        """
        sit_m = max(0.0, min(1000.0, float(sitting_minutes_daily)))
        stand_m = max(0.0, min(600.0, float(standing_minutes_daily)))
        walk_m = max(0.0, min(300.0, float(walking_minutes_daily)))
        total_m = sit_m + stand_m + walk_m

        if total_m == 0:
            total_m = 480.0
            sit_m = 360.0
            stand_m = 90.0
            walk_m = 30.0

        sit_pct = round((sit_m / total_m) * 100.0, 1)
        stand_pct = round((stand_m / total_m) * 100.0, 1)
        walk_pct = round((walk_m / total_m) * 100.0, 1)

        # Lipoprotein Lipase (LPL) metabolic activity index (drops 90% after 2 hours uninterrupted sitting)
        if sit_m > 360.0 and walk_m < 30.0:
            lpl_status = "Severely Suppressed (Low lipid clearance, blunted postprandial glucose uptake)"
        elif sit_m > 240.0:
            lpl_status = "Moderately Depressed (Intermittent sitting sluggishness)"
        else:
            lpl_status = "Optimal Metabolic Clearance (Frequent postural transitions)"

        # Hydrostatic Venous Pooling Risk (standing > 45 continuous mins or > 240 daily mins statically)
        if stand_m > 240.0:
            venous_risk = "HIGH ORTHOSTATIC POOLING: Risk of lower limb edema, plantar fasciitis, and venous reflux."
        elif stand_m > 120.0:
            venous_risk = "MODERATE ORTHOSTATIC STRAIN: Well-balanced if paired with calf raises and supportive mat."
        else:
            venous_risk = "LOW VENOUS STRAIN: Safe standing exposure."

        # Cornell 20-8-2 Ideal Ratios: Sit 66.7%, Stand 26.7%, Walk 6.7%
        # Score deviation from ideal balance (100 is perfect equilibrium)
        ideal_sit_dev = abs(sit_pct - 66.7)
        ideal_stand_dev = abs(stand_pct - 26.7)
        ideal_walk_dev = abs(walk_pct - 6.7)
        balance_score = round(max(0.0, 100.0 - (ideal_sit_dev * 0.8 + ideal_stand_dev * 0.8 + ideal_walk_dev * 1.5)), 1)

        return {
            "total_monitored_workday_minutes": total_m,
            "postural_distribution": {
                "sitting_minutes": sit_m,
                "sitting_percentage": f"{sit_pct}%",
                "standing_minutes": stand_m,
                "standing_percentage": f"{stand_pct}%",
                "walking_minutes": walk_m,
                "walking_percentage": f"{walk_pct}%"
            },
            "orthostatic_equilibrium_score": f"{balance_score} / 100",
            "lipoprotein_lipase_metabolic_state": lpl_status,
            "venous_pooling_risk_assessment": venous_risk,
            "ergonomic_recommendation": "Adopt the Cornell 20-8-2 rhythm: In every 30-min block, sit for 20 min, stand for 8 min, and walk for 2 min."
        }

    def generate_sit_stand_cadence_schedule(
        self,
        workday_start: str = "09:00",
        workday_end: str = "17:00"
    ) -> Dict[str, Any]:
        """
        Synthesizes a 30-minute cyclic motorized desk height adjustment schedule,
        alternating 20 min sitting, 8 min standing, and 2 min active ambulation.
        """
        def parse_h(t_str: str) -> float:
            parts = str(t_str).split(":")
            return float(parts[0]) + (float(parts[1]) / 60.0 if len(parts) > 1 else 0.0)

        def format_h(h_val: float) -> str:
            hh = int(h_val) % 24
            mm = int((h_val - int(h_val)) * 60)
            return f"{hh:02d}:{mm:02d}"

        start_h = parse_h(workday_start)
        end_h = parse_h(workday_end)
        total_hours = end_h - start_h if end_h >= start_h else (end_h + 24.0) - start_h

        # Generate sample sequence of cycles
        cycles_count = int(total_hours * 2) # two 30-min cycles per hour
        schedule_blocks = []

        curr = start_h
        for c in range(min(12, cycles_count)): # display first 12 cycles (~6 hours)
            t_sit_start = curr
            t_stand_start = curr + (20.0 / 60.0)
            t_walk_start = curr + (28.0 / 60.0)
            t_next = curr + 0.5

            schedule_blocks.append({
                "cycle_number": c + 1,
                "sit_phase": f"{format_h(t_sit_start)} - {format_h(t_stand_start)} (20 min Sitting: Neutral lumbar spine)",
                "stand_phase": f"{format_h(t_stand_start)} - {format_h(t_walk_start)} (8 min Standing: Motorized desk raised)",
                "walk_phase": f"{format_h(t_walk_start)} - {format_h(t_next)} (2 min Active: Ambulation / Calf pump)"
            })
            curr = t_next

        projected_daily_stand_mins = round(cycles_count * 8.0, 0)
        projected_daily_walk_mins = round(cycles_count * 2.0, 0)

        return {
            "workday_window": f"{workday_start} to {workday_end} ({round(total_hours, 1)} hours)",
            "total_30min_cycles_planned": cycles_count,
            "projected_total_standing_minutes": projected_daily_stand_mins,
            "projected_total_walking_minutes": projected_daily_walk_mins,
            "sample_cadence_schedule": schedule_blocks[:6],
            "ergonomic_rule": "Never exceed 30 minutes of continuous static standing to prevent plantar fascial ischemia."
        }
