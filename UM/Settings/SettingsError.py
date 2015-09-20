# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

##  Common base class for Setting file related errors.
class SettingsError(Exception):
    pass

##  Error thrown when a settings file misses certain keys or values.
class InvalidFileError(SettingsError):
    def __init__(self, path):
        super().__init__("File {0} is an invalid settings file".format(path))

##  Error thrown when a setting file's version does not match the current file version.
class InvalidVersionError(SettingsError):
    def __init__(self, path):
        super().__init__("Invalid version for file {0}".format(path))

##  Error thrown when a machine instance tries to use an unknown machine definition.
class DefinitionNotFoundError(SettingsError):
    def __init__(self, type_id):
        super().__init__("Could not find machine definition {0}".format(type_id))
