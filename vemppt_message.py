#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This file is part of vemppt_reader.

    vemppt_reader is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    vemppt_reader is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with vemppt_reader.  If not, see <https://www.gnu.org/licenses/>.
"""

import platform
if platform.system() == 'Windows':
    def print_message(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
else:
    def print_message(title, text, style):
        print("[!] " + title + ": " + text)

if __name__ == '__main__':
    print("[!] Wrong execution!\nPlease, run main.py or test the register with offtest.py")
