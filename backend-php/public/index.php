<?php

// initialize autoloader
require '../vendor/autoload.php';


// make application instance with the settings
$app = new \Slim\App(["settings" => include '../config/settings.php']);

// load the services
include '../dependencies.php';

// load the routing map
include '../routing.php';

// run the application
$app->run();

