object HelloWorld {
  def main(args: Array[String]): Unit = {
    val joinData = Set(
    (1,(Set(101, 102),(101,5))),
    (1,(Set(101, 102),(102,3))),
    (2,(Set(103, 104),(103,2))),
    (3,(Set(105, 101, 103, 102),(104,4))))

    val a = joinData.flatMap { case (uid, (leftSet, (rightPid, rightWeight))) =>
        leftSet.map(l => ((l, rightPid), rightWeight))
      }.map { case ((l, r), w) => (l, Array((r, w))) }
    println(joinData)
    println(a)

  }
  
}





/*
Set(
    Set(((101,101),5), ((102,101),5)), 
    Set(((101,102),3), ((102,102),3)), 
    Set(((103,103),2), ((104,103),2)), 
    Set(((105,104),4), ((101,104),4), ((103,104),4), ((102,104),4))
)

((104,103),2), 
((101,102),3), 
((102,104),4), 
((103,104),4), 
((102,102),3), 
((101,101),5), 
((101,104),4), 
((103,103),2), 
((102,101),5), 
((105,104),4),

((102,101),5), 
((105,104),4)


Set((102,[Lscala.Tuple2;@60285225), (101,[Lscala.Tuple2;@45820e51), (102,[Lscala.Tuple2;@e874448), (101,[Lscala.Tuple2;@1500955a), (102,[Lscala.Tuple2;@6043cd28), (103,[Lscala.Tuple2;@29b5cd00), (105,[Lscala.Tuple2;@cb51256), (101,[Lscala.Tuple2;@7113b13f), (104,[Lscala.Tuple2;@7ce6a65d), (103,[Lscala.Tuple2;@42d8062c))
*/
