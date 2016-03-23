# characters.py - analyse character interactions in Shakespeare plays
# Copyright (C) 2016 Unai Zalakain <unai@gisa-elkartea.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import csv
import re
import sys
from urllib import request
from bs4 import BeautifulSoup


ACTIONS = re.compile("(Enter|Exeunt|Exit|Re-enter)")
STAGE_CHANGE = lambda tag: tag.name == 'i' and ACTIONS.match(tag.text)
CHARACTER = lambda tag: tag.get('name', '').startswith('speech')


def appearances(soup):
    on_stage = set()
    soup = BeautifulSoup(soup, 'html.parser')
    all_characters = {character.text for character in soup.find_all(CHARACTER)}
    for tag in soup.find_all(STAGE_CHANGE):
        action, _, words = tag.text.partition(' ')
        action = action.lower()
        characters = {char for char in all_characters if char in words}
        if action == 'enter' or action == 're-enter':
            on_stage |= characters
        elif action == 'exeunt':
            on_stage = set()
        elif action == 'exit':
            on_stage -= characters
        yield on_stage.copy()


if __name__ == '__main__':
    soup = request.urlopen(sys.argv[1]).read()
    writer = csv.writer(sys.stdout)
    writer.writerow(['time', 'character'])
    for time, appearance in enumerate(appearances(soup)):
        for character in appearance:
            writer.writerow([time, character])
