#!/usr/bin/python
# encoding: utf-8

import os
import string
import sys
import workflow

def main(wf):

    log.debug('Started')

    if wf.update_available:
        log.debug("update available, attempting update")
        wf.start_update()

if __name__ == u"__main__":
    wf = workflow.Workflow(
            update_settings={
                'github_slug': 'plongitudes/SGLinkTransform',
                'frequency': 1
                }
            )
    log = wf.logger
    sys.exit(wf.run(main))

