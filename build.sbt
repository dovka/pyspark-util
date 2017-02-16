name := "pyspark-utils"

version := "0.0.2"

organization := "TargetHolding"

scalaVersion := "2.11.8"

credentials += Credentials(Path.userHome / ".ivy2" / ".sbtcredentials")

licenses += "Apache-2.0" -> url("http://opensource.org/licenses/Apache-2.0") 

libraryDependencies ++= Seq(
	"net.razorvine" % "pyrolite" % "4.10",
	"org.apache.spark" %% "spark-core" % "2.1.0",
	"org.apache.spark" %% "spark-streaming" % "2.1.0"
)

javacOptions ++= Seq("-source", "1.7", "-target", "1.7")

EclipseKeys.withSource := true
