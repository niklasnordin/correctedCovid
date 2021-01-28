

usa_min = 369327
usa_max = 569978
usa_reported = 354391

swe_min = 824
swe_max = 10642
swe_reported = 9771

usa_fraction = (usa_reported-usa_min)/(usa_max-usa_min)
swe_fraction = (swe_reported-swe_min)/(swe_max-swe_min)

usa_reported_like_swe = usa_min + swe_fraction*(usa_max-usa_min)
swe_reported_like_usa = swe_min + usa_fraction*(swe_max-swe_min)

print("Fraction: SWE = {}, USA = {}".format(swe_fraction, usa_fraction))

print("Reported dead")
print("USA {}. If USA reported like SWE {}".format(usa_reported, usa_reported_like_swe))
print("SWE {}. If SWE reported like USA {}".format(swe_reported, swe_reported_like_usa))

