# checksum_R

checksum_R('HBP_BB22_0027_323467', 'luo')
#'HBP_BB22_0027_323467_7' 
checksum_R('HBP_BB22_0027_323467_2', 'tarkista')
#False
checksum_R('HBP_BB22_0027_000000', 'luo')
#Biopankki ja tunnise eivat tasmaa ('HBP', '0') pitaisi olla 3

checksum_R('HBP_BB22_0027_000000', 'tarkista')
#Pituus vaarin pseudossa HBP_BB22_0027_000000
checksum_R('HBP_BB22_0027_300000_0', 'tarkista')
#False
checksum_R('HBP_BB22_0027_300000_9', 'tarkista')
#True
