

usa_min = 369327
usa_max = 569978
usa_reported = 354391

swe_min = 824
swe_max = 10642
swe_reported = 9771

ger_min = -21936
ger_max = 86133
ger_reported = 34194

fra_min = 26935
fra_max = 95878
fra_reported = 64780

usa_fraction = (usa_reported-usa_min)/(usa_max-usa_min)
swe_fraction = (swe_reported-swe_min)/(swe_max-swe_min)
ger_fraction = (ger_reported-ger_min)/(ger_max-ger_min)
fra_fraction = (fra_reported-fra_min)/(fra_max-fra_min)

usa_reported_like_swe = usa_min + swe_fraction*(usa_max-usa_min)
swe_reported_like_usa = swe_min + usa_fraction*(swe_max-swe_min)

swe_reported_like_ger = swe_min + ger_fraction*(swe_max-swe_min)
ger_reported_like_swe = ger_min + swe_fraction*(ger_max-ger_min)

#print("Fraction: SWE = {}, USA = {}".format(swe_fraction, usa_fraction))

print("Reported dead")
print("USA {}. If USA reported like SWE {}".format(usa_reported, usa_reported_like_swe))
print("SWE {}. If SWE reported like USA {}".format(swe_reported, swe_reported_like_usa))

print("SWE {}. If SWE reported like GER {}".format(swe_reported, swe_reported_like_ger))
print("GER {}. If GER reported like SWE {}".format(ger_reported, ger_reported_like_swe))
