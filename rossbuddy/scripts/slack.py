#!/usr/bin/env -S python3 -u

import os
import sys
import json
import logging
from urllib import request, parse
from supervisor import childutils

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    slack_token = os.environ.get('SLACK_BOT_TOKEN', None)
    slack_channel = os.environ.get('SLACK_CHANNEL', None)
    slack_disable = os.environ.get('SLACK_DISABLE', 'false')
    while True:
        headers,payload = childutils.listener.wait(
            sys.stdin,
            sys.stdout
        )

        if slack_disable.strip().lower() == 'true':
            childutils.listener.ok(sys.stdout)
            continue

        pheaders,pdata = childutils.eventdata(payload + '\n')
        eventname = headers['eventname']
        processname = pheaders['processname']

        if processname == 'slack':
            childutils.listener.ok(sys.stdout)
            continue

        if eventname == 'PROCESS_STATE_RUNNING':
            message = 'Ross Buddy is RUNNING'
            send_message(
                slack_token,
                slack_channel,
                message
            )
        elif eventname == 'PROCESS_STATE_EXITED':
            message = 'Ross Buddy has EXITED'
            send_message(
                slack_token,
                slack_channel,
                message
            )

        childutils.listener.ok(sys.stdout)

def send_message(token, channel, message):
    url = 'https://slack.com/api/chat.postMessage'
    data = {
        'channel': channel,
        'text': message
    }
    data = json.dumps(data).encode('utf-8')
    req =  request.Request(url, data=data)
    req.add_header('Authorization', f'Bearer {token}')
    req.add_header('Content-Type', 'application/json')
    r = request.urlopen(req)
    logger.info(f'slack response status {r.status}')

if __name__ == '__main__':
    main()
