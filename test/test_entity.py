import unittest

from iolite.entity import EntityFactory, RadiatorValve, Room, Switch

EXAMPLE_HEATER = {'properties': [
    {'timestamp': 1580472165268, 'name': 'valvePosition', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': True, 'requestedValue': None,
     'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'FunctionValueAsStringDatapoint',
                                'internal': False, 'hashCode': 22945785, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': 0.0, 'predictions': [], 'valueFriendlyName': 'Closed', 'ranges': [], 'hashCode': 23808661,
     'class': 'DoubleProperty', 'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580425966790, 'name': 'heatingMode', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': True, 'requestedValue': None,
     'requestedValueTimestamp': 1580397443162,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'FunctionValueAsStringDatapoint',
                                'internal': False, 'hashCode': 19818913, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': 'Normal', 'predictions': [], 'hashCode': 23639409, 'class': 'TextProperty',
     'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580414086827, 'name': 'waterFeedTemperature', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': False, 'requestedValue': None,
     'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'FunctionValueAsStringDatapoint',
                                'internal': False, 'hashCode': 13792398, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': 45.0, 'predictions': [], 'valueFriendlyName': None, 'ranges': [], 'hashCode': 29146318,
     'class': 'DoubleProperty', 'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580397428874, 'name': 'supportedCommunicationIntervals', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': False, 'requestedValue': None,
     'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'FunctionValueAsStringDatapoint',
                                'internal': False, 'hashCode': 27010580, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': '0,120,300,600,1200,1800,3600,28800', 'predictions': [], 'hashCode': 3342299,
     'class': 'TextProperty', 'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580472165268, 'name': 'currentEnvironmentTemperature', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': False, 'requestedValue': None,
     'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'FunctionValueAsStringDatapoint',
                                'internal': False, 'hashCode': 20061228, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': 19.0, 'predictions': [], 'valueFriendlyName': None, 'ranges': [], 'hashCode': 30576386,
     'class': 'DoubleProperty', 'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580472165268, 'name': 'batteryLevel', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': False, 'requestedValue': None,
     'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'BatteryLowDatapoint', 'internal': False,
                                'hashCode': 7283277, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': 100.0, 'predictions': [], 'valueFriendlyName': None, 'ranges': [], 'hashCode': 5645101,
     'class': 'DoubleProperty', 'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580472165268, 'name': 'rssi', 'namespaceURI': 'http://iolite.de', 'element': '25561123',
     'readable': True, 'writable': False, 'requestedValue': None, 'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'FunctionValueAsStringDatapoint',
                                'internal': False, 'hashCode': 772429, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': -64.0, 'predictions': [], 'valueFriendlyName': 'Very good', 'ranges': [], 'hashCode': 8125618,
     'class': 'DoubleProperty', 'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580472165268, 'name': 'heatingTemperatureSetting', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': True, 'requestedValue': None,
     'requestedValueTimestamp': 1580425366889,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'FunctionValueAsStringDatapoint',
                                'internal': False, 'hashCode': 12950729, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': 6.5, 'predictions': [], 'valueFriendlyName': None, 'ranges': [], 'hashCode': 11690872,
     'class': 'DoubleProperty', 'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580472165335, 'name': 'communicationInterval', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': True, 'requestedValue': None,
     'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'FunctionValueAsStringDatapoint',
                                'internal': False, 'hashCode': 29020087, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': 600, 'predictions': [], 'valueFriendlyName': None, 'ranges': [], 'hashCode': 5163525,
     'class': 'IntegerProperty', 'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1579794418064, 'name': 'repeaterRssi', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': False, 'requestedValue': None,
     'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'FunctionValueAsStringDatapoint',
                                'internal': False, 'hashCode': 1073663, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': None, 'predictions': [], 'valueFriendlyName': 'Very good', 'ranges': [], 'hashCode': 27860123,
     'class': 'DoubleProperty', 'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580472165268, 'name': 'windowStatusAssessment', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': False, 'requestedValue': None,
     'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'OpenClosedToBooleanDatapoint',
                                'internal': False, 'hashCode': 9612915, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': False, 'predictions': [], 'hashCode': 18993657, 'class': 'BooleanProperty',
     'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 1580397429005, 'name': 'deviceStatus', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'readable': True, 'writable': False, 'requestedValue': None,
     'requestedValueTimestamp': 0,
     'dataPointConfiguration': {'configuration': {}, 'dataPointType': 'IOLITEDeviceStatus', 'internal': True,
                                'hashCode': 2472974, 'class': 'DataPointConfiguration',
                                'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
     'value': 'OK', 'predictions': [], 'hashCode': 441420, 'class': 'TextProperty',
     'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'}], 'attributes': [
    {'timestamp': 0, 'name': 'gatewayIdentifier', 'namespaceURI': 'http://iolite.de', 'element': '25561123',
     'value': '01932471', 'hashCode': 28287297, 'class': 'TextAttribute',
     'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'},
    {'timestamp': 0, 'name': 'configuredLocationName', 'namespaceURI': 'http://iolite.de',
     'element': '25561123', 'value': 'Bad', 'hashCode': 32771072, 'class': 'TextAttribute',
     'ePackageURI': 'http://www.iolite.de/models/Properties-2.0.ecore'}], 'graphicalSymbolURI': None,
    'started': True, 'driverIdentifier': 'enocean-ip-driver.jar', 'typeNamespaceURI': 'http://iolite.de',
    'typeName': 'Heater', 'dataPointConfiguration': {}, 'id': 'id-1',
    'friendlyName': 'Stellantrieb_0', 'positionTimeStamp': 0,
    'placeIdentifier': 'placeIdentifier-1', 'environment': '7626396',
    'manufacturer': 'Jaeger Direkt', 'modelName': None, 'hashCode': 25561123, 'class': 'Device',
    'ePackageURI': 'http://www.iolite.de/environment-1.0.ecore'}


class MyTestCase(unittest.TestCase):
    def test_create_heater(self):
        entity_factory = EntityFactory()
        heater = entity_factory.create(EXAMPLE_HEATER)
        self.assertIsInstance(heater, RadiatorValve)
        self.assertEqual(heater.identifier, 'id-1')
        self.assertEqual(heater.name, 'Stellantrieb_0')

    def test_add_device_to_room(self):
        room = Room('1', 'Bedroom')
        switch = Switch('2', 'Bedroom Switch', 'Generic')
        room.add_device(switch)
        self.assertEqual(len(room.devices), 1)
        self.assertEqual(room.devices[0], switch)


if __name__ == '__main__':
    unittest.main()
