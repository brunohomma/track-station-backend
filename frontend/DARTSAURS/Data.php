<html>
<body>
<?php
// 5 seconds


$url = file_get_contents('http://10.0.0.106:8000/api/tracks/track');

header("refresh: 10");
    
echo date('H:i:s Y-m-d');
echo "<BR><BR>";


$pos  = strripos($url, '"latitude":');
$pos1 = strripos($url, ',"longitude":');
$pos11 = strripos($url,',"altitude":');
$pos2 = $pos1-$pos;

$latx1 = substr($url, $pos+11,$pos1-11-$pos); 
echo $latx1*1;
echo "<BR><BR>";

$lonx1 = substr($url, $pos1+13,$pos11-13-$pos1); 
echo $lonx1*1;
echo "<BR><BR>"; 

echo $url;
echo "<BR><BR>"; 
 
//{"name":"iss","id":25544,"latitude":-8.3766720509585,"longitude":-113.05831770981,"altitude":419.50179579962,"velocity":27577.341295747,"visibility":"daylight","footprint":4504.9279522623,"timestamp":1664730918,"daynum":2459855.2189583,"solar_lat":-3.7637293081903,"solar_lon":278.49676521018,"units":"kilometers"} 
 

?>

<script>
var x = <?php echo $latx1; ?>;
var y = <?php echo $lonx1; ?>;
	parent.teste(x,y);
</script>

</body>
</html>