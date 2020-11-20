#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 07:45:20 2020

@author: eholzbe
"""


from IPython.core.display import HTML

hide_code_str = '''
    <script>
    function hide_code() 
    {
     $('div.cell.code_cell.rendered.selected div.input').hide();        
    }
    </script>
'''
def hide_code():
    HTML(hide_code_str)
    