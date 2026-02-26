from datetime import datetime
from .input.curriculum_specializations import curriculums
from .pdf_extractor import *
from .display_solutions import *

def curriculum_test(study_plan,options):
    # Implement the logic to test if the course_list meets the requirements
    student_name = extract_student_name(study_plan['transcript'])
    course_list = extract_course_numbers(study_plan['transcript'])+study_plan['extra courses']
    specialization = study_plan['specialization']
    start_year = study_plan['start year']
    current_year = datetime.now().year
    results = {}
    earned_ECTS = {}
    for year in set(range(start_year, current_year + 1)).intersection(curriculums[specialization].keys()):
        earned_ECTS[year] = {group['name']:0 for group in curriculums[specialization][year]}
        results[year] = {}
        for group in curriculums[specialization][year]:
            for (course,ECTS) in group['courses'].items():
                if any(subcourse in course_list for subcourse in course):
                    earned_ECTS[year][group['name']] += ECTS
            results[year][group['name']] = earned_ECTS[year][group['name']] >= group['requirement']     
    if any(all(results[year].values()) for year in set(range(start_year, current_year + 1)).intersection(curriculums[specialization].keys())):
        min_year = min(
            (year for year in set(range(start_year, current_year + 1)).intersection(curriculums[specialization].keys())
            if all(results[year].values())),
            default=None
            )
        print(f"{student_name} satisfies requirements for {specialization} in {min_year}/{min_year+1} (start year: {start_year}) - See full curriculum below:")
        if options['txt']:
            write_requirements_to_text(student_name, curriculums[specialization][min_year],course_list,earned_ECTS[min_year],specialization,min_year)
        if options['html']:
            write_requirements_to_html(student_name, curriculums[specialization][min_year],course_list,earned_ECTS[min_year],specialization,min_year,open_option=options['open_html'])
    else:
        print(f"{student_name} does NOT satisfy requirements for {specialization} (start year: {start_year}) - See details below:")
        for year in range(start_year, current_year + 1):
            if year in curriculums[specialization].keys():
                    #for group in curriculum:
                        #if results[group['name']] == False:
                            #print(f"{group['name']} not satisfied: {earned_ECTS[group['name']]} ECTS earned, {group['requirement']} ECTS required.")
                            #print_requirement_table(group, course_list)
                if options['txt']:
                    write_requirements_to_text(student_name,curriculums[specialization][year],course_list,earned_ECTS[year],specialization,year)
                if options['html']:
                    write_requirements_to_html(student_name,curriculums[specialization][year],course_list,earned_ECTS[year],specialization,year,open_option=options['open_html'])
            else:
                if year<current_year:
                    print(f"Missing courses for {year}/{year+1} curriculum: No data available.")
