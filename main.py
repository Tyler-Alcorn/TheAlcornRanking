import configparser

# Initialize the parser and read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the API key
api_key = config['DEFAULT']['CFBD_API_KEY']

# Your application logic here
print(f"API Key: {api_key}")


