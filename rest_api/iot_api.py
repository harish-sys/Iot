from flask import Blueprint, jsonify, make_response, request
import sys
import traceback

from sqlalchemy import func
from sqlalchemy.testing import db

# from iot_service import Iotservice
from iot_base.model import Device, Event, IotRepo
import json

iot_routes = Blueprint('iot_routes', __name__)
iot_repo = IotRepo()
# iot_service = Iotservice(iot_repo)


@iot_routes.route('/get/events', methods=['GET', 'POST'])
def get_events():
    device_id = request.json.get('device_id')
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')

    " Get Event by date range by using event device_id  "

    iot_device = iot_repo.get_events_by_date_range(device_id, start_date, end_date)
    if iot_device is None:
        raise Exception("data not found")

    return jsonify([{
        'id': event.id,
        'device_id': event.device_id,
        'timestamp': event.timestamp,
        'temperature': event.temperature
    } for event in iot_device])


@iot_routes.route('/summary', methods=['GET', 'POST'])
def get_summary():
    " Get data by using device id and timestamp as start and end date and also calculate max and min  avg  temperature"
    device_id = request.json.get('device_id')
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')

    summary = iot_repo.get_temperature_summary(device_id, start_date, end_date)

    return jsonify({
        'device_id': device_id,
        'min_temp': summary.min_temp,
        'max_temp': summary.max_temp,
        'avg_temp': summary.avg_temp
    })
