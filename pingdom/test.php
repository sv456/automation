<html>
<head>
<title>Uptime Reporter</title>

<script>
function clearBox(tb)
{
    document.getElementById(tb).innerHTML = "";
} 
</script>
<script src="charts4php-free-latest/lib/js/jquery.min.js"></script> 
        <script src="charts4php-free-latest/lib/js/chartphp.js"></script> 
        <link rel="stylesheet" href="charts4php-free-latest/lib/js/chartphp.css"> 
<style>
html { 
  background: url(https://media.glassdoor.com/l/53/72/fc/05/new-successfactors-sap-signs.jpg) no-repeat center center fixed; 
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}


#load{
position:absolute;
z-index:1;
width:300px;
height:300px;
margin-top:-150px;
margin-left:-270px;
top:50%;
left:50%;
text-align:center;
line-height:300px;
}

select {
    width: 100%;
    padding: 16px 20px;
    border: none;
    border-radius: 4px;
    background-color: silver;
	font-size: 24px;
	box-shadow: 0 5px black;
	
	
}

input[type=date] {
  height=25px;
  width:100%
  margin: 0 auto; 
  font-family: arial, sans-serif;
  font-size: 24px;
  text-transform: uppercase;
  background-color: silver;
  outline: none;
  border: 0;
  border-radius: 4px;
  padding: 12px 20px;
  box-shadow: 0 5px black;
 
}
option{
	font-size: 24px;
	
}

.output th,.output td,.header td{
	border:2px solid black;
	padding: 8px;
	font-size: 24px;
}

.button {
  display: inline-block;
  padding: 15px 25px;
  font-size: 24px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  
  background-color: silver;
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px black;
}

