import os
import sys
from unittest import TestCase
from django.conf import settings

try:
    from friskby_gw import FriskByGW
except ImportError:
    path = os.path.join( settings.BASE_DIR , "GW")
    sys.path.insert( 0 , path )
    from friskby_gw import FriskByGW , FriskBySensor
    sys.path.pop(0)



class GWTest(TestCase):
    def setUp(self):
        pass


    def test_get_sensors(self):
        gw = FriskByGW()
        sensors = gw.sensorList()
        for sensor in sensors:
            self.assertTrue( isinstance( sensor , FriskBySensor ))
            
        if len(sensors) > 0:
            sensor = sensors[0]
        
        last_value = sensor.getLastValue( )
        

        
    def test_get_sensor(self):
        gw = FriskByGW( )
        sensor = gw.getSensor( "NO/does/not/exist")
        self.assertIsNone( sensor )
        
