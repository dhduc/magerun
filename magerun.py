#!/usr/bin/env python
import sys
import subprocess
import optparse
import string
import os
from datetime import datetime

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

class Magerun :
    param = 0
    theme = ''
    sections = {}
    folder = ''
    pwd = ''

    def init(self) :
        sections = [
            [
                'server', 
                [
                    ['restart fpm service', 'sudo service php7.0-fpm restart', ''],
                    ['restart apache server', 'sudo service apache2 restart', ''],
                    ['restart nginx server', 'sudo service nginx restart', '']
                ]
            ],
            [
                'git', 
                [
                    ['git pull', 'git pull', ''],
                    ['git status', 'git status', ''],
                    ['git difference', 'git diff', ''],
                    ['git reset stash', 'git checkout -- .', ''],
                    ['git add all', 'git add -A .', ''],
                    ['git commit', 'git commit', ''],
                    ['git show last commit', 'git show', ''],
                    ['git push', 'git push', '']
                ]
            ],
            [
                'database',
                [
                    ['enable module', 'php bin/magento module:enable', 'module'],
                    ['disable module', 'php bin/magento disable:enable', 'module'],
                    ['enable all module', 'php bin/magento module:enable --all --clear-static-content', ''],
                    ['setup upgrade schema', 'php bin/magento setup:upgrade', ''],
                    ['compile DI', 'php bin/magento setup:di:compile-multi-tenant', '']
                ]
            ],
            [
                'deploy',
                [
                    ['remove generated files in var folder', 'rm -rf var/cache var/generation var/page_cache var/tmp var/view_preprocessed', ''],
                    ['remove all static files', 'rm -rf pub/static', ''],
                    ['deploy static content', 'php bin/magento setup:static-content:deploy', 'locale']
                ]
            ],
            [
                'grunt',
                [
                    ['remove theme related static files', 'grunt clean:', 'theme'],
                    ['republish theme related static files', 'grunt exec:', 'theme'],
                    ['compile theme less files', 'grunt less:', 'theme']
                ]
            ],
            [
                'indexer and cache',
                [
                    ['reindex data', 'php bin/magento indexer:reindex', ''],
                    ['clear cache', 'php bin/magento cache:clean', ''],
                    ['flush cache', 'php bin/magento cache:flush', '']
                ]
            ],
            [
                'custom',
                [
                    ['custom command', 'php bin/magento', 'custom command']
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
        number = 0
        for section in sections :
            print color.YELLOW + section[0].capitalize() + ''
            for title, command, option in section[1] :
            	number = number + 1
                print color.GREEN + '  ' + str(number).capitalize() + '. ' + title + color.ENDC 
        
        # Close program
        print color.YELLOW + 'Close' + color.ENDC
        print color.RED + '  ' +'0. Close program' + color.ENDC

    def setFolder(self) :
        folder = raw_input('The folder of project')
        self.folder = folder

    def getFolder(self) :
        pwd = os.getCwd()
        self.pwd = pwd        

    def setParam(self) :
        print color.RED
        param = raw_input('You chose: ')
        try :
            param = int(param)
        except ValueError:
            print color.RED + 'Option not valid' + color.ENDC 
           
        print color.ENDC
        self.param = param

    def run(self) :
        self.init()
        self.option()
        self.loop()

    def loop(self) :
        self.title()
        self.menu()
        self.setParam()
        param = self.param
        if param != 0 :
        	self.execute()
        	self.loop()
        else :
        	print color.GREEN + 'Close program' + color.ENDC	   

    def execute(self) :
        param = self.param
        sections = self.sections
        now = datetime.now()
        number = 0
        for section in sections :
            area = section[0]
            for title, command, option in section[1] : 
            	number = number + 1  
                if param == number :
                    if option != '':
                        question = 'What '+ option +' you want to execute: '
                        _option = raw_input(question)
                        subprocess.call(command + ' ' + _option, shell=True)
                        print color.GREEN + title.capitalize() + ' for ' + _option + ' ' + option + ' successful' + color.BLUE + ' at %s:%s' % (now.hour, now.minute) + '\n'
                    else :
                        subprocess.call(command, shell=True)
                        print color.GREEN + title.capitalize() + ' successful' + color.BLUE + ' at %s:%s' % (now.hour, now.minute) + '\n'

magegun = Magerun()
magegun.run()