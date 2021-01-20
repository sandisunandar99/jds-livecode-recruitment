<?php

namespace App\Http\Controllers;

use App\Test;
use Illuminate\Support\Facades\DB;

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

    public function test(){
        // ini adalah variable payload sesuai sesuai soal yang di bubuhkan
        $payload = $this->payload();
        $date = Date('Y-m-d');

        try {
            Test::create([
                'nama' => $payload['nama'],
                'nik' => $payload['nik'],
                'no_tlp' => $payload['no_tlp'],
                'email' => $payload['email'],
                'alamat' => $payload['alamat'],
                'tgl_lahir' => $date,
                'kode_karyawan' => 'JDS21212121212121'
            ]);


            $response = response()->json(array('status' => true, 'msg' => 'Successfully Created'), 200);

        } catch (\Throwable $th) {
            $response = response()->json(array('message' => 'Error'), 500);
        }

        return $response;
    }
}
