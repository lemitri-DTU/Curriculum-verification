# Common to all specializations

polytechnic_foundation_2025 = {'name':'Polytechnic foundation courses (2025)',
    'courses':{('12100','12101','12105','12106','41636'):5, ('42500','42501','42502','45503','42504','42505'):5},
    'requirement':10
}
    
innovation_II_2025 = {'name':'Innovation course II (2025)',
    'courses':{('38102','42014','42015','42016'):5},
    'requirement':5
}

core_competence_mandatory_2025 = {'name':'Core competence mandatory courses (2025)',
    'courses':{('46205',):5, ('46740',):5, ('46770',):5},
    'requirement':15
}

# "General" specialization

core_competence_digital_2025 = {'name':'Core competence digital courses for general specialization (2025)',
    'courses':{('02452','02180'):5, ('02476','02807'):5, ('42112','42114'):5, ('46120',):5, ('46755',):5},
    'requirement':10
}

core_competence_technology_2025 = {'name':'Core competence technology courses for general curriculum (2025)',
    'courses':{('34552',):5, ('41418',):5, ('41468',):5, ('46200',):5, ('47301',):5, ('47330',):5, ('47334',):5},
    'requirement':5
}

core_competence_general_2025 = {'name':'Core competence general courses for general specialization (2025)',
    'courses':{('02417',):5, ('02431',):5, ('02435',):5, ('02619',):5, ('12362',):5, ('12611',):5, ('41462',):5, ('41464',):10, ('41465',):5, ('41466',):5, ('41468',):5, ('41469',):5, ('42001',):5, ('42879',):5, ('46705',):5, ('46745',):5, ('46750',):5,('46765',):5},
    'requirement':15
}

core_competence_combined_2025 = {'name':'Combined (technology + other) core competence courses without duplicates (2025)',
    'courses':{('34552',):5, ('41418',):5, ('41468',):5, ('46200',):5, ('47301',):5, ('47330',):5, ('47334',):5,
               ('02417',):5, ('02431',):5, ('02435',):5, ('02619',):5, ('12362',):5, ('12611',):5, ('41462',):5, ('41464',):10, ('41465',):5, ('41466',):5, ('41469',):5, ('42001',):5, ('42879',):5, ('46705',):5, ('46745',):5, ('46750',):5, ('46750',):5, ('46765',):5},
    'requirement':20
}

## Digital Energy Systems specialization

DES_core_competence_digital_2025 = {'name':'Core competence digital courses for Digital Energy Systems specialization (2025)',
    'courses':core_competence_digital_2025['courses'],
    'requirement':10
}

DES_core_competence_technology_2025 = {'name':'Core competence technology courses for Digital Energy Systems specialization (2025)',
    'courses':core_competence_technology_2025['courses'],
    'requirement':5
}

DES_core_competence_general_1_2025 = {'name':'Core competence general courses for Digital Energy Systems specialization - Part 1 (2025)',
    'courses':{('46750',):5, ('46765',):5},
    'requirement':10
}

DES_core_competence_general_2_2025 = {'name':'Core competence general courses for Digital Energy Systems specialization - Part 2 (2025)',
                'courses':{('02417',):5, ('02435',):5, ('02619',):5, ('46705',):5},
                'requirement':5
}

## Energy Systems Analysis specialization

ESA_core_competence_digital_2025 = {'name':'Core competence digital courses for Energy Systems Analysis specialization (2025)',
    'courses':{('42112','42114'):5, ('46120',):5, ('46755',):5},
    'requirement':10
}

ESA_core_competence_technology_2025 = {'name':'Core competence technology courses for Energy Systems Analysis specialization (2025)',
    'courses':core_competence_technology_2025['courses'],
    'requirement':5
}

ESA_core_competence_general_1_2025 = {'name':'Core competence general courses for Energy Systems Analysis specialization - Part 1 (2025)',
    'courses':{('42014',):5, ('42016',):5, ('42879',):5, ('46745',):5, ('46755',):5},
    'requirement':10
}

ESA_core_competence_general_2_2025 = {'name':'Core competence general courses for Energy Systems Analysis specialization - Part 2 (2025)',
    'courses':{('02435',):5, ('42001',):5},
    'requirement':5
}

ESA_core_competence_combined_2025 = {'name':'Combined Core competence digital & general 1/2 for Energy Systems Analysis specialization without duplicates (2025)',
    'courses':{('42112',):5, ('42114',):5, ('46120',):5, ('46755',):5,
               ('42014',):5, ('42016',):5, ('42879',):5, ('46745',):5},
    'requirement':20
}

## Energy Efficient Building Systems

EEBS_core_competence_digital_2025 = {'name':'Core competence digital courses for Energy Efficient Building Systems specialization (2025)',
    'courses':ESA_core_competence_digital_2025['courses'],
    'requirement':10
}

EEBS_core_competence_technology_2025 = {'name':'Core competence technology courses for Energy Efficient Building Systems specialization (2025)',
    'courses':core_competence_technology_2025['courses'],
    'requirement':5
}

EEBS_core_competence_general_1_2025 = {'name':'Core competence general courses for Energy Efficient Building Systems specialization - Part 1 (2025)',
    'courses':{('41462',):5, ('41466',):5},
    'requirement':10
}

EEBS_core_competence_general_2_2025 = {'name':'Core competence general courses for Energy Efficient Building Systems specialization - Part 2 (2025)',
    'courses':{('12362',):5, ('12611',):5, ('41465',):5, ('41468',):5, ('41469',):5},
    'requirement':5
}
