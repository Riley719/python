setwd("Desktop")
getwd()

didomain <- read.table("DI4domain.csv", sep=",", header=T)
diarea <- read.table("DI4area.csv", sep=",", header=T)
list_diarea <- list(
    diarea$Japan, diarea$Hokkaido, diarea$Tohoku,
    diarea$Kanto, diarea$Kanto.north.,
    diarea$Kanto.south., diarea$Kanto.Tokyo.,
    diarea$Koushinetsu, diarea$Tokai,
    diarea$Hokuriku, diarea$Kinki,
    diarea$Chugoku, diarea$Shikoku,
    diarea$Kyusyu, diarea$Okinawa)

for(x in 1:15){
    print(cor(didomain$Koyou, list_diarea[[x]]))
}

didomain <- read.table("DI4domain.csv", sep=",", header=T)
diarea <- read.table("DI4area.csv", sep=",", header=T)

min_cor <- data.frame(didomain$Koyou, diarea$Okinawa)

result <- lm(didomain$Koyou~diarea$Okinawa, data = min_cor)
summary(result)

plot(diarea$Okinawa, didomain$Koyou, xlab="Koyou", ylab="Okinawa")

plot(didomain$Koyou, type="l")


didomain <- read.table("DI4domain.csv", sep=",", header=T)
sal <- read.table("hon-maikin-kyo-jissu.csv", sep=",", header=T)

sal_x <- sal$所定内.労働時間..当年.[445:516]
koyou_y <- didomain$Koyou[169:240]

cor(sal_x, koyou_y)

getwd()
setwd("Desktop")

didomain <- read.table("DI4domain.csv", sep=",", header=T)
yosoku <- read.table("yosoku.csv", sep=",", header=T)

yosoku_x <- as.numeric(yosoku$NextMonth[38:109])
koyou_y <- didomain$Koyou[169:240]

cor(yosoku_x, koyou_y)

default.par <- par()
mai <- par()$mai
mai[4] <- mai[1]
par(mai = mai)

plot(yosoku_x, type="l", ylab="yosoku", xlab="month", col="blue")
par(new=T)
plot(koyou_y, type="l", ylab="", axes=FALSE, xlab="", col="red")
axis(4)
mtext("koyou", side=4, line=3)

koyou_y

death <- read.table("number_of_death.csv", sep=",", header=T)
popu <- read.table("Popu.csv", sep=",", header=T)
med <- read.table("med.csv", sep=",", header=T)

popu$Popu
death$death
med$med

per <- rep(0,28)

for(i in 1:28){
    per[i] = 1000 * death$death[i] / popu$Popu[i]
}

cor(med$med, per[13:26])
