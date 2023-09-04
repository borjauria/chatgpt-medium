import configparser

# Method to read config file settings
def read_config():
    """
    Loads and parses the configuration data from 'config.ini'.

    This function reads the 'config.ini' file located in the current working directory
    and returns a configuration object containing the sections and their respective settings.

    Returns:
        config: A configuration object containing data from 'config.ini'.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config