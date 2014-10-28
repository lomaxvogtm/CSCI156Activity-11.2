__author__ = 'Madeleine'

transcript = {'Fall 2013': [['CHEM', '105', '01', 'General Chemistry I'], ['PHIL', '214', '01', 'FYE Ethics'],
             ['MUSI', '215', '01', 'Symphonic Band'], ['FREN', '101', '01', 'French I']],
              'Spring 2014': [['CHEM', '106', '01', 'General Chemistry I'], ['CHEM', '313', '01', 'Environmental Chemistry'],
             ['MUSI', '217', '01', 'Jazz Band'], ['FREN', '102', '01', 'French II']],
              'Fall 2014': [['CHEM', '313', '01', 'Organic Chemistry I'], ['CSCI', '156', '01', 'GitHub Appreciation'],
             ['PHYS', '125', '01', 'Physics I'], ['FREN', '201', '02', 'French III']],
              'Spring 2015': [['CHEM', '316', '01', 'Organic Chemistry II'], ['PHYS', '126', '01', 'Physics II'],
             ['FREN', '202', '01', 'French IV'], ['BIOL', '345', '01', 'Human Disease']]}

def printtranscript(transcript):
    for semester in transcript:
        print(semester)
        for course in transcript[semester]:
            print(len(str(semester))*" "+course[0]+" "+ course[1]+" "+course[2]+" "+course[3])

def semesters(subject, transcript):
    for semester in transcript:
        for course in transcript[semester]:
            if course[0] == subject:
                print (semester)
                break




semesters('PHIL', transcript)
