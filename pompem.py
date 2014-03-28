# -*- coding: UTF-8 -*-

import sys
if sys.version_info > (2, 6):
    import argparse
else:
    import optparse

from Engine.Update import UpdateVersion
from Engine.ExecAndPrint import execute

sys.path.insert(0, '..')


def args_to_legacy():
    print "Legacy"


def args_to_newer():
    print "Mew"


def main():
    #TODO: Remove comment.
    # IF Python < 2.7:
    parser = optparse.OptionParser(add_help_option=False)
    # ELSE:
    parser = argparse.ArgumentParser(description='Explot find tool')

    #
    # Para atender a PEP8 no quesito
    # http://legacy.python.org/dev/peps/pep-0008/#maximum-line-length
    # verificar a possibilidade de substituir essa criação de argumentos
    # com YAML ou JSON.
    #

    #
    # TODO: Que tal em vez de usar --html e --text usar:
    # --format com opções [txt|html|json|csv]
    #
    parser.add_argument(
        '-m',
        '--html',
        dest='fileHtml',
        action='store_true',
        help='entre the file name'
    )
    parser.add_argument(
        '-s',
        '--search',
        dest='keywords',
        type=str,
        help='text for search'
    )
    parser.add_argument(
        '-t',
        '--text',
        dest='fileText',
        action='store_true',
        help='entre the file name'
    )
    parser.add_argument(
        '-u',
        '--update',
        dest='update',
        action='store_true',
        help='upgrade to latest version'
    )


    # TODO: Remove this after changes.
    # parser.add_option("-s", "--search", dest="keywords", type="string",
    #                                     help="text for search",)

    # parser.add_option("--txt", dest="fileText", \
    #                   action="store_true", help="enter the file name",)

    # parser.add_option("--html", dest="fileHtml", action="store_true", \
    #                   help="enter the file name",)

    # parser.add_option("--update",
    #               action="store_true", dest="update",
    #               help="upgrade to latest version")

    # parser.add_option("-h", "--help",
    #                   action="store_true", dest="help", help="-h")

    # (options, args) = parser.parse_args()

    # argsParameters = {}
    # keywords = options.keywords
    # fileText = options.fileText
    # fileHtml = options.fileHtml
    # update = options.update
    # help = options.help

    args = parser.parser_args()



    if help:
       printHelpMessage()
       return
    #keywords = "ssh"
    if (update):
        u = UpdateVersion()
        u.update() #Update from github
        return
    if(keywords):
        if fileText:
            argsParameters["fileText"] = fileText
        if fileHtml:
            argsParameters["fileHtml"] = fileHtml
        keywordsformated = str(keywords).split(",")
        if keywordsformated:
            argsParameters["keywordsformated"] = keywordsformated
            argsParameters["keywords"] = keywords
            execute(**argsParameters)
    else:
        basicInfo()
        return

def printHelpMessage():
     print """
Options:
  -h, --help                      show this help message and exit
  -s, --search <keyword,keyword,keyword>  text for search
  --txt                           Write txt File
  --html                          Write html File
  --update                        upgrade to latest version
              """

def basicInfo():
     print """
            Pompem - Exploit Finder  |  Developed by Relax Lab
              \n    Rafael Francischini (Programmer and Ethical Hacker) - @rfunix\n
    Bruno Fraga (Security Researcher) - @brunofraga_net\n
              Usage: pompem.py [-s/--search <keyword,keyword,keyword,...>]
                               [--txt Write txt file  ]
                               [--html Write html file]
      \n              Get basic options and Help, use: -h\--help
              """

if __name__ == "__main__":
    main()
