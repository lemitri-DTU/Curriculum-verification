from src.curriculum_test import *

#Define the student's characteristics
study_plan = {
    'transcript': '/Users/lesiamitridati/Desktop/RA060U_JMgHINbR_5106077.pdf',
    'extra courses': ['42114'],
    'specialization': 'Energy Systems Analysis',
    'start year': 2023
}

#Choose the options to tune the outputs of the curriculum_test function
options = {
   'txt': True,
   'html': False,
   'open_html': False
}

# run verification test
curriculum_test(study_plan,options)
