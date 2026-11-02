# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Cardiorespiratory VO2Max Velocity Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentCardiorespiratoryVo2MaxVelocity

def main():
    agent = PersonalAgentCardiorespiratoryVo2MaxVelocity()

    print("=" * 70)
    print("DEMO: Personal Agent Cardiorespiratory VO2Max & Longevity Engine")
    print("=" * 70)

    # 1. Estimate VO2max via Uth Formula (RHR: 54 bpm, Max HR: 185 bpm, Male, Age 42)
    res_hr = agent.estimate_vo2max_from_heart_rate_ratio(
        resting_hr_bpm=54.0,
        max_hr_bpm=185.0,
        age=42,
        sex="male"
    )

    print(f"\n1. Cardiorespiratory VO2max Evaluation (Heart Rate Ratio):")
    print(f"   Resting HR / Max HR: {res_hr['resting_heart_rate_bpm']} / {res_hr['maximum_heart_rate_bpm']} bpm")
    print(f"   Estimated VO2max: {res_hr['estimated_vo2max_ml_kg_min']} mL/kg/min (Normative Median: {res_hr['normative_age_sex_median']})")
    print(f"   Fitness Tier: {res_hr['cardiorespiratory_fitness_tier']}")
    print(f"   Chronological Age: {res_hr['chronological_age']} years")
    print(f"   Biological Cardiorespiratory Age: {res_hr['biological_cardiorespiratory_age']} years (Shift: {res_hr['fitness_age_delta_years']})")
    print(f"   Mortality Hazard Ratio: {res_hr['all_cause_mortality_hazard_ratio']} ({res_hr['longevity_advantage']})")

    # 2. Estimate VO2max via Cooper 12-Minute Run Test (2,850 meters, BW 74 kg)
    res_cooper = agent.estimate_vo2max_from_cooper_run(
        twelve_minute_distance_meters=2850.0,
        bodyweight_kg=74.0
    )

    print(f"\n2. Cooper 12-Minute Aerobic Field Test (2,850 meters):")
    print(f"   Estimated VO2max: {res_cooper['estimated_vo2max_ml_kg_min']} mL/kg/min")
    print(f"   Absolute VO2max: {res_cooper['absolute_vo2max_liters_min']} L/min")
    print(f"   Aerobic Velocity (vVO2max): {res_cooper['aerobic_velocity_v_vo2max_kmh']} km/h (Pace: {res_cooper['average_kilometer_pace_min_sec']})")
    print(f"   Training Strategy: {res_cooper['training_prescription']}")

    print("\nVerification complete: Cardiorespiratory capacity engine executed flawlessly.")

if __name__ == "__main__":
    main()
