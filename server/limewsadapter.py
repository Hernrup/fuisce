
class LimeWSAdapter:
    def __init__(self):
        print("Init")

    @staticmethod
    def get_tastings(self):
        return {
            'success': 'true',
            'tastings': [
                {'id': 1, 'name': 'Whisky1', 'date': '2014-01-01'},
                {'id': 2, 'name': 'Whisky2', 'date': '2014-01-02'}
            ]
        }

    @staticmethod
    def get_drinks_for_tasting(self, tastingid):
        return {
            'success': 'true',
            'drinks': [
                {'id': 1, 'name': 'Whisky1'},
                {'id': 2, 'name': 'Whisky2'}
            ]
        }

    @staticmethod
    def get_users(self):
        return {
            'success': 'true',
            'users': [
                {'id': 1, 'name': 'User1'},
                {'id': 2, 'name': 'User2'}
            ]
        }

    @staticmethod
    def add_review(self):
       return {
            'success': 'true'
        }