<html>
<meta charset="gbk">
<head>
    <title>test </title> 
</head>
<body background="kd2.jpg" style=" background-repeat:no-repeat; background-size:100% 100%; background-attachment:fixed;">
<p> </p>
<form style="text-align:center" action="test.php" method="post">
    用户: <input type="text" id="yong" name="user" value="user"><br>
    密码: <input type="password" name="mima" value="Mouse"><br>

    <input type="submit" value="绑定" >
</form>
<p style="text-align:center">点击"提交"按钮，表单数据将被发送到服务器上的“test.php”。</p>
<?php
$a=$_GET['id']
?>
</body>
<script>
    function fun1() {
        var arr="<?php echo $a;?>";
        document.getElementById("yong").value=arr;
    }
</script>
<button onclick="fun1()"></button>
</html>
