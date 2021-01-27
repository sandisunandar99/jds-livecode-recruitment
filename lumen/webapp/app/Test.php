<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Test extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */

    protected $fillable = [
        'nama',
        'nik',
        'no_tlp',
        'email',
        'alamat',
        'tgl_lahir',
        'kode_karyawan'
    ];
}
