# creates a plot of GC skew given a single string sequence file defined as myseq.
#
#
# Using seqinR package this command will convert a fasta file into the correct format for gcskew
# read.fasta(file = "filename", as.string = FALSE, 
# forceDNAtolower = TRUE, set.attributes = FALSE, seqonly = TRUE, strip.desc = TRUE)
gcskew <- function(x) {
  if (!is.character(x) || length(x) > 1)
    stop("single string expected")
tmp <- tolower(s2c(x))
nC <- sum(tmp =="c")
nG <- sum(tmp =="g")
if(nC+nG == 0)
  return(NA)
return(100* (nC-nG)/(nC+nG))
}

# Here you can adjust step and window size
step <- 5000
wsize <- 5000

starts <- seq(from = 1, to = nchar(myseq), by = step)
starts <- starts[-length(starts)]
n <- length(starts)
result <- numeric(n)
for(i in seq_len(n)){
  result[i] <- gcskew(substr(myseq, starts[i], starts[i] + wsize - 1))
  }

xx <- starts/1000
yy <- result
n <- length(result)
hline <- 0
plot(yy ~ xx, type = "n", axes = FALSE, ann=FALSE, ylim = c(-10,10))

# This will begin the plotting process
polygon(c(xx[1], xx, xx[n]), c(min(yy), yy, min(yy)), col = "black", border = NA)
usr <- par("usr")
rect(usr[1], usr[3], usr[2], hline, col = "white", border = NA)
lines(xx,yy)
abline(h=hline)
box()
axis(1, at = seq(0, 1600, by = 200))

# Plot labels
title(xlab = "Megaplasmid Position (Kbp)", ylab = "(C-G)/(C+G) %", main = expression(paste("GC skew in ", italic(Pseudomonas ~ ~ syringae ~ ~ lac ~ ~ 107)," pMP")))