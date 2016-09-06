
#!/bin/sh

echo "<br><font color ="red">SyntaxErr myList.sh Script Results: </font> </br>" > myList_SyntaxErr.html

for i in *
 do 
   echo "<br>$i<br/>" >> myList_SyntaxErr.html
done

xdg-open myList_SyntaxErr.html
