<html>
<body>
<h1>LOGIN</h1>
{{message}}<br/>
<form action="/login" method="post">
    <hr/>
    <table>
        <tr>
            <td><em>NAME</em></td>
            <td><input type="text",name="username"/><br/></td>
        </tr>
        <tr>
            <td><em>PASSWORD</em></td>
            <td><input type="password",name="password"/><br/></td>
        </tr>
    </table>
    <hr/>
    <input type="submit" value="Submit"/>
</form>
</body>
</html>
