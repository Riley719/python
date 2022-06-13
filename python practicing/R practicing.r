m <- matrix(c(1, 4, 2, 5, 3, 6), nrow=2, ncol=3)

for(x in 1:3){
    if(x%%2 != 0){
        print(mean(m[,x]))
    }
}

matrix <- matrix(c(3, 0, -3, 2, -1, -4, 1, -2, -10), nrow=3, ncol=3)

for(x in 1:3){
    print(mean(matrix[,x]))
}

c <- matrix[1,] + matrix[3,]

plot(c, type="b")

print(m)

setwd("Desktop")

getwd()

di <- read.table("DI4domain.csv", sep=",", header=T))
plot(di$Kakei, type="l", ylim=c(10, 70))
par(new=T)
plot(di$Kigyo, type="l", col="blue", ylim=c(10, 70))

boxplot(di$Kakei, di$Kigyo, names=c("Kakei", "Kigyo"))

plot(di$Kakei, di$Kigyo, xlim=c(10, 70), ylim=c(10, 70))

par(new=T)
y <- function(x){ return(x) }
plot(y, type="l", xlim=c(10, 70), col="blue")

result = lm(Kigyo~Kakei, data=di)
summary(result)

library(ggplot2)
gp <- ggplot(data=di, aes(x=Kakei, y=Kigyo))
gp <- gp + geom_point()
gp <- gp + geom_smooth()
gp <- gp + theme_bw()
print(gp)

install.packages("ggplot2", dependencies = TRUE)

library(resshape2)
di4violin <- melt(di, id.vars="Month", variable.name="domain", value.name="di")
gp <- ggplot(data=di4violin, aes(x=domain, y=di, color=domain))
gp <- gp + geom_violin()
gp <- gp + theme_gray()
print(gp)