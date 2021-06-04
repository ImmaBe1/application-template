import configparser
from sys import exit
import os
from string import ascii_lowercase
from random import choice
from glob import glob
from flask import request

class ConfigFile:

    config = None
    filenames = None

    '''
    Accepts a property name and pulls that key from the properities file.
    If property is not found, then program will exit and log error and post to slack
    '''
    '''
    @staticmethod
    def readConfig(filename, property_name, section = 'main'):
        try:
            if ConfigFile.config is None or ConfigFile.filename != filename:
                ConfigFile.filename = filename
                ConfigFile.config = configparser.RawConfigParser()
                ConfigFile.config.read(filename)
            return ConfigFile.config.get(section, property_name)
        except Exception as ex:
            print('Error reading the properties file.', ex)
            exit(1)
   '''

    @staticmethod
    def writeConfig(file, property_name, property_value, section = 'main'):
        try:
            config = configparser.ConfigParser()
            config.read(file)
            config.set(section, property_name, property_value)
            
            with open(file, 'w') as configfile:
                config.write(configfile)

        except Exception as ex:
            print('Error write to the properties file.', ex)
            exit(1)

class Auxil:
    @staticmethod
    def read_file(filename):
        contents = ''
        try:
            file = open(filename, "r")
            contents = file.read()
        except OSError as e:
            print("Error: %s : %s" % (filename, e.strerror))
        return contents

    @staticmethod
    def write_to_file(filename, contents, method = "w"):
        try:
            if method not in ['w', 'a']:
                raise Exception('Invalid input to write a file requested: %s' % method)
            file = open(filename, method)
            file.write(contents)
            file.close()
        except OSError as e:
            print("Error: %s : %s" % (filename, e.strerror))
    
    @staticmethod
    def remove_file(filename):
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except OSError as e:
                print("Error: %s : %s" % (filename, e.strerror))
        else:
            print("The file: {} does not exist".format(filename))
    
    @staticmethod
    def remove_files(file_path, pattern):
        files = glob(file_path + '/' + pattern)
        for file in files:
            Auxil.remove_file(file)
    
    @staticmethod
    def is_file_exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def is_file_empty(file_path):
        return os.stat(file_path).st_size == 0

    @staticmethod
    def get_file_size_in_bytes(file_path):
        return os.path.getsize(file_path)

    @staticmethod
    def create_directory(dir_path):
        if os.path.exists(dir_path) == False:
            try:
                os.mkdir(dir_path)
            except OSError:
                print ("Unable to create a directory: %s" % dir_path)
                return False
        return True

    @staticmethod
    def create_full_file_path(filename):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError:
            print("Unable to create a filepath: " + filename)
            return False
        return True

    @staticmethod
    def get_random_string(string_len):
        letters = ascii_lowercase
        return ''.join(choice(letters) for i in range(string_len))
    
    @staticmethod
    def validate_form_parameters(parameters):
        missing_param = []
        for key in parameters:
            if key not in request.form:
                missing_param.append(key) 
        return missing_param