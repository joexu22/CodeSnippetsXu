var f = 0;
var g = 1;
for (var i = 0; i <= 15; i++)
{
	console.log(f);
	f = f + g;
	g = f - g;
}