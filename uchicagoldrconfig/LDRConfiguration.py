
from os import access, R_OK
from os.path import dirname, exists, join, realpath
from configparser import ConfigParser

class LDRConfiguration(object):
    base_directory = realpath(__file__)
    config_directory = join(base_directory, 'config')

    def __init__(self):
        self.evaluate_for_config_data()
        self.db_info = {'user':data['Database'].get('db_user'),
                        'name':data['Database'].get('db_name'),
                        'host':data['Database'].get('db_host'),
                        'passwd':data['Database'].get('db_pass')}
        self.log_info = {'server':data['Logging'].get('server'),
                         'port':data['Logging'].get('port')}

    def check_config_directory(self):
        if not isdir(config):
            return False
        return True
    
    def check_writeability(self):
        return access(base_directory, W_OK)

    def make_config_directory(self):
        if self.check_writeability() and not isdir(config_directory):
            mkdir(config_directory):
            return True
        return False

    def check_for_config_file(self):
        return exists(join(config_directory,'ldr.ini'))

    def write_config_data(self, p):
        assert isinstance(p, ConfigParser)
        p.add_section('Database')
        p.add_section('Logging')
        p.set('Database','db_pass','replace_me')
        p.set('Database','db_user','fill_me_in_with_something_real')
        p.set('Database','db_host','example.com')
        p.set('Database','db_name','fill_me_in')
        p.set('Logging','server','example.com')
        p.set('Logging','port','1')        
        return p

    def retrieve_config_data(self):
        parser = ConfigParser()
        if check_for_config_file():
            parser.read(join(config_directory,'ldr.ini'))
        else:
            parser = self.write_config_data(parser)
        return parser

    def set_config_data(self, data_object):
        assert isinstance(data_object, ConfigParser)
        assert len(data_object.sections()) > 0
        self.data = data_object

    def evaluate_for_configdata(self):
        base_directory = dirname(realpath(__file__))
        config_file = join(base_directory,'config','ldr.ini')
        if not self.check_check_config_directory():
            self.make_config_directory()
        data = self.retrieve_configuration_data()
        self.set_config_data(data)


