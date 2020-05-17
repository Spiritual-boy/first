<?php
#echo("Congratulations!\n");
#$cmd = system("python zhenghe.py -u",$ret);

$output = system('python zhenghe.py');
#$array = explode(',', $output);
#echo '<script>window.location="index.html";document.getElementById("sousuokuang").value=$output;</script>';
#echo $output;
#$output=1;
#$str= "gj.php?id=1";
#$url=$str.$output;
#$message = "这是一个来自 php 的值。";
echo "<script language=\"JavaScript\" type=\"text/JavaScript\">;\r\n<!--\r\n alert('".$output."');\r\n-->;\r\n<!--\r\n window.location=\"index.php?id='$output'\";\r\n-->;\r\n</script>;";
#echo '<script>alert("hahah"+'.$str.');</script>';
#echo "<div id='value1' style=\"display: none;\">".$message."</div>";
#echo "<script language=\"JavaScript\" type=\"text / JavaScript\">;\r\n<!--\r\n window.location=\"gj.php?id=1\";r\n-->;</script>;";