provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "web_server" {
  ami           = "ami-0abcdef1234567890"  # Replace with latest Amazon Linux AMI
  instance_type = "t2.micro"
  key_name      = "my-key-pair"

  tags = {
    Name = "AI-Web3-Server"
  }
}

resource "aws_s3_bucket" "static_site" {
  bucket = "ai-web3-static-site"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

resource "aws_cloudfront_distribution" "cdn" {
  origin {
    domain_name = aws_s3_bucket.static_site.bucket_regional_domain_name
    origin_id   = "S3Origin"
  }

  enabled = true

  default_cache_behavior {
    viewer_protocol_policy = "redirect-to-https"
    target_origin_id       = "S3Origin"
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}
