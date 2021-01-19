<?php

namespace App\Http\Controllers;

class Test1Controller extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        //
    }

    public function test1(){
        // $file = realpath(__DIR__ . '/../../database/seed/payload.json');
        // $json = json_decode(file_get_contents($file_path), true);

        return response()->json(['name' => 'Abigail', 'state' => 'CA']);
    }
}
