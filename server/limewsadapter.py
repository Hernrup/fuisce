
class LimeWSAdapter:
    # def __init__(self):

    @staticmethod
    def get_events():
        return {
            'success': 'true',
            'tastings': [
                {'id': 1, 'name': 'Whisky1', 'date': '2014-01-01'},
                {'id': 2, 'name': 'Whisky2', 'date': '2014-01-02'}
            ]
        }

    @staticmethod
    def get_whisky_by_event(event_id):
        return {
            'success': 'true',
            'eventid': event_id,
            'drinks': [
                {'id': 1, 'name': 'Whisky1'},
                {'id': 2, 'name': 'Whisky2'}
            ]
        }

    @staticmethod
    def get_users():
        return {
            'success': 'true',
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