.button:hover {background-color: #3e8e41}

.button:active {
  background-color: #3e8e41;
  box-shadow: 0 5px black;
  transform: translateY(4px);
}

</style>
<script language="javascript" type="text/javascript">
    var mealsByCategory = {
	ABC: ["Select","ALL","DC02","DC04","DC08","DC10","DC12","DC17","DC18","DC19"],
	BCD:["Select","ALL","DC02","DC04","DC08","DC10","DC12","DC17","DC18","DC19"],
	CDE:["Select","ALL","DC02","DC04","DC08","DC10","DC12","DC17","DC18","DC19"],
    DEF:["Select","ALL","DC12","DC17"],
    EFG: ["Select","ALL","DC12", "RackSpace", "DC17", "DC19"],
	FGH: ["Select","ALL","DC02","DC04","DC08","DC10","DC12","DC16","DC17","DC18","DC19"],
	GHI: ["Select","ALL","DC02","DC04","DC08","DC10","DC12","DC12B","DC171","DC17","DC18","DC19"],
}

    function changecat(value) {
        if (value.length == 0) document.getElementById("dc").innerHTML = "<option></option>" ;
        else {
            var catOptions = "";
            for (categoryId in mealsByCategory[value]) {
                catOptions += "<option>" + mealsByCategory[value][categoryId] + "</option>";
            }
            document.getElementById("dc").innerHTML = catOptions;
        }
    }
	
	
	var environment = {
	ABC: ["Select","Prod","Preview","Sales","BOSCH"],
	BCD:["Select","Prod","Sales"],
	CDE:["Select","Prod","Preview","Sales","Stage"],
    DEF:["Select","Prod"],
	EFG:["Select","Prod","Stage"],
	FGH: ["Select","Prod","Preview","Sales"],
	GHI: ["Select","Prod","Preview","Sales"],
}

    function changeenv(value) {
        if (value.length == 0) document.getElementById("env").innerHTML = "<option></option>" ;
        else {
            var envOptions = "";
            for (categoryId in environment[value]) {
                envOptions += "<option>" + environment[value][categoryId] + "</option>";
            }
            document.getElementById("env").innerHTML = envOptions;
        }
    }
    </script>
</head>

<body  onload='sortTable(0);'>
<Center><h1 style="color:orange"><b>SAP SDO Service Availability Report</b></h1></Center>
<div id=form align="center">
<div id="load" style="display:none;"><center><img src="http://4.bp.blogspot.com/-tjMYWRYVIvg/UrCQf3JDpTI/AAAAAAAAGNI/g8IbqLIPBtY/s1600/loadingeffect2.png"></center></div>
<form id=Inputs action="" method="POST" onsubmit="return ray.ajax()">
<center><table>
<td align="left" width=200px> <b>Select The Product:</b> 
  <select name="product" id="product" onChange="changecat(this.value);changeenv(this.value);">
    <option value="" disabled selected>Select</option>
	<option value="ABC">ABC</option>
	<option value="BCD">BCD</option>
	<option value="CDE">CDE</option>
    <option value="DEF">DEF</option>
    <option value="EFG">EFG</option>
	<option value="FGH">FGH</option>
	<option value="GHI">GHI</option>
</select></td>
<td width=200px> <b>Select Data Center:</b> 
  <select name="dc" id="dc">
    <option value="" disabled selected>Select</option>
</select></td>
<td width=200px> <b>Select Environment:</b> 
  <select name="env" id="env"><option value='NO' selected disabled>Select</option>
</select></td>
<td width=200px> <b>Select Start Date:</b>
<input type="date" name="start_date" id="start_date">
</td>

<td width=200px><b>Select End Date:</b>
<input type="date" name="end_date" id="end_date"></td></tr></table></center><br>
<div align="center"><input type="submit" class="button" value="Submit" name="submit" onclick="clearBox('tb'); clearBox('tb1');">&nbsp;&nbsp;&nbsp;<input type="reset" class="button" value="Reset" name="reset" onclick="clearBox('tb'); clearBox('tb1');"></div>

</form></div>
<center>
<?php 
$k=array();
$v=array();
if(isset($_POST["submit"]))
{
	$var1=$_POST["product"];
	if($var1=="")
	{
		echo "<script>";
		echo "alert('Please enter product')";
		echo "</script>";
		echo "";
		goto en;
	}
	$var2=$_POST["start_date"];
	if($var2=="")
	{
		echo "<script>";
		echo "alert('Please enter start date')";
		echo "</script>";
		goto en;
	}
	$var3 = $_POST["end_date"];
	if($var3=="")
	{
		echo "<script>";
		echo "alert('Please enter end date')";
		echo "</script>";
		goto en;
	}
	$var4=$_POST["dc"];
	if($var4=="" or $var4=="Select")
	{
		echo "<script>";
		echo "alert('Please enter DC')";
		echo "</script>";
		goto en;
	}
	$var5=$_POST["env"];
	if($var5=="" or $var5=="Select")
	{
		echo "<script>";
		echo "alert('Please enter environment')";
		echo "</script>";
		goto en;
	}
	$var="";
	
	if ($var1=="" or $var2=="" or $var3=="" or $var4=="" or $var4=="Select" or $var5=="Select")
	{
		
		echo "<b style='color:#20CD9F;text-shadow: 1px 0 0 #000, 0 -1px 0 #000, 0 1px 0 #000, -1px 0 0 #000;'>","Please check the values entered","</b>";
		die();
		
	}
	else
	{
		$var=shell_exec("python outtest.py $var1 $var2 $var3 $var4 $var5");
		if((strlen($var))==8){
			echo "<b style='color:#20CD9F;text-shadow: 1px 0 0 #000, 0 -1px 0 #000, 0 1px 0 #000, -1px 0 0 #000;'>","Please check the selected DC or Environment</b>";
			die();
		}
    $vari = json_decode($var,true);
	if(empty($vari['data']))
	{
		echo "<b id='al' style='color:#20CD9F;text-shadow: 1px 0 0 #000, 0 -1px 0 #000, 0 1px 0 #000, -1px 0 0 #000;'>",$var5," is not in ",$var4," for ",$var1,"</b>";
		die();
	}
	$vars=$vari['data'];
	$varx=$vari['xl_name'];
	echo "<div name='tb' id='tb'>";
	echo "<table class='header' style='border:2px solid black;background:silver;border-collapse: collapse;'>","<caption style='font-size:27px'><b style='color:#20CD9F;text-shadow: 1px 0 0 #000, 0 -1px 0 #000, 0 1px 0 #000, -1px 0 0 #000;'>",$var1," Availability Report</b> </caption>" ,"<tr><td>From : " , $var2 ,"</td>" ,"<td>   To : " , $var3 , "</td></tr></table>";
	echo "<table id='myTable' class='output' style='border:2px solid black;background:silver;border-collapse: collapse;'>" ,"<tr>","<th><b>Check Name</b></th>" , "<th><b>Availablity</b>" , "</th></tr>";
	foreach( $vars as $key => $value){
		echo "<tr>", "<td>" , "$key" , "</td>" , "<td>" . "$value" , "</td>" , "</tr>";
		array_push($k,$key);
		array_push($v,(float)$value);
	}
	echo "</table>";
	}
	echo "</div>";
	en:
}

	
?></center>
<script type="text/javascript">
document.getElementById('product').value = "<?php echo $_POST['product'];?>";
  changecat('<?php echo $_POST['product']?>');
  changeenv('<?php echo $_POST['product']?>')
  document.getElementById('dc').value = "<?php echo $_POST['dc'];?>";
  document.getElementById('env').value = "<?php echo $_POST['env'];?>";
  document.getElementById('start_date').value = "<?php echo $_POST['start_date'];?>";
  document.getElementById('end_date').value = "<?php echo $_POST['end_date'];?>";
</script>
<br>
<center><a href="<?php echo $varx ?>"><input type="submit" class="button"  value="Export to Excel"></a>&nbsp;&nbsp;<input type="submit" class="button" onclick="chart();" value="Show on Graph"><br>
</center>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="http://cdn.jsdelivr.net/webshim/1.12.4/extras/modernizr-custom.js"></script>
<script src="http://cdn.jsdelivr.net/webshim/1.12.4/polyfiller.js"></script>
<script>
  webshims.setOptions('waitReady', false);
  webshims.setOptions('forms-ext', {type: 'date'});
  webshims.setOptions('forms-ext', {type: 'time'});
  webshims.polyfill('forms forms-ext');
</script>
<script>
function clearBox(elementID)
{
    document.getElementById(elementID).innerHTML = "";
}
</script>
<script type="text/javascript">
var ray={
ajax:function(st)
	{
		this.show('load');
	},
show:function(el)
	{
		this.getID(el).style.display='';
	},
getID:function(el)
	{
		return document.getElementById(el);
	}
}
</script>
<script>
function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("myTable");
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc"; 
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.getElementsByTagName("TR");
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++; 
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.bundle.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.bundle.min.js"</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
<script src="Chart.js"></script>
<script>
    var myChart = new Chart({...})
</script>

<script>
var ks=<?php echo json_encode($k );?>;
var vs=<?php echo json_encode($v );?>;
var vr=[];
var vrr=[]
for(i=0;i<ks.length;i++){
	vr.push("#0000FF");
	vrr.push("black");
}
wid=vr.length
    

function chart(){
	$('#myChart').css('background-color','#ADD8E6')
	$('#myChart').css('height','650');
	if (wid <5){
        $('#myChart').css('width','420');
		
    } else if (wid>10) {
        $('#myChart').css('width','1400');
    }
	else{
		$('#myChart').css('width','700');
	}
var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ks,
        datasets: [{
			label: "Percentage",
            data: vs,
			backgroundColor: vr,
            borderColor: vrr,
        }]
    },
	options:	
	{
		title: {
            display: true,
            text: 'Availability',
			fontSize:22,
			fontFamily:'Bookman'
        },
		responsive: false,
        maintainAspectRatio: false,
		scales: {
        xAxes: [{
            barPercentage: 1.0,
			categoryPercentage: 0.9,
			ticks: {
					fontSize:17,
					fontColor:"black",
					autoSkip: false,
					maxRotation: 90,
					minRotation: 90,
      }
			
			
        }],
		yAxes: [{
            display: true,
            ticks: {
				fontSize:17,
				fontColor: "#FF8C00",
                stepSize: 0.1,
                suggestedMin: 99.00,
            }
        }]
    }
    },
	
});
}
</script>
<br><br>
<center><div id="tb1">
 <canvas id="myChart" >
 </canvas></div></center>
</body>
</html>
