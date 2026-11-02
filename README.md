# Personal Agent Cardiorespiratory VO2Max Velocity Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Uth heart rate ratio VO2max estimator, Cooper 12-minute run converter, ACSM longevity hazard ratio indexer, and cardiorespiratory fitness biological age modeler.

## Architecture

```mermaid
flowchart TD
    HeartRateInput[Resting HR bpm & Max HR bpm] --> UthEngine[Uth Heart Rate Ratio Modeler]
    UthEngine --> VO2MaxHR[VO2max mL/kg/min: 15.3 * HRmax / HRrest]
    CooperInput[12-Minute Run Distance Meters] --> CooperEngine[Kenneth Cooper Field Test Formula]
    CooperEngine --> VO2MaxCooper[VO2max mL/kg/min: d12 - 504.9 / 44.73]
    VO2MaxHR & VO2MaxCooper --> AgeStratifier[ACSM Age & Sex Median Benchmark Matrix]
    AgeStratifier --> BiologicalFitnessAge[Cardiorespiratory Biological Age Offset]
    AgeStratifier --> MortalityHazard[JAMA All-Cause Mortality Hazard Ratio]
```

## Quickstart

```python
from client import PersonalAgentCardiorespiratoryVo2MaxVelocity

agent = PersonalAgentCardiorespiratoryVo2MaxVelocity()
res = agent.estimate_vo2max_from_heart_rate_ratio(resting_hr_bpm=54.0, max_hr_bpm=185.0, age=42)
print(f"VO2max: {res['estimated_vo2max_ml_kg_min']} mL/kg/min | Fitness Age: {res['biological_cardiorespiratory_age']} yrs")
```
