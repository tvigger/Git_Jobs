from pprint import pprint
from requests import post
from requests import get
from requests import delete

# pprint(get('http://127.0.0.1:5000/api/jobs').json())
# pprint(get('http://127.0.0.1:5000/api/jobs/1').json())
# pprint(get('http://127.0.0.1:5000/api/jobs/999').json())
# pprint(get('http://127.0.0.1:5000/api/jobs/one').json())

# pprint(post('http://127.0.0.1:5000/api/jobs', json={
#     'team_leader': '2',
#     'collaborators': '1, 3, 4',
#     'job': 'get some sleep',
#     'work_size': '9',
#     'is_finished': False
# }).json())
# pprint(post('http://127.0.0.1:5000/api/jobs', json={}).json())
# pprint(post('http://127.0.0.1:5000/api/jobs', json={
#     'team_leader': '2',
#     'collaborators': '1, 3, 4',
#     'work_size': '9',
#     'is_finished': False
# }).json())
# pprint(post('http://127.0.0.1:5000/api/jobs', json={
#     'team_leader': '2',
#     'collaborators': '1, 3, 4',
#     'job': 'get some sleep',
#     'work_size': '9',
# }).json())
# pprint(get('http://127.0.0.1:5000/api/jobs').json())

post('http://127.0.0.1:5000/api/jobs', json={
    'team_leader': 2,
    'collaborators': '1, 3, 4',
    'job': 'get some sleep',
    'work_size': 9,
    'is_finished': False
})
# pprint(get('http://127.0.0.1:5000/api/jobs').json())
# pprint(delete('http://127.0.0.1:5000/api/jobs/4').json())
# pprint(delete('http://127.0.0.1:5000/api/jobs/999').json())
# pprint(delete('http://127.0.0.1:5000/api/jobs/one').json())
# pprint(get('http://127.0.0.1:5000/api/jobs').json())
