<%inherit file="layout.mako"/>

<p class="title">${title}</p>

<p>average sleep duration: ${avg_sleep_duration} hours</p>
<p>average sleep quality: ${avg_sleep_quality}</p>
<p>histogram of sleep times:<br />
<div id="s1" style="width:600px;height:300px;"></div><br />
</p>
<p>histogram of wakeup times:<br />
<div id="s2" style="width:600px;height:300px;"></div><br />
</p>
<script type="text/javascript">
$(function(){
    var d1 = [];
    var d1m = 0.75*${s1_stats[2]}/jstat.dnorm(${s1_stats[0]},${s1_stats[0]},${s1_stats[1]});
    var d2 = [];
    var d2m = 0.75*${s2_stats[2]}/jstat.dnorm(${s2_stats[0]},${s2_stats[0]},${s2_stats[1]});
    
    for (var i = 0; i < 24; i+= 0.25) {
      d1.push([i,d1m*jstat.dnorm(i,${s1_stats[0]},${s1_stats[1]})]);
      d2.push([i,d2m*jstat.dnorm(i,${s2_stats[0]},${s2_stats[1]})]);
    }
    
    var xt1 = [];
    i = 0;
    while (i < 24) {
      xt1.push([i,((i+13)%24).toString()]);
      i++;
    }
    
    $.plot($("#s1"),[
        {
            data: ${s1_data},
            bars: { show: true }
        },
        {
          data: d1,
          lines: {show: true}
        }
    ], {
        xaxis: { ticks: xt1 }
    });
    $.plot($("#s2"),[
        {
            data: ${s2_data},
            bars: { show: true },
        },
        {
            data: d2,
            lines: {show: true}
        }
    ], {
        xaxis: { ticks: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] }
        
    });
});
</script>