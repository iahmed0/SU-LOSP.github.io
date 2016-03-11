import csv
import re
import sys
from urllib import request
from bs4 import BeautifulSoup


ACTIONS = re.compile("(Enter|Exeunt|Exit)")
STAGE_CHANGE = lambda tag: tag.name == 'i' and ACTIONS.match(tag.text)


def appearances(soup):
    on_stage = set()
    soup = BeautifulSoup(soup, 'html.parser')
    for tag in soup.find_all(STAGE_CHANGE):
        action, _, words = tag.text.partition(' ')
        action = action.lower()
        characters = {w.strip() for w in words.split(',') if w.isupper()}
        if action == 'enter':
            on_stage |= characters
        elif action == 'exeunt':
            on_stage = set()
        elif action == 'exit':
            on_stage -= characters
        yield on_stage.copy()


if __name__ == '__main__':
    soup = request.urlopen(sys.argv[1]).read()
    data = list(appearances(soup))
    writer = csv.writer(sys.stdout)
    writer.writerow(['time', 'character'])
    for time, appearance in enumerate(data):
        for character in appearance:
            writer.writerow([time, character])
