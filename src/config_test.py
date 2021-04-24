import configparser
import sys

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('pyXLL_Test.ini')
Debug_Mode = config.getboolean('SETTINGS', 'Debug_Mode')
Con1_server = config['DATABASE SETTINGS']['Con1_server']

print(Con1_server)
sys.exit("Boom")