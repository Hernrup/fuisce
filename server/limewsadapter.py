import logging
from suds.client import Client
from xml.dom import minidom
import datetime

class LimeWSAdapter:
    def __init__(self):
        logging.getLogger('suds.client').setLevel(logging.DEBUG)
        url = 'http://luserver1011:8089/whisky/?wsdl'
        self._client = Client(url)

        print(self._client)

    def get_events(self):

        data = open('xmltemplates/events.xml').read()
        xmldoc = minidom.parseString(self._client.service.GetXmlQueryData(data))
        item_list = xmldoc.getElementsByTagName('event')
        events_list = []

        for s in item_list:
            events_list.append({'id': s.attributes['idevent'].value, 'name': s.attributes['name'].value})

        return {
            'events': events_list
        }

    def get_whisky_by_event(self, event_id):
        data = open('xmltemplates/whisky.xml').read()
        data = data.replace('{1}', (event_id if event_id else "-1"))
        result = self._client.service.GetXmlQueryData(data)
        xmldoc = minidom.parseString(result)
        item_list = xmldoc.getElementsByTagName('wut')
        result_list = []

        for s in item_list:
            result_list.append({'id': s.attributes['whisky.idwhisky'].value, 'name': s.attributes['whisky.name'].value})

        return {
            'eventid': event_id,
            'whiskys': result_list
        }

    def get_users(self, event_id):
        data = open('xmltemplates/users.xml').read()
        data = data.replace('{1}', (event_id if event_id else "-1"))
        result = self._client.service.GetXmlQueryData(data)
        xmldoc = minidom.parseString(result)
        item_list = xmldoc.getElementsByTagName('participant')
        result_list = []

        for s in item_list:
            result_list.append({'id': s.attributes['taster.idtaster'].value, 'name': s.attributes['taster.name'].value})

        return {
            'eventid': event_id,
            'users': result_list
        }

    def add_review(self, review_data):

        data = open('xmltemplates/addreview.xml').read()
        params = review_data.get('params').get('review')

        data = data.replace('{1}', params.get('user').get('id'))
        data = data.replace('{2}', params.get('event').get('id'))
        data = data.replace('{3}', params.get('whisky').get('id'))
        data = data.replace('{4}', str(params.get('points')))
        data = data.replace('{5}', str(params.get('smokyness')))
        data = data.replace('{6}', str(params.get('strength')))
        data = data.replace('{7}', params.get('nose'))
        data = data.replace('{8}', params.get('taste'))
        data = data.replace('{9}', params.get('finish'))
        data = data.replace('{10}', params.get('comment'))
        data = data.replace('{11}', str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        logging.info(review_data)
        logging.info(data)
        result = self._client.service.UpdateData(data)
        xmldoc = minidom.parseString(result)
        item_list = xmldoc.getElementsByTagName('error')

        return {
            'success': 'true'
        }