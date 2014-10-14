
class LimeWSAdapter:
    # def __init__(self):

    @staticmethod
    def get_events():
        return {
            'success': 'true',
            'events': [
                {'id': 1, 'name': 'Event1', 'date': '2014-01-01'},
                {'id': 2, 'name': 'Event2', 'date': '2014-01-02'}
            ]
        }

    @staticmethod
    def get_whisky_by_event(event_id):
        return {
            'success': 'true',
            'eventid': event_id,
            'whiskys': [
                {'id': 1, 'name': 'Whisky1'},
                {'id': 2, 'name': 'Whisky2'}
            ]
        }

    @staticmethod
    def get_users(event_id):
        return {
            'success': 'true',
            'eventid': event_id,
            'users': [
                {'id': 1, 'name': 'User1'},
                {'id': 2, 'name': 'User2'}
            ]
        }

    @staticmethod
    def add_review(review_data):
       return {
            'success': 'true'
        }