<?php 
session_start();
user_name = $_POST["user_name"]
$_SESSION[""] = user_name
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>login</title>
</head>
<body>
<form action="./confirm.cgi" method="post">
gender<input type="ratio" name="gender"><br>
nitizi<input type="date" name="nitizi"><br>
<input type="hidden" name="user_name" values="{form1}">
<input type="hidden" name="home_address" values="{form2}">
<input type="submit" name="submit" value="アカウント作成">
</form>
</body>
</html>