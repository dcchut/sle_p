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
<div class="frow">
    <div class="fleft">&nbsp;</div>
    <div class="fright"><input type="submit" value="register"></div>
</div>
</form>