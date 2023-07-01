# encoding: utf-8

import sys
from workflow import Workflow3
from xcmds import XCMDS

def main(wf):
    wf = Workflow3()
    args = wf.args
    if len(args) == 0:
        wf.logger.warn("[main] args is empty")
        return
    wf.logger.debug("[main] args: {}".format(args))
    
    cmd, arg = parse_args(args)
    if cmd == "" or arg == "":
        wf.logger.warn("[main] invalid cmd: %s or arg: %s", cmd, arg)
        return
    wf.logger.debug("[main] cmd: %s, arg: %s", cmd, arg)

    do_cmd = XCMDS.get(cmd)
    if do_cmd is None:
        wf.logger.warn("[main] undefined cmd: %s", cmd)
        return
    
    result = do_cmd(arg)
    wf.logger.debug("[main] result: %s", result)
    
    wf.add_item(title=u'{}'.format(result), 
                subtitle=u'Input: {}'.format(arg), 
                arg=u'{}'.format(result),
                valid=True)
    wf.send_feedback()
    
def parse_args(args):
    if len(args) < 2:
        return "", ""
    cmd = args[0].upper()
    return cmd, args[1]

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))