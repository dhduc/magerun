#!/usr/bin/env python
import sys
import subprocess
import optparse
import string

class color:
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    # Color
    ORANGE = '\033[33m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    LIGHTGRAY = '\033[97m'
    BLACK = '\033[98m'

class Magegun :
    param = 0
    theme = ''
    sections = {}

    def init(self) :
        sections = [
            [
                'server', 
                [
                    [1, 'restart fpm service', 'sudo service php7.0-fpm restart', ''],
                    [2, 'restart apache server', 'sudo service apache2 restart', ''],
                    [3, 'restart nginx server', 'sudo service nginx restart', '']
                ]
            ],
            [
                'database',
                [
                    [4, 'enable module', 'php bin/magento module:enable', 'module'],
                    [5, 'disable module', 'php bin/magento disable:enable', 'module'],
                    [6, 'enable all module', 'php bin/magento module:enable --all --clear-static-content', ''],
                    [7, 'setup upgrade schema', 'php bin/magento setup:upgrade', ''],
                    [8, 'compile DI', 'php bin/magento setup:di:compile-multi-tenant', '']
                ]
            ],
            [
                'deploy',
                [
                    [9, 'remove generated files in var folder', 'rm -rf var/cache var/generation var/page_cache var/tmp var/view_preprocessed', ''],
                    [10, 'remove all static files', 'rm -rf pub/static', ''],
                    [11, 'deploy static content', 'php bin/magento setup:static-content:deploy', 'locale']
                ]
            ],
            [
                'grunt',
                [
                    [12, 'remove theme related static files', 'grunt clean:', 'theme'],
                    [13, 'republish theme related static files', 'grunt exec:', 'theme'],
                    [14, 'compile theme less files', 'grunt less:', 'theme']
                ]
            ],
            [
                'indexer and cache',
                [
                    [15, 'reindex data', 'php bin/magento indexer:reindex', ''],
                    [16, 'clear cache', 'php bin/magento cache:clean', ''],
                    [17, 'flush cache', 'php bin/magento cache:flush', '']
                ]
            ],
            [
                'custom',
                [
                    [18, 'custom command', 'php bin/magento', '']
                ],
            ]
        ]

        self.sections = sections

    def option(self) :
        parser = optparse.OptionParser()
        parser.add_option('-t', '--theme', dest='theme', help='Theme')
        (options, args) = parser.parse_args()
        if options.theme is None :
            self.theme = 'blank'
        else :    
            self.theme = options.theme    

    # Title
    def title(self) :
        print color.GREEN + 'Magento 2 Helper ' + color.LIGHTGRAY + 'version ' + color.YELLOW + '1.0.1' + color.ENDC
        print color.BLUE + '@author ducdh' + color.ENDC

    # Menu
    def menu(self) :
        sections = self.sections
        for section in sections :
            print color.YELLOW + section[0].capitalize() + ''
            for number, title, command, option in section[1] :
                print color.GREEN + '  ' + str(number).capitalize() + '. ' + title + color.ENDC 

    def getParam(self) :
        print color.RED
        param = raw_input('You chose: ')
        try :
            param = int(param)
            if (param < 0) or (param > 17) :
                print color.RED + 'Option not valid' + color.ENDC
                return 
        except ValueError:
            print color.RED + 'Option not valid' + color.ENDC 
           
        print color.ENDC
        self.param = param

    def run(self) :
        self.init()
        self.option()
        self.title()
        self.menu()
        self.getParam()
        self.execute()

    def execute(self) :
        param = self.param
        sections = self.sections
        for section in sections :
            area = section[0]
            for number, title, command, option in section[1] :   
                if param == number :
                    if option != '':
                        question = 'What '+ option +' you want to execute: '
                        _option = raw_input(question)
                        subprocess.call(command + ' ' + _option, shell=True)
                        print color.GREEN + title.capitalize() + ' for ' + _option + ' ' + option + ' successful'
                    else :
                        subprocess.call(command, shell=True)
                        print color.GREEN + title.capitalize() + ' successful'

magegun = Magegun() 
magegun.run()