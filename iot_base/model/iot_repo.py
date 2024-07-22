from sqlalchemy import func

from DataBase import database_service
from iot_base.model.iot_event import Device, Event


class IotRepo:
    def __init__(self):
        self.session = database_service.db_session()

        pass

    def create_iot(self, iot_request):
        self.session.add(iot_request)
        self.session.commit()

    def get_events_by_date_range(self, device_id, start_date, end_date):
        print(device_id, start_date, end_date, "input ---------------")
        result = self.session.query(Event).filter(
            Event.device_id == device_id,
            Event.timestamp.between(start_date, end_date)
        ).all()
        return result

    def get_temperature_summary(self, device_id, start_date, end_date):
        print('NNNNNNNNNNNNNNNNNNNNNNNNN', device_id, start_date, end_date)
        summary = self.session.query(
            func.min(Event.temperature).label('min_temp'),
            func.max(Event.temperature).label('max_temp'),
            func.avg(Event.temperature).label('avg_temp')
        ).filter(
            Event.device_id == device_id,
            Event.timestamp.between(start_date, end_date)
        ).first()

        print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFF', summary)
        return summary
