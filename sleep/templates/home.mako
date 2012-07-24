<%inherit file="layout.mako"/>

% if request.user:
	<script type="text/javascript">
		$(function(){
			// Datepicker
			$('#start_date').datepicker({
				dateFormat: 'dd/mm/yy'
			});
			
			// shade the alternate rows
			$(".shade:even").addClass("alt");
			// change colour on hover
			$(".shade").mouseover(function(){$(this).addClass("over");}).mouseout(function(){$(this).removeClass("over");});
			
		});
	</script>
	<p class="title">insert a new sleep record:</p>
	<p>
	note: if you went to sleep at 11:35pm on 10/06/2012, then write 10/06/2012 under start date.<br />
	if you went to sleep at 3:00am on 11/06/2012, then write 11/06/2012 under start date.
		<form action="${request.route_url('home')}" method="POST">
		<div class="frow">
		    <div class="fleft"><a title="this is the date of the time you went to sleep">start date (dd/mm/yyyy)</a>:</div>
		    <div class="fright"><input name="start_date" id="start_date" type="text"></div>
		</div>
		<div class="frow">
		    <div class="fleft">start time:</div>
		    <div class="fright"><select name="start_time">
		    % for hr in [12] + range(1,12):
		    	% for mn in range(0,60,10):
		    		<option value="${hr},${mn}">${str(hr).zfill(2)}:${str(mn).zfill(2)}</option>
	    		% endfor
    		% endfor
		    </select>
		    <select name="start_ampm">
			    <option value="am">AM</option>
			    <option value="pm" selected>PM</option>
		    </select>
		    </div>
		</div>
		<div class="frow">
		    <div class="fleft">end time:</div>
		    <div class="fright"><select name="end_time">
		    % for hr in [12] + range(1,12):
		    	% for mn in range(0,60,10):
		    		<option value="${hr},${mn}">${str(hr).zfill(2)}:${str(mn).zfill(2)}</option>
	    		% endfor
    		% endfor
		    </select>
		    <select name="end_ampm">
			    <option value="am" selected>AM</option>
			    <option value="pm">PM</option>
		    </select>
		    </div>
		</div>
		<div class="frow">
		    <div class="fleft">quality (higher is better)</div>
		    <div class="fright"><select name="quality">
		% for i in range(-5,6):
		    <option value="${i}"
		    % if i == 0:
		    	selected
	    	% endif
	    	>${i}</option>
		% endfor
		</select>
		</div>
		</div>
		<div class="frow">
		    <div class="fleft">&nbsp;</div>
		    <div class="fright"><input type="submit" value="insert"></div>
		</div>
	</p>
    <p class="title">your sleep records:</p>
	<p>
	% if records:
		<div class="grow ghead">
		    <div class="gc gc0">date:</div>
		    <div class="gc gc1">start time:</div>
		    <div class="gc gc1">end time:</div>
		    <div class="gc gc2">quality:</div>
		    <div class="gc gc1">duration:</div>
		    <div class="gc gc2">actions:</div>
		</div>
		% for r in records:
			<div class="grow shade">
				<div class="gc gc0">${r['date']}</div>
				<div class="gc gc1">${r['start']}</div>
				<div class="gc gc1">${r['end']}</div>
				<div class="gc gc2">${r['quality']}</div>
				<div class="gc gc1">${r['duration']} hours</div>
				<div class="gc gc2"><a href="${request.route_url('delete',id=r['id'])}">delete</a></div>
			</div>
		% endfor
	% else:
		none
	% endif	
	</p>
% else:
	<p>This is <b>sle_p</b>, another useless website with negligible social benefit. Hopefully we'll get some nice statistics out of this, and maybe even some nice
	bar plots as well.</p>
% endif