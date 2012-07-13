<%inherit file="layout.mako"/>

<p class="title">register</p>

<form action="${request.route_url('register')}" method="POST">
<div class="frow">
    <div class="fleft">username:</div>
    <div class="fright"><input type="text" name="username" value="${username}"></div>
</div>
<div class="frow">
    <div class="fleft">password:</div>
    <div class="fright"><input type="password" name="password"></div>
</div>
<div class="frow">
    <div class="fleft">confirm password:</div>
    <div class="fright"><input type="password" name="cpassword"></div>
</div>
<div class="frow">
    <div class="fleft">email:</div>
    <div class="fright"><input type="text" name="email" value="${email}"></div>
</div>
<p style="width:500px;">
by registering for sle_p you agree that sle_p can use your submitted
data for statistical purposes. sle_p will always present user submitted
data in an anonymous manner</p>
<!-- 
god I have no idea about writing disclaimers,
but the spirit is there
-->
<div class="frow">
    <div class="fleft">&nbsp;</div>
    <div class="fright"><input type="submit" value="register"></div>
</div>
</form>