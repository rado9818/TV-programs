<?php
/**
 * Created by PhpStorm.
 * User: radoslav
 * Date: 18.12.18
 * Time: 17:08
 */

namespace App\Controllers;


use App\Models\Version;
use Dotenv\Dotenv;
use Psr\Container\ContainerInterface;

class ProgramsController
{
    private $c;


    /**
     * Tasks constructor.
     *
     * @param ContainerInterface $container
     */
    public function __construct(ContainerInterface $container)
    {
        $this->c = $container;
    }

    public function index($request, $response, $args)
    {
        $db = $this->c->get('db');
        $programs = $db::table('programs')->get();


        return $response->withJson($programs);
    }

    public function store($request, $response, $args)
    {
        $db = $this->c->get('db');

        $db::table('programs')->truncate();

        $data = $request->getParsedBody();

        $programs = json_decode(file_get_contents('php://input'), true);
        //dd($programs);

        foreach ($programs as $program) {
            $db::table('programs')->insert(
                [
                    'name' => $program["name"],
                    'start_time' => $program["start_time"]
                ]

            );
        }

        return $response->withJson($programs);
    }


}