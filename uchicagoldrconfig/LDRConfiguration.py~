

from configparser import ConfigParser, SectionProxy
from inspect import getfile, getmodulename, getsourcefile
from os import access, mkdir, R_OK, W_OK
from os.path import abspath, dirname, exists, isdir, join, realpath
import sys

class LDRConfiguration(object):
    _base_directory = dirname(realpath(__file__))
    _config_directory = join(_base_directory, 'config')

    def __init__(self, config_directory):
        self.set_base_directory(config_directory)
        print(self._base_directory)
        self.set_config_directory()
        self.evaluate_for_configdata()

    def set_config_directory(self):
        self._config_directory = join(self._base_directory, 'config')

    def set_base_directory(self, directory_path):
        assert isinstance(directory_path, str)
        assert exists(directory_path)
        self._base_directory = abspath(directory_path)
        self.evaluate_for_configdata()
        return True

    def get_config(self):
        out = dict()
        attributes = [x for x in dir(self) if not callable(getattr(self, x)) \
                      and not x.startswith('__') and not x.startswith('_') and isinstance(getattr(self, x), dict)]
        for n in attributes:
            out[n] = getattr(self,n)
        return out

    def check_config_directory(self):
        if not isdir(self._config_directory):
            return False
        return True
    
    def check_writeability(self):
        return access(self._base_directory, W_OK)

    def make_config_directory(self):
        if self.check_writeability() and not isdir(self._config_directory):
            mkdir(self._config_directory)
            return True
        return False

    def check_for_config_file(self):
        return exists(join(self._config_directory,'ldr.ini'))

    def write_config_data(self, p):
        assert isinstance(p, ConfigParser)
        p.add_section('Database')
        p.add_section('Logging')
        p.set('Database','db_host','example.com')
        p.set('Database','db_name','fill_me_in')
        p.set('Database','db_user','fill_me_in_with_something_real')
        p.set('Database','db_pass','replace_me')
        p.set('Logging','server','example.com')
        p.set('Logging','port','1')        
        return p

    def retrieve_config_data(self):
        parser = ConfigParser()
        if self.check_for_config_file():
            print("hi")
            parser.read(join(self._config_directory,'ldr.ini'))
        else:
            print("nope")
            parser = self.write_config_data(parser)
            cfgfile = open(join(self._config_directory,'ldr.ini'),'w')
            parser.write(cfgfile)
            cfgfile.close()
        return parser

    def set_config_data(self, data_object):
        assert isinstance(data_object, ConfigParser)
        assert len(data_object.sections()) > 0
        self.data = data_object

    def evaluate_for_configdata(self):
        config_file = join(self._base_directory,'config','ldr.ini')
        if not self.check_config_directory():
            self.make_config_directory()
        data = self.retrieve_config_data()
        self.retrieve_section_data(data)

    def define_value(self, a_dict, element, value):
        assert isinstance(a_dict, dict)
        assert isinstance(element, str)
        assert isinstance(value, str)
        a_dict[element] = value

    def retrieve_section_data(self, datum):
        assert isinstance(datum, ConfigParser)
        assert len(datum.sections()) > 0
        for n in datum.sections():
            self.retrieve_data_from_a_section(datum[n])

    def retrieve_data_from_a_section(self, section):
        assert isinstance(section, SectionProxy)
        section_name = section.name.lower()
        setattr(self, section_name, {})
        for key,value in section.items():
            getattr(self, section_name)[key] = value
