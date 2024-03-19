from flask import jsonify, request
from flask_restful import abort, Resource
from data import db_session
from data.jobs import Jobs
from data.reqparse import job_parser

fields = ('id', 'job', 'team_leader', 'collaborators', 'work_size', 'start_date', 'end_date', 'is_finished')


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    user = session.query(Jobs).get(job_id)
    if not user:
        abort(404, message=f'Job id:{job_id} not found :(')


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(only=fields)})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(only=fields) for item in jobs]})

    def post(self):
        args = job_parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished'],
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
