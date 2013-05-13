# This plugin sets necessary environment variables to run Bro with
# myricom load balancing.

import BroControl.plugin

class LBNetmap(BroControl.plugin.Plugin):
    def __init__(self):
        super(LBNetmap, self).__init__(apiversion=1)

    def name(self):
        return "lb_netmap"

    def pluginVersion(self):
        return 1

    def init(self):
        for nn in self.nodes():
            if nn.type != "worker":
                continue

            if nn.lb_method == "netmap":
                nn.env_vars += ["NETMAP_NUM_RINGS=%d" % int(nn.lb_procs)]
                nn.env_vars += ["NETMAP_NAME=%s" % nn.name]

