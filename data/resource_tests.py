from pprint import pprint
from requests import get, post, delete
from users import generate_password_hash

# pprint(get('http://localhost:5000/api/v2/users').json())
# pprint(get('http://localhost:5000/api/v2/users/1').json())
# pprint(get('http://localhost:5000/api/v2/users/2').json())
# pprint(delete('http://localhost:5000/api/v2/users/2').json())
# pprint(post('http://localhost:5000/api/v2/users', json={
#     'surname': 'papa',
#     'name': 'johns',
#     'age': 25,
#     'address': 'pizza_tower',
#     'position': 'papa',
#     'speciality': 'pizzamaker',
#     'hashed_password': generate_password_hash('123321'),
#     'email': 'bestpizz@papa.me'
# }).json())
# pprint(delete('http://localhost:5000/api/v2/users/2').json())

pprint(get('http://localhost:5000/api/v2/jobs').json())
pprint(get('http://localhost:5000/api/v2/jobs/1').json())
pprint(get('http://localhost:5000/api/v2/jobs/2').json())
pprint(delete('http://localhost:5000/api/v2/jobs/2').json())
pprint(post('http://localhost:5000/api/v2/jobs', json={
    'team_leader': 3,
    'collaborators': '1, 2, 4',
    'job': 'work',
    'work_size': 1,
    'is_finished': False
}).json())
pprint(delete('http://localhost:5000/api/v2/jobs/2').json())