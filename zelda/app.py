#!/usr/bin/env python
# see https://realpython.com/run-python-scripts/#using-the-script-filename

""" Entry point for application from 
"""

import logging, asyncio, sys
from datetime import datetime
import argparse # see https://docs.python.org/3/library/argparse.html#module-argparse
import server, markdown, scripts, backlinks

    
async def launch(args):
    """
        if cmd:
            if cmd['robot'] == 'tag_report':
                await tag_report(cmd['label'])
                with open(log_file) as file:  
                    note['body'] = note['body'] + '\n* * *\n' + file.read()
                    await server.update_note(note)
            else:
                logging.warning(f"Unknown script: {cmd['robot']}")
    """

    if args.cmd == 'scripts':
        result = await scripts.find()
        logging.info(result)
    elif args.cmd == 'backlinks':
        await server.edit_notes(backlinks.add_backlinks, args.tag, logging.getLogger())



def config_log(debug, log_file = 'app.log'):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format='%(levelname)s:%(message)s', 
        handlers=[logging.FileHandler(log_file,'w'), logging.StreamHandler()]
        )
    logging.debug(f"Zelda launching at {datetime.now()}.")

def config_arg_parser():
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Turns Joplin into a Zettelkasten')
    parser.add_argument('cmd', help=f"The command Zelda will run", choices=['scripts', 'backlinks'])
    parser.add_argument("-d", "--debug", help="Print debug messages", action="store_true")
    parser.add_argument("-t", "--tag", help="Only process notes with this tag")
    args = parser.parse_args(sys.argv[1:])
    config_log(args.debug)
    #print(sys.path)
    asyncio.run(launch(args))