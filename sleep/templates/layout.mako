<!DOCTYPE html>
<html>
<head>
	<title>sle_p</title>
	<link rel="stylesheet" href="/static/css/style.css">
	<link type="text/css" href="/static/css/jquery-ui-1.8.21.custom.css" rel="stylesheet" />
	<script type="text/javascript" src="/static/js/jquery-1.7.2.min.js"></script>
	<script type="text/javascript" src="/static/js/jquery-ui-1.8.21.custom.min.js"></script>
	<script type="text/javascript" src="/static/js/jquery.flot.min.js"></script>
	<script type="text/javascript" src="/static/js/jstat-1.0.0.min.js"></script>
</head>
<body>
<div id="page">
	<p><div id="title"><a href="${request.route_url('home')}">sle_p</a>, by <a href="http://dcc.nitrated.net/">dcchut</a></div>
	% if request.user:
		${request.user.username}.  <a href="${request.route_url('stats')}">global stats</a> - <a href="${request.route_url('pstats')}">personal stats</a> - <a href="${request.route_url('logout')}">logout</a>.
	% else:
		 <a href="${request.route_url('login')}">login</a> or <a href="${request.route_url('register')}">register</a>.
	% endif
	</p><hr />
% if request.session.peek_flash():
  <div id="flash">
    <% flash = request.session.pop_flash() %>
	% for message in flash:
	${message}<br>
	% endfor
  </div>
% endif
${next.body()}
</div>
</body>
</html>