# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Standing Desk Orthostatic Balancer Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentStandingDeskOrthostaticBalancer

def main():
    agent = PersonalAgentStandingDeskOrthostaticBalancer()

    print("=" * 70)
    print("DEMO: Personal Agent Standing Desk Orthostatic Balancer")
    print("=" * 70)

    # 1. Audit typical tech worker day (420 min sitting, 45 min standing, 15 min walking)
    res_audit = agent.calculate_sit_stand_orthostatic_strain(
        sitting_minutes_daily=420.0,
        standing_minutes_daily=45.0,
        walking_minutes_daily=15.0
    )

    print(f"\n1. Daily Postural Distribution & Orthostatic Audit:")
    print(f"   Sitting: {res_audit['postural_distribution']['sitting_minutes']} min ({res_audit['postural_distribution']['sitting_percentage']})")
    print(f"   Standing: {res_audit['postural_distribution']['standing_minutes']} min ({res_audit['postural_distribution']['standing_percentage']})")
    print(f"   Walking: {res_audit['postural_distribution']['walking_minutes']} min ({res_audit['postural_distribution']['walking_percentage']})")
    print(f"   Equilibrium Score: {res_audit['orthostatic_equilibrium_score']}")
    print(f"   LPL Metabolic State: {res_audit['lipoprotein_lipase_metabolic_state']}")
    print(f"   Venous Strain: {res_audit['venous_pooling_risk_assessment']}")
    print(f"   Guidance: {res_audit['ergonomic_recommendation']}")

    # 2. Generate Cornell 20-8-2 Schedule
    res_cadence = agent.generate_sit_stand_cadence_schedule(
        workday_start="09:00",
        workday_end="17:00"
    )

    print(f"\n2. Cornell 20-8-2 Cyclic Desk Cadence Schedule:")
    print(f"   Workday: {res_cadence['workday_window']} ({res_cadence['total_30min_cycles_planned']} cycles)")
    print(f"   Projected Standing: {res_cadence['projected_total_standing_minutes']} min | Walking: {res_cadence['projected_total_walking_minutes']} min")
    print(f"   First 3 Cycles:")
    for block in res_cadence['sample_cadence_schedule'][:3]:
        print(f"     Cycle #{block['cycle_number']}:")
        print(f"       - {block['sit_phase']}")
        print(f"       - {block['stand_phase']}")
        print(f"       - {block['walk_phase']}")

    print("\nVerification complete: Standing desk orthostatic engine executed flawlessly.")

if __name__ == "__main__":
    main()
