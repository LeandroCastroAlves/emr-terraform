resource "aws_emr_cluster" "this" {
  name          = var.cluster_name
  release_label = "emr-6.15.0"
  applications  = ["Spark", "Hadoop"]

  log_uri = "s3://${var.log_bucket}/emr-logs/"

  service_role = aws_iam_role.emr_service_role.arn

  ec2_attributes {
    instance_profile = aws_iam_instance_profile.emr_profile.arn
  }

  master_instance_group {
    instance_type  = "m5.xlarge"
    instance_count = 1
  }

  core_instance_group {
    instance_type  = "m5.xlarge"
    instance_count = 2
  }

  termination_protection = false
  keep_job_flow_alive_when_no_steps = true

}

resource "aws_s3_bucket" "emr_logs" {
  bucket = "leandro-emr-logs-dev"
}

resource "aws_s3_bucket_versioning" "emr_logs" {
  bucket = aws_s3_bucket.emr_logs.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "emr_logs" {
  bucket = aws_s3_bucket.emr_logs.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "emr_logs" {
  bucket = aws_s3_bucket.emr_logs.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
