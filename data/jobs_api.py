import flask
from flask import jsonify, request
from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')
fields = ('job', 'team_leader', 'collaborators', 'work_size', 'start_date', 'end_date', 'is_finished')


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify({'jobs': [item.to_dict(only=fields) for item in jobs]})


@blueprint.route('/api/jobs', methods=['POST'])
def post_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ('job', 'team_leader', 'collaborators', 'work_size', 'is_finished')):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    job = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    session.add(job)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify({'job': job.to_dict(only=fields)})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    session.delete(job)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
