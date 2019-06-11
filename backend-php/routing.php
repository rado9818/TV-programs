<?php
use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

/* @var $app \Slim\App */

//Calls endpoints will go here

$app->get('/programs/{id}', \App\Controllers\ProgramsController::class . ':index');
$app->post('/programs/{id}', \App\Controllers\ProgramsController::class . ':store');
