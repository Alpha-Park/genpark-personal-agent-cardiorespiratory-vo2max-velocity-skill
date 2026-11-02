---
name: genpark-personal-agent-cardiorespiratory-vo2max-velocity-skill
version: "1.0.0"
description: "Zero-dependency Uth heart rate ratio VO2max estimator, Cooper 12-minute run converter, ACSM longevity hazard ratio indexer, and cardiorespiratory fitness biological age modeler."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Cardiorespiratory VO2Max Velocity Skill

Designed for **OpenClaw**, **Hermes**, and sovereign personal AI assistants to evaluate cardiorespiratory fitness ($VO_2\max$ in mL/kg/min), calculate aerobic capacity via the Uth-Sørensen-Overgaard-Pedersen heart rate ratio formula ($15.3 \times \frac{HR_{\max}}{HR_{\text{rest}}}$) and Cooper 12-minute field run tests, determine biological cardiorespiratory fitness age, and model all-cause mortality hazard reductions from large-scale prospective cohort studies.

## Agent In-Context Capabilities

- **Mathematical VO2max Estimation**: Computes cardiorespiratory fitness without expensive lab metabolic carts via validated physiological resting/max heart rate ratios.
- **Biological Fitness Age Quantification**: Translates aerobic deviation from age/sex medians into biological fitness age offsets (-1.0 yr per 0.4 mL/kg/min gain).
- **Epidemiological Longevity Hazard Mapping**: Incorporates JAMA Network Open data demonstrating an 80% lower mortality hazard for elite cardiorespiratory fitness.

## Tools Summary

1. `estimate_vo2max_from_heart_rate_ratio`: Returns estimated VO2max, cardiorespiratory tier, biological fitness age, and mortality hazard ratio.
2. `estimate_vo2max_from_cooper_run`: Calculates VO2max, absolute oxygen consumption (L/min), and aerobic velocity ($vVO_2\max$).
