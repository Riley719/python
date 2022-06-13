m <- matrix(c(1, 4, 2, 5, 3, 6), nrow=2, ncol=3)

for(x in 1:3){
    if(x%%2 != 0){
        print(mean(m[,x]))
    }
}