<?php

$x=1;
$primes[0]=2;

for($y=3;$y<=600851475143;$y+2){

	if($y % $primes[$x-1] != 0){
		$primes[$x] = $val;
		$x++;
		print_r($y);
	}
}

?>
