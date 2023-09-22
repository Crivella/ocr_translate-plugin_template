###################################################################################
# {{cookiecutter.plugin_name}} - a plugin for ocr_translate              #
# Copyright (C) 2023-present {{ cookiecutter.github_user }}                                      #
#                                                                                 #
# This program is free software: you can redistribute it and/or modify            #
# it under the terms of the GNU General Public License as published by            #
# the Free Software Foundation, either version 3 of the License.                  #
#                                                                                 #
# This program is distributed in the hope that it will be useful,                 #
# but WITHOUT ANY WARRANTY; without even the implied warranty of                  #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                   #
# GNU General Public License for more details.                                    #
#                                                                                 #
# You should have received a copy of the GNU General Public License               #
# along with this program.  If not, see {http://www.gnu.org/licenses/}.           #
#                                                                                 #
# Home: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}                          #
###################################################################################
"""{{ cookiecutter.short_description }}"""

__version__ = '{{ cookiecutter.version }}'

box_model_data = {
    # Name of the model that will be created in the user database and displayed in the extension
    "name": "{{ cookiecutter.model_name_prefix }}",
    # List of ISO 639-1 codes of the languages that will be supported by the model
    "lang": [],
    # How the model requires the codes to be passed (one of 'iso1', 'iso2b', 'iso2t', 'iso3')
    # If the models codes only partially match or are totally different from one of the ISO standards, see iso1_map
    "lang_code": "iso1",
    # Name of the entrypoint for the model (should match what is used in pyproject.toml)
    "entrypoint": "{{cookiecutter.entry_point_prefix}}.box",
    # Maps ISO-639-1 codes to the codes used by the model. Does not need to map every language, only those that are
    # different from getattr(lang: m.Language, lang_code)
    "iso1_map": {}
}

ocr_model_data = {
    # Name of the model that will be created in the user database and displayed in the extension
    "name": "{{ cookiecutter.model_name_prefix }}",
    # List of ISO 639-1 codes of the languages that will be supported by the model
    "lang": [],
    # How the model requires the codes to be passed (one of 'iso1', 'iso2b', 'iso2t', 'iso3')
    # If the models codes only partially match or are totally different from one of the ISO standards, see iso1_map
    "lang_code": "iso1",
    # Name of the entrypoint for the model (should match what is used in pyproject.toml)
    "entrypoint": "{{cookiecutter.entry_point_prefix}}.box",
    # Maps ISO-639-1 codes to the codes used by the model. Does not need to map every language, only those that are
    # different from getattr(lang: m.Language, lang_code)
    "iso1_map": {}
}

tsl_model_data = {
    # Name of the model that will be created in the user database and displayed in the extension
    "name": "{{ cookiecutter.model_name_prefix }}",
    # List of ISO 639-1 codes of the source languages that will be supported by the model
    "lang_src": [],
    # List of ISO 639-1 codes of the destination languages that will be supported by the model
    "lang_dst": [],
    # How the model requires the codes to be passed (one of 'iso1', 'iso2b', 'iso2t', 'iso3')
    # If the models codes only partially match or are totally different from one of the ISO standards, see iso1_map
    "lang_code": "iso1",
    # Name of the entrypoint for the model (should match what is used in pyproject.toml)
    "entrypoint": "{{cookiecutter.entry_point_prefix}}.box",
    # Maps ISO-639-1 codes to the codes used by the model. Does not need to map every language, only those that are
    # different from getattr(lang: m.Language, lang_code)
    "iso1_map": {}
}
