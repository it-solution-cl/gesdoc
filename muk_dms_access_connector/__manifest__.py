# -*- coding: utf-8 -*-

###################################################################################
# 
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    'name': "MuK Documents Access Connector",
    'summary': """Documents Connector""",
    'description': """ 
        Technical module to provide some utility features. The
        module is mainly used as a dependency by other modules
        and to provide a collection of common service functions.
    """,
    'version': '11.0.0.0.1',   
    'category': 'Hidden',   
    'license': 'AGPL-3',    
    'author': "MuK IT",
    'website': "http://www.mukit.at",
    'contributors': [
        "Mathias Markl <mathias.markl@mukit.at>",
    ],
    'depends': [
        'muk_dms',
        'muk_dms_access',
        'muk_dms_connector'
    ],
    "data": [
    ],
    'images': [
        'static/description/banner.png'
    ],
    "installable": True,
    "auto_install": True
}