coverage <- as.matrix(read.csv("coverage.csv",sep=";"))

testNum <- dim(coverage)[1]
unitNum <- dim(coverage)[2]

totalCoverageSum <- vector("integer", testNum)

for (t in 1:testNum) {
  totalCoverageSum[t] = sum(coverage[t, ])
}

sortedByTotalSumRet <- sort(totalCoverageSum, index.return = TRUE)
sortedByTotalSum = sortedByTotalSumRet$ix

sortedByAdditionalSum <- rep(0, testNum)
testUsed <- rep(FALSE, testNum)
unitProb <- rep(1.0, testNum)

eps <- 1e-5

for (rank in 1:testNum) {
  bestTestProbSum <- -1
  bestTestTotalSum <- -1
  for (candTest in 1:testNum) {
    if (testUsed[candTest])
      next
    probSum  <- 0.0
    for (u in 1:unitNum)
      probSum <- probSum + coverage[candTest, u] * unitProb[u]
    if (probSum > bestTestProbSum 
        || (abs(probSum - bestTestProbSum) < eps && totalCoverageSum[candTest] > bestTestTotalSum)) {
      bestTest <- candTest
      bestTestProbSum <- probSum
      bestTestTotalSum <- totalCoverageSum[candTest]
    }
  }
  sortedByAdditionalSum[rank] <- bestTest
  testUsed[bestTest] <- TRUE
  for (u in 1:unitNum) {
    if (coverage[bestTest, u]) 
      unitProb[u] = 0.0;
  }
}

print(sortedByTotalSum)
print(sortedByAdditionalSum)