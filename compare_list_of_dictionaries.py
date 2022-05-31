list_of_studyContent_of_upcomingLiveClass = [
  {
    "endTime": "7:30 AM",
    "scheduleID": 14330734,
    "startTime": "7:00 AM",
    "subject": "English",
    "subjectLevel": "Level G1",
    "subjectWeek": "26-Z",
    "test": True
  },
  {
    "endTime": "8:00 AM",
    "scheduleID": 14371946,
    "startTime": "7:30 AM",
    "subject": "Math",
    "subjectLevel": "Level 0B",
    "subjectWeek": "2-B",
    "test": False
  },
  {
    "endTime": "7:30 AM",
    "scheduleID": 14371966,
    "startTime": "7:00 AM",
    "subject": "English",
    "subjectLevel": "Master Reader",
    "subjectWeek": "1-A",
    "test": False
  },
  {
    "endTime": "8:00 AM",
    "scheduleID": 14375000,
    "startTime": "7:30 AM",
    "subject": "Math",
    "subjectLevel": "Level 6A",
    "subjectWeek": "6-F",
    "test": True
  }
]

list_of_students_of_schedules = [
  {
    "endTime": "7:30 AM",
    "scheduleID": 14330734,
    "startTime": "7:00 AM",
    "studentID": 118727,
    "studentName": "Mon1 Dec",
    "subject": "English",
    "subjectLevel": "Level G1",
    "subjectWeek": "26-Z",
    "test": True
  },
  {
    "endTime": "7:30 AM",
    "scheduleID": 14371966,
    "startTime": "7:00 AM",
    "studentID": 118728,
    "studentName": "Mon2 Dec",
    "subject": "English",
    "subjectLevel": "Master Reader",
    "subjectWeek": "1-A",
    "test": False
  },
  {
    "endTime": "8:00 AM",
    "scheduleID": 14371946,
    "startTime": "7:30 AM",
    "studentID": 118727,
    "studentName": "Mon1 Dec",
    "subject": "Math",
    "subjectLevel": "Level 0B",
    "subjectWeek": "2-B",
    "test": False
  },
  {
    "endTime": "8:00 AM",
    "scheduleID": 14375000,
    "startTime": "7:30 AM",
    "studentID": 118728,
    "studentName": "Mon2 Dec",
    "subject": "Math",
    "subjectLevel": "Level 6A",
    "subjectWeek": "6-F",
    "test": True
  }
]


# def check_attributes(a, b):
#     count = 0
#     for a_item in a:
#         for b_item in b:
#             if a_item['scheduleID'] == b_item['scheduleID']:
#                 count += 1
#                 print(f"scheduleID Matched for {a_item['scheduleID']}")
#                 if a_item['endTime'] == b_item['endTime']:
#                     print(f'endTime Matched')
#                     count += 1
#                 if a_item['startTime'] == b_item['startTime']:
#                     print('startTime Matched')
#                     count += 1
#                 if a_item['subject'] == b_item['subject']:
#                     print('subject Matched')
#                     count += 1
#                 if a_item['subjectLevel'] == b_item['subjectLevel']:
#                     print('subjectLevel Matched')
#                     count += 1
#                 if a_item['subjectWeek'] == b_item['subjectWeek']:
#                     print('subjectWeek Matched')
#                     count += 1
#                 if a_item['test'] == b_item['test']:
#                     print('test Matched')
#                     count += 1
#                 break
#             else:
#                 continue
#     return count


# number_of_validated_attributes = check_attributes(list_of_studyContent_of_upcomingLiveClass, list_of_students_of_schedules)
# print(number_of_validated_attributes)
# for b_item in b:
#     del b_item['studentID']
#     del b_item['studentName']
#
# print(b)


list_of_subjects_upcoming_live_class = [
    {
        "scheduleID": 14330820,
        "subject": "English",
        "subjectWeek": "19-S",
        "subjectLevel": "Level M1",
        "startTime": "5:30 PM",
        "endTime": "6:00 PM",
        "test": False
    },
    {
        "scheduleID": 14372007,
        "subject": "Math",
        "subjectWeek": "1-A",
        "subjectLevel": "Level 8",
        "startTime": "6:00 PM",
        "endTime": "6:30 PM",
        "test": True
    }
]

list_of_subjects_schedules = [
    {
        "scheduleID": 14330820,
        "subject": "English",
        "subjectWeek": "19-S",
        "subjectLevel": "Level M1",
        "startTime": "5:30 PM",
        "endTime": "6:00 PM",
        "test": False
    },
    {
        "scheduleID": 14372007,
        "subject": "Math",
        "subjectWeek": "1-A",
        "subjectLevel": "Level 8",
        "startTime": "6:00 PM",
        "endTime": "6:30 PM",
        "test": True
    }
]

print(list_of_subjects_upcoming_live_class == list_of_subjects_schedules)
