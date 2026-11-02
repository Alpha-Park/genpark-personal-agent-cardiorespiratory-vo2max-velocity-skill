# -*- coding: utf-8 -*-
"""Personal Agent Cardiorespiratory VO2Max Velocity Skill.

Zero-dependency Uth heart rate ratio VO2max estimator, Cooper 12-minute run converter,
ACSM longevity hazard ratio indexer, and cardiorespiratory fitness biological age modeler.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentCardiorespiratoryVo2MaxVelocity:
    """Quantitative cardiorespiratory fitness and aerobic capacity engine based on
    the Uth-Sørensen-Overgaard-Pedersen formula and JAMA Network Open longevity hazard models."""

    # ACSM age and sex-stratified median VO2max benchmarks (mL/kg/min)
    NORMATIVE_MEDIANS = {
        "male": {
            (20, 29): 46.5,
            (30, 39): 44.0,
            (40, 49): 41.5,
            (50, 59): 37.5,
            (60, 69): 33.5,
            (70, 99): 28.0
        },
        "female": {
            (20, 29): 39.5,
            (30, 39): 37.0,
            (40, 49): 34.5,
            (50, 59): 31.0,
            (60, 69): 27.5,
            (70, 99): 23.0
        }
    }

    def estimate_vo2max_from_heart_rate_ratio(
        self,
        resting_hr_bpm: float = 58.0,
        max_hr_bpm: float = 182.0,
        age: int = 42,
        sex: str = "male"
    ) -> Dict[str, Any]:
        """Calculates VO2max (mL/kg/min) via the Uth et al. heart rate ratio formula,
        cardiorespiratory fitness percentile, biological fitness age, and mortality hazard ratio."""
        rhr = max(35.0, min(120.0, float(resting_hr_bpm)))
        mhr = max(rhr + 20.0, min(230.0, float(max_hr_bpm)))
        a = max(18, int(age))
        gender = "female" if sex.lower().startswith("f") else "male"

        # Uth-Sørensen-Overgaard-Pedersen formula:
        # VO2max = 15.3 * (HRmax / HRrest)
        vo2max = round(15.3 * (mhr / rhr), 1)

        # Lookup normative median for age & sex
        norm_map = self.NORMATIVE_MEDIANS[gender]
        norm_ref = 40.0 if gender == "male" else 33.0
        for (low, high), val in norm_map.items():
            if low <= a <= high:
                norm_ref = val
                break

        # Fitness Tier Classification
        diff = vo2max - norm_ref
        if diff >= 10.0:
            tier = "Elite / Superior Cardiorespiratory Fitness (> 95th percentile)"
            hazard_ratio = 0.20  # 5-fold mortality risk reduction vs low fitness
        elif diff >= 4.0:
            tier = "Excellent Aerobic Capacity (75th - 95th percentile)"
            hazard_ratio = 0.38
        elif diff >= -3.0:
            tier = "Good / Normative Aerobic Baseline (50th - 75th percentile)"
            hazard_ratio = 0.55
        elif diff >= -8.0:
            tier = "Below Average / Fair (25th - 50th percentile)"
            hazard_ratio = 0.75
        else:
            tier = "Low Cardiorespiratory Fitness (< 25th percentile)"
            hazard_ratio = 1.00  # reference high-risk group

        # Biological Fitness Age Modeling:
        # VO2max declines by ~1% per year after age 25 (~0.4 mL/kg/min/yr)
        age_shift = round(-1.0 * (diff / 0.40), 1)
        fitness_age = max(18.0, round(a + age_shift, 1))

        return {
            "resting_heart_rate_bpm": rhr,
            "maximum_heart_rate_bpm": mhr,
            "estimated_vo2max_ml_kg_min": vo2max,
            "normative_age_sex_median": norm_ref,
            "cardiorespiratory_fitness_tier": tier,
            "chronological_age": a,
            "biological_cardiorespiratory_age": fitness_age,
            "fitness_age_delta_years": f"{'+' if age_shift > 0 else ''}{age_shift} years",
            "all_cause_mortality_hazard_ratio": hazard_ratio,
            "longevity_advantage": f"{round((1.0 - hazard_ratio) * 100)}% lower all-cause mortality hazard vs low fitness baseline"
        }

    def estimate_vo2max_from_cooper_run(
        self,
        twelve_minute_distance_meters: float = 2750.0,
        bodyweight_kg: float = 75.0
    ) -> Dict[str, Any]:
        """Calculates VO2max using the Kenneth Cooper 12-minute run field test equation."""
        d = max(550.0, float(twelve_minute_distance_meters))
        bw = max(35.0, float(bodyweight_kg))

        # Cooper Equation: VO2max = (d12 - 504.9) / 44.73
        vo2max = round((d - 504.9) / 44.73, 1)

        # Velocity at VO2max (vVO2max in km/h):
        # Average pace over 12 mins extrapolated to aerobic velocity
        v_vo2max = round((d / 1000.0) / (12.0 / 60.0), 2)

        # Absolute O2 consumption in L/min
        abs_vo2_l_min = round((vo2max * bw) / 1000.0, 2)

        return {
            "cooper_twelve_minute_distance_meters": d,
            "estimated_vo2max_ml_kg_min": vo2max,
            "absolute_vo2max_liters_min": abs_vo2_l_min,
            "aerobic_velocity_v_vo2max_kmh": v_vo2max,
            "average_kilometer_pace_min_sec": f"{int(60.0 / v_vo2max)}:{int(((60.0 / v_vo2max) % 1) * 60):02d} /km",
            "training_prescription": (
                "To optimize VO2max: execute 1 weekly high-intensity interval session (4x4 min @ 90-95% HRmax) "
                "coupled with 150-180 min/week Zone 2 base building."
            )
        }
