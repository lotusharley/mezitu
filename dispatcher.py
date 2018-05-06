# -*- coding: utf-8 -*-
#python
import zmq
from baseconfig import defaultconfig

if __name__ == '__main__':
    config = defaultconfig()
    zContext = zmq.Context()
    zSock = zContext.socket(zmq.PUB)
    zSock.bind(config.PUBLISHER_URL)
    while True:
        s =raw_input('Press Anykey To Exit...')
        zSock.send('end')
        break
    zSock
    quit()
    