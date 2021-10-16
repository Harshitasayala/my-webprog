<html>
<body>
%if extra != None: 
    <h2> Helloo {{name}}, {{extra}}!!</h2>
%else:
    <h2> Helloo {{name.upper()}}!!</h2>
    <h2> Helloo {{name[::-1]}}!!</h2>
%end
<br>
...from the template!!
</body>
</html>
