variable "cluster_name" {
  default = "emr-cluster-ec2"
}

variable "log_bucket" {
  default = "emr-logs-dev"
  description = "Bucket S3 para logs do EMR"
}
