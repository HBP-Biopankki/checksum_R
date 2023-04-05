
Checksum_R <-function(my_str){

  magic_numbers <- c(7,3,1,7,3,1)

  palat  <- strsplit(my_str, "_")
  iterable = strsplit(palat[[1]][4], "")[[1]]
  
  
  master_list = list(rev(iterable), magic_numbers)
  master_list$mult = as.numeric(master_list[[1]]) * master_list[[2]]
  master_summa = sum(master_list$mult)
  
  return ((master_summa %/% 10 *10 +10) - master_summa)
}

Checksum_R('HBP_BB22_0027_323467')





