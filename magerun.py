#!/usr/bin/env python
import sys
import subprocess
import optparse

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
    commands = {}

    def init(self) :
        commands = {
            '1. Restart FPM',
            '2. Restart Apache',
            '3. Restart Nginx',
        }
        self.commands = commands

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
        commands = self.commands
        for command in commands :
            print color.GREEN + command

    def getParam(self) :
        print color.RED
        param = int(raw_input('You chose: '))
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
        # commands = self.commands
        # keys = commands.keys()
        # values = commands.values()
        if param == 1 :
            self.clearCache()
        elif param == 2 :
            self.flushCache()
        else :
            print color.RED + 'Not valid'

    def restartFpm():
        command = 'sudo service php7.0-fpm restart'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Restart FPM service successful' 

    def restartApache():
        command = 'sudo service apache2 restart'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Restart apache server successful'            

    def restartNginx():
        command = 'sudo service nginx restart'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Restart nginx server successful'

    def reindexData(self) :
        command = 'php bin/magento indexer:reindex'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Reindex data successful'
                
    def clearCache(self) :
        command = 'php bin/magento cache:clean'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Clear cache successful'

    def flushCache(self) :
        command = 'php bin/magento cache:flush'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Flush cache successful'

    def removeVar() :
        command = 'rm -rf var/cache var/page_cache var/generation var/view_preprocessed'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Remove var files successful'

    def removeStatic() :
        theme = raw_input('Theme : ')
        command = 'grunt clean:' + theme
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Clean static files successful'

    def republishStatic() :
        theme = raw_input('Theme : ')
        command = 'grunt exec:' + theme
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Republish static files successful'

    def compileLess() :
        theme = raw_input('Theme : ')
        command = 'grunt less:' + theme
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Compile less files successful'

    def enableModule():
        command = 'php bin/magento module:enable --all --clear-static-content'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Flush cache successful'                                            

    def setupUpgrade():
        command = 'php bin/magento setup:upgrade'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Flush cache successful'
    
    def setupContent():
        command = 'php bin/magento kingliving:setup'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Flush cache successful'

    def compileDI():
        command = 'php bin/magento setup:di:compile-multi-tenant'
        subprocess.call(command, shell=True)
        print color.GREEN
        print 'Flush cache successful'
        
    def deployContent():
        locale = raw_input('Locale: ')
        command = 'php bin/magento setup:static-content:deploy' + locale
        subprocess.call('php bin/magento cache:flush', shell=True)
        print color.GREEN
        print 'Flush cache successful'                

magegun = Magegun() 
magegun.run()