import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

url = config.get('default', 'url')

print url
