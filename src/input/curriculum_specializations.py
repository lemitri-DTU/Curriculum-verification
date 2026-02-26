from .curriculum_groups_2023 import *
from .curriculum_groups_2024 import *
from .curriculum_groups_2025 import *

general_curriculum = {
    2023:[
        polytechnic_foundation_2023,
        innovation_II_2023,
        core_competence_mandatory_2023,
        core_competence_mandatory_replacement_2023,
        core_competence_digital_2023,
        core_competence_technology_2023,
        core_competence_general_2023,
        core_competence_combined_2023
    ],
    2024:[
        polytechnic_foundation_2024,
        innovation_II_2024,
        core_competence_mandatory_2024,
        core_competence_digital_2024,
        core_competence_technology_2024,
        core_competence_general_2024,
        polytechnic_innovation_combined_2024, 
        innovation_digital_combined_2024, 
        innovation_general_combined_2024, 
        technology_general_combined_2024

    ],
    2025:[
        polytechnic_foundation_2025,
        innovation_II_2025,
        core_competence_mandatory_2025,
        core_competence_digital_2025,
        core_competence_technology_2025,
        core_competence_general_2025,
        core_competence_combined_2025
    ]
}

digital_energy_systems_curriculum = {
    2025:[
    polytechnic_foundation_2025,
    innovation_II_2025,
    core_competence_mandatory_2025,
    DES_core_competence_digital_2025,
    DES_core_competence_technology_2025,
    DES_core_competence_general_1_2025,
    DES_core_competence_general_2_2025
]}

energy_systems_analysis_curriculum = {
    2025:[
    polytechnic_foundation_2025,
    innovation_II_2025,
    core_competence_mandatory_2025,
    ESA_core_competence_digital_2025,
    ESA_core_competence_technology_2025,
    ESA_core_competence_general_1_2025,
    ESA_core_competence_general_2_2025,
    ESA_core_competence_combined_2025
],
2023:[
    polytechnic_foundation_2023,
    innovation_II_2023,
    core_competence_mandatory_2023,
    ESA_core_competence_mandatory_2023,
    ESA_core_competence_technology_2023,
    ESA_core_competence_digital_2023,
    ESA_core_competence_general_2023,
    ESA_core_competence_combined_2023
]    
}

energy_efficient_building_systems_curriculum = {
    2025:[
    polytechnic_foundation_2025,
    innovation_II_2025,
    core_competence_mandatory_2025,
    EEBS_core_competence_digital_2025,
    EEBS_core_competence_technology_2025,
    EEBS_core_competence_general_1_2025,
    EEBS_core_competence_general_2_2025
]}

specialization_names = ['General','Digital Energy Systems','Energy Systems Analysis','Energy Efficient Building Systems']

curriculums = {'General':general_curriculum,
               'Digital Energy Systems':digital_energy_systems_curriculum,
               'Energy Systems Analysis':energy_systems_analysis_curriculum,
               'Energy Efficient Building Systems':energy_efficient_building_systems_curriculum}
