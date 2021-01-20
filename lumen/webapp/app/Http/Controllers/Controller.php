<?php

namespace App\Http\Controllers;

use Laravel\Lumen\Routing\Controller as BaseController;

class Controller extends BaseController
{
    static function payload(){
        $file_path = realpath(__DIR__ . '/../../../database/seeds/payload.json');
        $json = json_decode(file_get_contents($file_path), true);

        return $json;
    }
}
