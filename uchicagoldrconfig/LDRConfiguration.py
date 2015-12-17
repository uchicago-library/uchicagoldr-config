
from os import access, R_OK
from os.path import dirname, exists, join, realpath
from configparser import ConfigParser

class LDRConfiguration(object):
    def __init__(self):
        data = self.search_for_configurationdata()
        self.db_info = {'user':data['Database'].get('db_user'),
                        'name':data['Database'].get('db_name'),
                        'host':data['Database'].get('db_host'),
                        'passwd':data['Database'].get('db_pass')}
        self.log_info = {'server':data['Logging'].get('server'),
                         'port':data['Logging'].get('port')}

    def search_for_configurationdata(self):
        base_directory = dirname(realpath(__file__))
        config_file = join(base_directory,'config','ldr.ini')
        print(config_file)
        print(access(config_file, R_OK))
        if exists(config_file):
            print("hola")
            parser = ConfigParser()
            opened_file = open(config_file,'r')
            parser.read(config_file)
        else:
            config_file = open(join(base_directory,'config','ldr.ini'),'w')
            parser.add_section('Database')
            parser.add_section('Logging')
            parser.set('Database','db_pass','replace_me')
            parser.set('Database','db_user','fill_me_in_with_something_real')
            parser.set('Database','db_host','example.com')
            parser.set('Database','db_name','fill_me_in')
            parser.set('Logging','server','example.com')
            parser.set('Logging','port','1')
            parser.write(config_file)
        config_data = parser
        return config_data


