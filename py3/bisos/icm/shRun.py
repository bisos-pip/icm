# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: A /library/ Beginning point for development of new ICM oriented libraries.
"""

import typing

icmInfo: typing.Dict[str, typing.Any] = { 'moduleDescription': ["""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
*** concept             -- Desctiption of concept
**      [End-Of-Description]
"""], }

icmInfo['moduleUsage'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""

icmInfo['moduleStatus'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current     :: For now it is an ICM. Turn it into ICM-Lib. [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:py:name :style "fileName"
icmInfo['moduleName'] = "shRun"
####+END:

####+BEGIN: bx:icm:py:version-timestamp :style "date"
icmInfo['version'] = "202110240036"
####+END:

####+BEGIN: bx:icm:py:status :status "Production"
icmInfo['status']  = "Production"
####+END:

icmInfo['credits'] = ""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/icmInfo-mbNedaGplByStar.py"
icmInfo['authors'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['copyright'] = "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]"
icmInfo['licenses'] = "[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"
icmInfo['maintainers'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['contacts'] = "[[http://mohsen.1.banan.byname.net/contact]]"
icmInfo['partOf'] = "[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]"
####+END:

icmInfo['panel'] = "{}-Panel.org".format(icmInfo['moduleName'])
icmInfo['groupingType'] = "IcmGroupingType-pkged"
icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"


####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/bisos/git/auth/bxRepos/bisos-pip/icm/py3/bisos/icm/shRun.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][??]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][??]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=  :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:


# import os
# import pwd
# import grp
# import collections
# import enum
#
#import traceback

# import pathlib

from invoke import run

from deprecated import deprecated

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__
####+END:


####+BEGIN: bx:icm:py3:func :funcName "bash" :funcType "" :retType "" :deco "deprecated(\"moved to bpf\")" :argsList "" :comment "Runs As Root"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][??]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][??]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /bash/ =Runs As Root= deco=deprecated("moved to bpf")  [[elisp:(org-cycle)][| ]]
#+end_org """
@deprecated("moved to bpf")
def bash(
####+END:
    command,
    **kwargs
):
####+END:
    """Based on verbosity level, add appropriate kwargs.

Based on --verbosity set hide=False
Based on --callTracking set echo=True
"""

    #icm.TM_here("Args: {}".format(args))
    for key in kwargs:
        icm.TM_here("keyword arg: %s: %s" % (key, kwargs[key]))

    specifiedArg_hide = kwargs.pop('hide', None)
    specifiedArg_echo = kwargs.pop('echo', None)
    # specifiedArg_warn = kwargs.pop('warn', None)

    verbosityLevel = icm.icmRunArgs_verbosityLevel()

    if specifiedArg_hide is not None:
        kwargs['hide'] = specifiedArg_hide
    else:
        if verbosityLevel >= 30:
            #kwargs['hide'] = True    # True is different from 'both' in that it overrides echo=True
            kwargs['hide'] = 'both'
        else:
            kwargs['hide'] = False

    if specifiedArg_echo is not None:
        kwargs['echo'] = specifiedArg_echo
    else:
        if icm.icmRunArgs_isCallTrackingMonitorOn():
            kwargs['echo'] = True
        else:
            kwargs['echo'] = False


    #result = run(command, hide=True, warn=True, echo=True)
    #print(kwargs)

    result = run(command, **kwargs)
    return result


####+BEGIN: bx:dblock:python:section :title "Basic Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Basic Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:icm:py3:func :funcName "cmnds" :funcType "" :retType "" :deco "deprecated(\"moved to bpf\")" :argsList "" :comment "Runs As Root"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][??]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][??]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /cmnds/ =Runs As Root= deco=deprecated("moved to bpf")  [[elisp:(org-cycle)][| ]]
#+end_org """
@deprecated("moved to bpf")
def cmnds(
####+END:
        cmnd,
        **kwArgs,
):
    """
** Adds a sudo to cmnd
    """
    retVal =  icm.subProc_bash(cmnd, **kwArgs)
    return retVal


####+BEGIN: bx:icm:py3:func :funcName "sudoCmnds" :funcType "" :retType "" :deco "deprecated(\"moved to bpf\")" :argsList "" :comment "Runs As Root"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][??]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][??]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /sudoCmnds/ =Runs As Root= deco=deprecated("moved to bpf")  [[elisp:(org-cycle)][| ]]
#+end_org """
@deprecated("moved to bpf")
def sudoCmnds(
####+END:
        cmnd,
        **kwArgs,
):
    """
** Adds a sudo to cmnd
    """
    sudoedCmnd = """sudo -- sh -c '{cmnd}'""".format(cmnd=cmnd)
    retVal =  icm.subProc_bash(sudoedCmnd, **kwArgs)
    return retVal

####+BEGIN: bx:icm:py3:func :funcName "sudoOut" :funcType "" :retType "" :deco "deprecated(\"moved to bpf\")" :argsList "" :comment "Runs As Root"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][??]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][??]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /sudoOut/ =Runs As Root= deco=deprecated("moved to bpf")  [[elisp:(org-cycle)][| ]]
#+end_org """
@deprecated("moved to bpf")
def sudoOut(
####+END:
        cmnd,
        **kwArgs,
):
    """
** Adds a sudo to
    """
    sudoedCmnd = """sudo -- sh -c '{cmnd}'""".format(cmnd=cmnd)
    return icm.subProc_bashOut(sudoedCmnd, **kwArgs)



####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
