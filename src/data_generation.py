import numpy as np
import pandas as pd

def generate_synthetic_data(seed: int = 123) -> pd.DataFrame :
    """
    Generates statistically realistic synthetic agricultural data.
    Returns a pandas DataFrame.
    """

########################################################################

    np.random.seed(seed)

########################################################################

    years = np.arange(2000,2025)
    n_years = len(years)

########################################################################

    baseline_rainfall = 800
    rainfall_trend = -3
    normal_variability = np.random.normal( loc=0 , scale=60 , size=n_years )
    extreme_events = np.zeros(n_years)
    extreme_years = np.random.choice( n_years , size=2 , replace=False )
    for i in extreme_years:
        extreme_events[i] = np.random.choice([-150,150])
    rainfall_mm = ( baseline_rainfall + (rainfall_trend*(years - years[0])) + normal_variability + extreme_events)
    rainfall_mm = np.clip( rainfall_mm , 300 , None )

########################################################################

    baseline_temperature = 25.0
    temperature_trends = +0.03
    temperature_noise = np.random.normal( loc=0 , scale=0.4 , size=n_years )
    temperature_c = (baseline_temperature + (temperature_trends*(years-years[0])) + temperature_noise)

########################################################################

    soil_index = np.zeros(n_years)
    soil_index[0] = 0.72
    natural_degradation = 0.003
    soil_noise = 0.005
    for i in range(1, n_years):
        soil_index[i] = (
            soil_index[i - 1]
            - natural_degradation
            + np.random.normal(0, soil_noise)
        )
    soil_index = np.clip(soil_index, 0.5, 0.85)

########################################################################

    base_irrigation = 30.0  
    irrigation_trend = 1.0
    mean_rainfall = np.mean(rainfall_mm)
    rainfall_sensitivity = -0.03  
    irrigation_noise = np.random.normal( loc=0 , scale=2.0 , size=n_years )
    irrigation_pct = ( base_irrigation + irrigation_trend * (years - years[0]) + rainfall_sensitivity * (rainfall_mm - mean_rainfall) + irrigation_noise )
    irrigation_pct = np.clip(irrigation_pct, 30, 70)

########################################################################

    base_fertilizer = 80.0
    irrigation_effect = 0.8      # kg/ha per % irrigation
    soil_compensation = -60.0    # compensate poorer soil
    fertilizer_trend = 1.2       # intensification over time
    fertilizer_noise = np.random.normal( loc=0, scale=10.0, size=n_years )
    fertilizer_kg_ha = ( base_fertilizer + irrigation_effect * irrigation_pct + soil_compensation * (soil_index - 0.7) + fertilizer_trend * (years - years[0]) + fertilizer_noise)
    fertilizer_kg_ha = np.clip(fertilizer_kg_ha, 50, 200)

########################################################################

    pest_pressure = np.random.uniform( low=0.1, high=0.5, size=n_years )
    outbreak_years = np.random.choice( n_years, size=3, replace=False )
    for i in outbreak_years:
        pest_pressure[i] += np.random.uniform(0.4, 0.6)
    pest_pressure_index = np.clip(pest_pressure, 0.0, 1.0)

########################################################################

    base_yield = 2000
    rainfall_coeff = 2.5          # kg/ha per mm
    soil_coeff = 1200             # kg/ha per soil index unit
    irrigation_coeff = 15         # kg/ha per % irrigation
    fertilizer_coeff = 3.0        # kg/ha per kg fertilizer
    baseline_temp = 25.0
    temperature_coeff = 120     # kg/ha per °C above baseline
    pest_coeff = 800            # kg/ha at pest_pressure = 1
    yield_noise = np.random.normal( loc=0 , scale=150 , size=n_years )
    yield_decline_rate = 15  # kg/ha lost per year due to sustainability stress
    system_stress = (
        -yield_decline_rate * (years - years[0])
    )
    yield_kg_ha = (
        base_yield
        + rainfall_coeff * rainfall_mm
        + soil_coeff * soil_index
        + irrigation_coeff * irrigation_pct
        + fertilizer_coeff * fertilizer_kg_ha
        - temperature_coeff* (temperature_c - baseline_temp)
        - pest_coeff * pest_pressure_index
        + system_stress 
        + yield_noise
    )
    yield_kg_ha = np.clip(yield_kg_ha, 0, None)

########################################################################

    data = pd.DataFrame({
        "year": years,
        "rainfall_mm": rainfall_mm.round(1),
        "temperature_c": temperature_c.round(2),
        "soil_index": soil_index.round(3),
        "irrigation_pct": irrigation_pct.round(1),
        "fertilizer_kg_ha": fertilizer_kg_ha.round(1),
        "pest_pressure_index": pest_pressure_index.round(2),
        "yield_kg_ha": yield_kg_ha.round(0)
    })


########################################################################

    # return pd.DataFrame()
    return data