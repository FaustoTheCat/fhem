open IN, "< i:/Leaf.log";

my $path = "";
my $Long = 0;
my $Lat = 0;


my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime();
$year+=1900;
$mon+=1;
my $today = sprintf("%04d-%02d-%02d",$year,$mon,$mday);

print"$today\n";
while (<IN>) {
	chomp;
	my $line = $_;
	my($Date,$tmp,$Key,$Value) = split(" ", $line);

	next if ($tmp ne "Leaf");
	($Date, $Time) = split("_", $Date);
	next if ($Date ne $today);

	if ($Key eq "Long:") {
		$Long = $Value;
	} elsif ($Key eq "Lat:")  {
		$Lat = $Value;	
	}
	if (($Long != 0) && ($Lat != 0)) {
		$path .= "|".$Lat.",".$Long if(length($path) < 1800 && ($Lat ne $oldlat || $Long ne $oldlon));
		$oldlat = $Lat;
		$oldlon = $Long;
		$Long = 0;
		$Lat = 0;								
	}
}
close IN;
print "https://maps.googleapis.com/maps/api/staticmap?language=en&size=620x480&scale=2&key=$googlekey&style=feature:poi|element:labels|visibility:off&style=feature:transit|element:labels|visibility:simplified|saturation:-80&maptype=roadmap$path";
#return "https://maps.googleapis.com/maps/api/staticmap?language=en&size=620x480&scale=2&key=$googlekey&style=feature:poi|element:labels|visibility:off&style=feature:transit|element:labels|visibility:simplified|saturation:-80&maptype=roadmap$path";
