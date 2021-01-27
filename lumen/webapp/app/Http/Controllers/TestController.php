<?php

namespace App\Http\Controllers;

use App\Test;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;

class TestController extends Controller
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

    public function test(Request $req){
        // ini adalah variable payload sesuai sesuai soal yang di bubuhkan
        $payload = $this->payload();
        // $payload = $req->all();
        $date = Date('Y-m-d');

        try {
            $sql = (array('text' => 'simpen data nanti di variable $sql ini ya,, hapus aja text array nya'));

            $response = response()->json(array('code' => 200, 'message' => 'Successfully Created', 'data' => $sql), 200);
        } catch (\Throwable $th) {
            $response = response()->json(array('code' => 500, 'message' => 'Error'), 500);
        }

        return $response;
    }
}
