# -*- coding: utf-8 -*-
"""
Application
===========
"""

from __future__ import division, unicode_literals

import dash

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['APP']

APP = dash.Dash('Colour - Dash')
APP.config['suppress_callback_exceptions'] = True

APP.css.append_css({
    'external_url': [
        'http://colour-science.org/assets/css/all-nocdn.css',
        'http://colour-science.org/assets/css/font-awesome.css'
    ]
})
