<?php

$x=1;$primes[0]=2;

function primecandidate($var, $a){
//	echo 'prime candidate start' . '<br />' . '$var=' . $var . '<br />' . '$a=' . $a . '<br />';
	
	global $z, $primes;
	
	while($z<$a){
//	echo "while $z<$a <br /> $var % $primes[$z]:" . $var % $primes[$z] . "<br />";
		if($var % $primes[$z] != 0){
//			echo 'made it inside loop <br />';
			$z++;
			primecandidate($var, $a);
		}else{
//			echo 'failed out <br />';
			return false;
		}
	}
	
	return true;

}

for($y=3;$y<=1000;$y+=2){
//	echo '$y=' . $y . "<br />" . '$primes[$x-1]=' . $primes[$x-1] . "<br />" . '$y % $primes[$x-1]=' . $y % $primes	[$x-1] . "<br />";
	$z = 0;
	if(primecandidate($y, $x))
	{		
		$primes[$x] = $y;
		$x++;
		echo "Prime Found: $y" . "<br />";
	} else {
//		echo "Didn't find any <br />";
	}		
};

?>
