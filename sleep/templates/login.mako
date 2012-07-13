<%inherit file="layout.mako"/>

<p class="title">login</p>

<form action="${request.route_url('login')}" method="POST">
	<div class="frow">
		<div class="fleft">username / email address:</div>
		<div class="fright"><input type="text" name="login"></div>
	</div>
	<div class="frow">
	    <div class="fleft">password:</div>
	    <div class="fright"><input type="password" name="password"></div>
	</div>
	<div class="frow">
	    <div class="fleft">&nbsp;</div>
	    <div class="fright"><input type="submit" value="login"></div>
	</div>
</form>