<!DOCTYPE html>
<html lang="en">
<head>

    <title>Magerun</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
    <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.6.0/styles/default.min.css">
    <style type="text/css">
        /* Sticky footer styles
-------------------------------------------------- */
html {
  position: relative;
  min-height: 100%;
}
body {
  /* Margin bottom by footer height */
  margin-bottom: 60px;
}
.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  /* Set the fixed height of the footer here */
  height: 60px;
  background-color: #f5f5f5;
}


/* Custom page CSS
-------------------------------------------------- */
/* Not required for template or sticky footer method. */

body > .container {
  padding: 60px 15px 0;
}
.container .text-muted {
  margin: 20px 0;
}

.footer > .container {
  padding-right: 15px;
  padding-left: 15px;
}

code {
  font-size: 80%;
}

    </style>
    <style type="text/css">
        .hljs, .hljs-subst {
            background: #123;
            color: #fff;
        }
    </style>
    </head>
    <?php ?>
    <?php 
        class Helper {
            static user;
            static pwd;
            static title;
            public function __construct() {
                $user = shell_exec('whoami');
                $pwd = shell_exec('pwd');
                $title = $user.'@'.$user.':'.$pwd;
                self::title = $title;
            }
        }
        class Magerun {
            public $param = 0;
            public $output = '';
            public $sections = array();
            public $theme = '';
            public $menu = '';

            public function __construct() {
                $this->init();
            }

            public function init() {
                $sections = array(
                        'common' => array(
                                array('current path', 'pwd', ''),
                                array('list all', 'ls -l', ''),
                                array('git status', 'git status', '')
                            ),
                        'indexer and cache' => array(
                                array('reindex data', 'php bin/magento indexer:reindex', ''),
                                array('clear cache', 'php bin/magento cache:clean', ''),
                                array('flush cache', 'php bin/magento cache:flush', '')
                            )
                    );

                $this->sections = $sections;
            }

            public function menu() {
                $sections = $this->sections;
                $menu = '';
                $number = 0;

                foreach ($sections as $section => $items) {
                    $menu .= '<h4>'.ucfirst($section).'</h4><hr>';
                    foreach ($items as $commands) {
                        $number++;
                        $menu .= '<a href="/?param='.$number.'" class="btn btn-primary">'.ucfirst($commands[0]).'</a>&nbsp;';
                    }
                    $menu .= '<br>';
                }

                echo $menu;
            }

            public function getParam() {
                $param = 0;
                if (isset($_GET['param'])) {
                    $param = $_GET['param'];
                }

                $this->param = $param;
            }

            public function run() {
                $sections = $this->sections;
                $number = 0;
                $param = $this->param;
                $output = '';
                foreach ($sections as $section => $items) {
                    foreach ($items as $commands) {
                        $number++;
                        if ($number == $param) {
                            $output = shell_exec($commands[1]);
                        }
                    }
                }

                $this->output = $output;
            }

            public function result() {
                $output = $this->output;
                echo $output;
            }

            public function input() {
                $this->menu();
            }

            public function output() {
                $this->getParam();
                $this->run();
                $this->result();
            }
        }
    ?>
  <body>

    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="" style="font-size: 3rem">Magerun</a>
        </div>
      </div>
    </nav>

    <!-- Begin page content -->
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <?php 
            $magerun = new Magerun();
            $magerun->input();
          ?>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <h4>Console</h4>

        <pre>
            <p>Terminal</p>
            <code class="bash">
              <?php
                $magerun->output();
              ?>
            </code>
        </pre>
        
      </div>
    </div>

    <footer class="footer">
      <div class="container">
        <p class="text-muted">Helper for Magento 2</p>
      </div>
    </footer>


<script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.6.0/highlight.min.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
</body>
</html>