function fade()
{
	animate("line1",1, "fadeInUp");
	animate("line2",3, "fadeInUp");
	animate("line3",3, "fadeInUp");
	animate("line4",5, "fadeInUp");
	animate("line5",7, "fadeInUp");
	animate("line6",9, "fadeInUp");
	animate("line7",11, "fadeInUp");
	animate("tabs",13, "fadeInUp");
}
function animate(id , time, type)
{
	setTimeout(
		function ()
		{
			document.getElementById(id).style.display = "inherit";
			document.getElementById(id).className = "animated "+type;

		},time*500);
}
