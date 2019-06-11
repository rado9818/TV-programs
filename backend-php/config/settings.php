<?php

// return the configuration
return array(

    // general slim config
    'displayErrorDetails' => true,
    'addContentLengthHeader' => false,

    // database specific config
    'db' => array(
        'driver' => 'mysql',
        'host' => 'localhost',
        'database' => '',
        'username' => '',
        'password' => '',
        'charset'   => 'utf8mb4',
        'collation' => 'utf8mb4_general_ci',
        'prefix'    => '')


);
