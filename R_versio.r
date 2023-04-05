
Checksum_R <-function(my_str){

  roundUp  <- function(x){round(x+5,-1)}


  magic_numbers <- c(7,3,1,7,3,1)

  palat  <- strsplit(my_str, "_")
  iterable = strsplit(palat[[1]][4], "")[[1]]
  
  
  master_list = list(iterable, magic_numbers)
  master_list$mult = as.numeric(master_list[[1]]) * master_list[[2]]
  master_summa = sum(master_list$mult)
  
  return (roundUp(master_summa) - master_summa)
}

Checksum_R('HBP_BB22_0027_323467')





